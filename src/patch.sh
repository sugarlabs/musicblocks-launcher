#!/bin/sh
sed -i "s,window.isElectron == true,true,g" musicblocks/js/*.js
sed -i "s,confirm(,false \&\& confirm(,g" musicblocks/js/SaveInterface.js
sed -i "s,e.preventDefault();,,g" musicblocks/js/SaveInterface.js
sed -i 's,e.returnValue = "";,,g' musicblocks/js/SaveInterface.js

