#!/bin/sh
sed -i "s,window.isElectron == true,true,g" musicblocks/js/*.js
sed -i "s,return \"\";,,g" musicblocks/js/SaveInterface.js
sed -i "s,event.preventDefault();,,g" musicblocks/js/SaveInterface.js
sed -i 's,event.returnValue = "";,,g' musicblocks/js/SaveInterface.js
sed -i 's, is a collection of tools for exploring musical,,g' musicblocks/index.html
sed -i 's,concepts.,,g' musicblocks/index.html
