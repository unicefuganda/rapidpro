var common = require('./common');

module.exports = function(config) {
  config.set(common({
    plugins: ['karma-safari-launcher'],
    browsers: ['Safari']
  }));
};
