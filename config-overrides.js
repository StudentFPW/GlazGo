const { override } = require('customize-cra')
const { addWebpackModuleRule } = require('customize-cra')

module.exports = override(
    addWebpackModuleRule({
        test: /\.svg$/i,
        issuer: /\.[jt]sx?$/,
        use: [{ loader: '@svgr/webpack', options: { dimensions: false } }],
    }),
  );
