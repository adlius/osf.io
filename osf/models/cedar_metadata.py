import copy

from django.core.exceptions import ValidationError
from django.db import models
from jsonschema import validate as jsonschema_validate, ValidationError as JsonSchemaValidationError

from osf.models.base import BaseModel, ObjectIDMixin
from osf.utils.datetime_aware_jsonfield import DateTimeAwareJSONField

IGNORED_REQUIRED_PROPERTIES = {
    '@id',
    'schema:isBasedOn',
    'schema:name',
    'schema:description',
    'pav:createdOn',
    'pav:createdBy',
    'pav:lastUpdatedOn',
    'oslc:modifiedBy',
}


class CedarMetadataTemplate(ObjectIDMixin, BaseModel):
    schema_name = models.CharField(max_length=255, default=None)
    cedar_id = models.CharField(max_length=255, default=None)
    template = DateTimeAwareJSONField(default=dict)
    active = models.BooleanField(default=True)
    template_version = models.PositiveIntegerField()
    should_index_for_search = models.BooleanField(default=False)

    class Meta:
        unique_together = ('cedar_id', 'template_version')

    def __unicode__(self):
        return f'(name=[{self.schema_name}], version=[{self.template_version}], id=[{self.cedar_id}])'

    def get_semantic_iri(self):
        return self.cedar_id

    def is_active(self):
        return self.active


class CedarMetadataRecord(ObjectIDMixin, BaseModel):

    guid = models.ForeignKey('Guid', on_delete=models.CASCADE, related_name='cedar_metadata_records')
    template = models.ForeignKey('CedarMetadataTemplate', on_delete=models.CASCADE)
    metadata = DateTimeAwareJSONField(default=dict)
    is_published = models.BooleanField(default=False)

    class Meta:
        unique_together = ('guid', 'template')

    def __unicode__(self):
        return f'(guid=[{self.guid._id}], template=[{self.template._id}])'

    def get_template_semantic_iri(self):
        return self.template.get_semantic_iri()

    def get_template_name(self):
        return self.template.schema_name

    def get_template_version(self):
        return self.template.template_version

    def clean(self):
        if self.is_published:
            schema = copy.deepcopy(self.template.template)
            required = schema.get('required')
            if isinstance(required, list):
                required[:] = [prop for prop in required if prop not in IGNORED_REQUIRED_PROPERTIES]
            context_schema = schema.get('properties', {}).get('@context', {})
            context_required = context_schema.get('required')
            if (
                isinstance(self.metadata, dict)
                and isinstance(self.metadata.get('@context'), dict)
                and isinstance(context_required, list)
            ):
                allowed_context_fields = set(context_required)
                self.metadata['@context'] = {
                    key: value
                    for key, value in self.metadata['@context'].items()
                    if key in allowed_context_fields
                }

            try:
                jsonschema_validate(self.metadata, schema)
            except JsonSchemaValidationError as e:
                raise ValidationError(
                    f'CEDAR metadata does not validate against template "{self.template.schema_name}": {e.message}'
                )

    def save(self, *args, **kwargs):
        self.clean()
        self.guid.referent.update_search()
        return super().save(*args, **kwargs)
