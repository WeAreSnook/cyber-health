#!/bin/bash

gem install dpl --pre
npm install http-server -g
cd accessibility || exit
npm install --unsafe-perm -g chromedriver
npm install