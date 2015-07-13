var $ = require('jquery');
var URI = require('URIjs');
var moment = require('moment');
var ko = require('knockout');

var FilesWidget = require('js/FilesWidget');
var Fangorn = require('js/fangorn');
var $osf = require('js/osfHelpers');

var node = window.contextVars.node;

ko.bindingHandlers.osfUploader = {
    init: function(element, valueAccessor, allBindings, viewModel, bindingContext) {
        ko.cleanNode(document.getElementById(bindingContext.$root.editorId));
        //$osf.applyBindings(bindingContext.$root, bindingContext.$root.editorId);
        console.log(bindingContext);
        // var fw = new FilesWidget(
        //     element.id,
        //     node.urls.api + 'files/grid/',
        //     {
        //         onselectrow: function(item) {
        //             userClick = true;
        //             this.multiselected([item]);
        //             self.preview_value = item.data;
        //             this.path = item.data.path;
        //             self.files = item.data;

        //             var tb = this;
        //             var fileurl = "";
        //             if (item.data.kind === "file") {
        //                 var redir = new URI(item.data.nodeUrl);
        //                 redir.segment("files").segment(item.data.provider).segmentCoded(item.data.path.substring(1));
        //                 fileurl = redir.toString() + '/';
        //                 viewModel.selectedFileName(item.data.name);
        //                 viewModel.setValue(fileurl);
        //             } else {
        //                 viewModel.selectedFileName("no file selected");
        //                 fileurl = "";
        //                 viewModel.setValue(null);
        //             }
        //         },
        //         dropzone: {                                           // All dropzone options.
        //             url: function(files) {return files[0].url;},
        //             clickable : "#" + element.id,
        //             addRemoveLinks: false,
        //             previewTemplate: '<div></div>',
        //             parallelUploads: 1,
        //             acceptDirectories: false,
        //             fallback: function(){}
        //         },
        //         resolveRows: function(item) {
        //             var tb = this;
        //             item.css = '';

        //             if (item.data.addonFullname !== undefined) {
        //                 if (item.data.addonFullname !== "OSF Storage") {
        //                     item.css = "text-muted";
        //                 } 
        //             }
        //             if (tb.isMultiselected(item.id)) {
        //                 item.css = 'fangorn-selected';
        //             }
        //             var defaultColumns = [{
        //                 data: 'name',
        //                 folderIcons: true,
        //                 filter: true,
        //                 custom: Fangorn.DefaultColumns._fangornTitleColumn
        //             }];
        //             if (item.parentID) {
        //                 item.data.permissions = item.data.permissions || item.parent().data.permissions;
        //                 if (item.data.kind === 'folder') {
        //                     item.data.accept = item.data.accept || item.parent().data.accept;
        //                 }
        //             }

        //             if (item.data.uploadState && (item.data.uploadState() === 'pending' || item.data.uploadState() === 'uploading')) {
        //                 return Fangorn.Utils.uploadRowTemplate.call(tb, item);
        //             }

        //             var configOption = Fangorn.Utils.resolveconfigOption.call(this, item, 'resolveRows', [item]);
        //             return configOption || defaultColumns;
        //         },
        //         lazyLoadOnLoad: function (tree, event) {
        //             var tb = this;
        //             if (tree.data.addonFullname !== undefined) {
        //                 if (tree.data.addonFullname !== "OSF Storage") {
        //                     tree.open = false;
        //                     tree.load = false;
        //                     tree.css = "text-muted";
        //                     tree.data.permissions.edit = false;
        //                     tree.data.permissions.view = false;
        //                     if (!tree.data.name.includes(" (Only OSF Storage supported to ensure accurate versioning.)")) {
        //                         tree.data.name = tree.data.name + " (Only OSF Storage supported to ensure accurate versioning.)";
        //                     }
        //                 } else if (tree.depth === 2 && viewModel.value() === null) {
        //                     tb.multiselected([tree]);
        //                 }
        //             }
        //             tree.children.forEach(function(item) {
        //                 if (item.data.kind === "file" && item.data.provider !== "osfstorage") {
        //                     item.open = false;
        //                     item.load = false;
        //                 } else if (viewModel.value() !== null) {
        //                     var fullPath = viewModel.value().split("/");
        //                     var path = fullPath[fullPath.length - 2];
        //                     var correctedPath = "/" + path;
        //                     if (item.data.kind === "file" && item.data.path === correctedPath) {
        //                         tb.multiselected([item]);
        //                         viewModel.selectedFileName(item.data.name);
        //                     }
        //                 }

        //                 Fangorn.Utils.inheritFromParent(item, tree);
        //             });
        //             Fangorn.Utils.resolveconfigOption.call(this, tree, 'lazyLoadOnLoad', [tree, event]);
        //             Fangorn.Utils.reapplyTooltips();

        //             if (tree.depth > 1) {
        //                 Fangorn.Utils.orderFolder.call(this, tree);
        //             }
        //         }
  
        //     }
        // );
        // fw.init();
    },
    update: function(element, valueAccessor, allBindings, viewModel, bindingContext) {
        console.log("update");
        // if (FilesWidget) {
        //     console.log("exists");
        //     FilesWidget.destroy();
        // }
        var fw = new FilesWidget(
            element.id,
            node.urls.api + 'files/grid/',
            {
                onselectrow: function(item) {
                    userClick = true;
                    this.multiselected([item]);
                    self.preview_value = item.data;
                    this.path = item.data.path;
                    self.files = item.data;

                    var tb = this;
                    var fileurl = "";
                    if (item.data.kind === "file") {
                        var redir = new URI(item.data.nodeUrl);
                        redir.segment("files").segment(item.data.provider).segmentCoded(item.data.path.substring(1));
                        fileurl = redir.toString() + '/';
                        viewModel.selectedFileName(item.data.name);
                        viewModel.setValue(fileurl);
                    } else {
                        viewModel.selectedFileName("no file selected");
                        fileurl = "";
                        viewModel.setValue(null);
                    }
                },
                dropzone: {                                           // All dropzone options.
                    url: function(files) {return files[0].url;},
                    clickable : "#" + element.id,
                    addRemoveLinks: false,
                    previewTemplate: '<div></div>',
                    parallelUploads: 1,
                    acceptDirectories: false,
                    fallback: function(){}
                },
                resolveRows: function(item) {
                    var tb = this;
                    item.css = '';

                    if (item.data.addonFullname !== undefined) {
                        if (item.data.addonFullname !== "OSF Storage") {
                            item.css = "text-muted";
                        } 
                    }
                    if (tb.isMultiselected(item.id)) {
                        item.css = 'fangorn-selected';
                    }
                    var defaultColumns = [{
                        data: 'name',
                        folderIcons: true,
                        filter: true,
                        custom: Fangorn.DefaultColumns._fangornTitleColumn
                    }];
                    if (item.parentID) {
                        item.data.permissions = item.data.permissions || item.parent().data.permissions;
                        if (item.data.kind === 'folder') {
                            item.data.accept = item.data.accept || item.parent().data.accept;
                        }
                    }

                    if (item.data.uploadState && (item.data.uploadState() === 'pending' || item.data.uploadState() === 'uploading')) {
                        return Fangorn.Utils.uploadRowTemplate.call(tb, item);
                    }

                    var configOption = Fangorn.Utils.resolveconfigOption.call(this, item, 'resolveRows', [item]);
                    return configOption || defaultColumns;
                },
                lazyLoadOnLoad: function (tree, event) {
                    var tb = this;
                    if (tree.data.addonFullname !== undefined) {
                        if (tree.data.addonFullname !== "OSF Storage") {
                            tree.open = false;
                            tree.load = false;
                            tree.css = "text-muted";
                            tree.data.permissions.edit = false;
                            tree.data.permissions.view = false;
                            if (!tree.data.name.includes(" (Only OSF Storage supported to ensure accurate versioning.)")) {
                                tree.data.name = tree.data.name + " (Only OSF Storage supported to ensure accurate versioning.)";
                            }
                        } else if (tree.depth === 2 && viewModel.value() === null) {
                            tb.multiselected([tree]);
                        }
                    }
                    tree.children.forEach(function(item) {
                        if (item.data.kind === "file" && item.data.provider !== "osfstorage") {
                            item.open = false;
                            item.load = false;
                        } else if (viewModel.value() !== null) {
                            var fullPath = viewModel.value().split("/");
                            var path = fullPath[fullPath.length - 2];
                            var correctedPath = "/" + path;
                            if (item.data.kind === "file" && item.data.path === correctedPath) {
                                tb.multiselected([item]);
                                viewModel.selectedFileName(item.data.name);
                            }
                        }

                        Fangorn.Utils.inheritFromParent(item, tree);
                    });
                    Fangorn.Utils.resolveconfigOption.call(this, tree, 'lazyLoadOnLoad', [tree, event]);
                    Fangorn.Utils.reapplyTooltips();

                    if (tree.depth > 1) {
                        Fangorn.Utils.orderFolder.call(this, tree);
                    }
                }
  
            }
        );
        fw.init();

    }
};

var Uploader = function(data) {
    
    var self = this;

    self.selectedFileName = ko.observable('no file selected');

    $.extend(self, data);
};

module.exports = {
    Uploader: Uploader
};
