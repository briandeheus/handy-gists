#!/bin/bash

package_json='
{
  "name": "frontend",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "babel-plugin-transform-class-properties": "^6.24.1",
    "babel-plugin-transform-object-rest-spread": "^6.26.0",
    "babel-preset-env": "^1.7.0",
    "babel-preset-react": "^6.24.1",
    "node-sass": "^4.11.0",
    "parcel-bundler": "^1.11.0",
    "react": "^16.8.3",
    "react-dom": "^16.8.3"
  }
}'

babelrc='
{
  "presets": ["env", "react"],
  "plugins": ["transform-class-properties", "transform-object-rest-spread"]
}
'

echo -e "$package_json" > package.json
