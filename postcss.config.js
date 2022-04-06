module.exports = {
    plugins: {
      autoprefixer: {},
      'postcss-px-to-viewport': {
        unitToConvert: 'px',
        viewportWidth: 1920,
        unitPrecision: 3,
        viewportUnit: 'vw',
        // fontViewportUnit: 'vw',
        selectorBlackList: ['.ignore', 'el-button'],
        minPixelValue: 1,
        mediaQuery: false,
        exclude: /node_modules/
      }
    }
  }