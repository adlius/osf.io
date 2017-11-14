var webpack = require('webpack');
var path = require('path');
var common = require('../webpack.common.config.js');
var BundleTracker = require('webpack-bundle-tracker');

var websiteRoot = path.join(__dirname, '..', 'website', 'static');

var adminRoot = path.join(__dirname, 'static');

var staticAdminPath = function(dir) {
    return path.join(adminRoot, dir);
};

// Adding bundle tracker to plugins
var plugins = common.plugins.concat([
    // for using webpack with Django
    new BundleTracker({filename: './webpack-stats.json'}),
]);

common.output = {
    path: './static/public/js/',
    // publicPath: '/static/', // used to generate urls to e.g. images
    filename: '[name].js',
    sourcePrefix: ''
};

var config = Object.assign({}, common, {
    entry: {
        'admin-base-page': staticAdminPath('js/pages/base-page.js'),
        'prereg-admin-page': staticAdminPath('js/pages/prereg-admin-page.js'),
        'admin-registration-edit-page': staticAdminPath('js/pages/admin-registration-edit-page.js'),
        'dashboard': staticAdminPath('js/sales_analytics/dashboard.js'),
        'metrics-page': staticAdminPath('js/pages/metrics-page.js'),
        'whitelist-add-page': staticAdminPath('js/pages/whitelist-add-page.js'),
        'whitelist-delete-page': staticAdminPath('js/pages/whitelist-delete-page.js')
    },
    plugins: plugins,
    debug: true,
    devtool: 'source-map',
});
config.resolve.root = [websiteRoot, adminRoot];
module.exports = config;
