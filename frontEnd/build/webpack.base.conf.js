var path = require('path')

module.exports = {
  node: {
    fs: 'empty'
  },
  entry: {
    app: './src/app.js'
  },
  output: {
    path: path.resolve(__dirname, '../dist/webstatic'),
    publicPath: '/webstatic/',
    filename: '[name].js'
  },
  externals: {
    'jquery': 'jQuery'
  },
  resolve: {
    alias: {
      vue: 'vue/dist/vue.js',
      src: path.resolve(__dirname, '../src'),
      commonFunc: path.resolve(__dirname, '../src/assets/js/common.js')
    },
    extensions: ['', '.js', '.vue', '.less']
  },
  resolveLoader: {
    root: path.join(__dirname, 'node_modules')
  },
  module: {
    loaders: [
      {
        test: /\.vue$/,
        loader: 'vue'
      },
      {
        test: /\.js$/,
        exclude: /node_modules|vue\/dist|vue-router\/|vue-loader\/|vue-hot-reload-api\//,
        loader: 'babel',
        query: {compact: false}
      },
      {
        test: /\.json$/,
        loader: 'json'
      },
      {
        test: /\.less$/,
        loader: 'css!less'
      },
      {
        test: /\.scss$/,
        loader: "style!css!sass"
      },
      {
        test: /\.css$/,
        loader: 'css'

      },
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'url',
        query: {
          limit: 10000,
          name: '[name].[ext]?[hash]'
        }
      },
      {
        test: /\.(eot|woff|ttf|svg)\??.*$/,
        loader: 'url-loader?limit=30000&name=[name]-[hash].[ext]'
      },
      {
        test: /\.styl$/,
        loader: 'style-loader!css-loader!stylus-loader'
      }
    ]
  },
  vue: {
    loaders: {
      js: 'babel!eslint',
      less: 'vue-style!css!less',
      sass: 'vue-style!css!sass'
    }
  },
  eslint: {
    formatter: require('eslint-friendly-formatter')
  }
}
