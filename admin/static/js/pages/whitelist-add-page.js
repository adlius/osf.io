'use strict';

var $ = require('jquery');

var $osf = require('js/osfHelpers');
var ko = require('knockout');

var AddWhitelistPreprintProvidersViewModel = function() {
    var self = this;
    self.preprint_providers = ko.observableArray([]);
    self.providers_added = ko.observableArray([]);
    self.share_api_url = window.templateVars.share_api_url + "/api/v2/search/creativeworks/_search";
    self.api_v2_url = window.templateVars.api_v2_url + "preprint_providers/"
};

AddWhitelistPreprintProvidersViewModel.prototype.updatePreprintProviders = function() {
    var self = this;
    var query_obj = {"query":{"bool":{"must":{"query_string":{"query":"*"}},"filter":[{"terms":{"types":["preprint"]}}]}},"from":0,"aggregations":{"sources":{"terms":{"field":"sources","size":500}}}};

    var share_api_call =  $.ajax({
        url: self.share_api_url,
        type: "POST",
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify(query_obj)
    });

    var api_v2_call =  $.get(self.api_v2_url);

    $.when(share_api_call, api_v2_call).then(function (firstResponse, secondResponse) {
        var share_providers = firstResponse[0].aggregations.sources.buckets.map(function(item) {
            return item.key;
        });

        var internal_providers = secondResponse[0].data.map(function(item) {
            return item.attributes.name;
        });

        var external_providers = share_providers.filter( function( item ) {
            return internal_providers.indexOf( item ) < 0;
        });

        external_providers.forEach(function(item){
            self.preprint_providers.push({
                "name": item
            });
        });

    });

};

$(document).ready(function() {
    var viewModel = new AddWhitelistPreprintProvidersViewModel();
    ko.applyBindings(viewModel);
    viewModel.updatePreprintProviders();
});

