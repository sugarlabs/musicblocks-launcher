#!/bin/sh
sed -i "s,window.isElectron == true,true,g" musicblocks/js/*.js
sed -i "s,return \"\";,,g" musicblocks/js/SaveInterface.js
sed -i "s,event.preventDefault();,,g" musicblocks/js/SaveInterface.js
sed -i 's,event.returnValue = "";,,g' musicblocks/js/SaveInterface.js
sed -i 's, is a collection of tools for exploring fundamental musical concepts in a fun way.,,g' musicblocks/js/turtledefs.js
