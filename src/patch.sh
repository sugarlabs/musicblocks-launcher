sed -i "s,window.isElectron == true,true,g" musicblocks/js/*.js
sed -i "s,confirm(,false \&\& confirm(,g" musicblocks/js/SaveInterface.js
sed -i "s,e.preventDefault();,,g" musicblocks/js/SaveInterface.js
sed -i 's,e.returnValue = "";,,g' musicblocks/js/SaveInterface.js
sed -i 's,<title>,<!-- https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP --><meta http-equiv="Content-Security-Policy" content="default-src \x27self\x27; script-src \x27self\x27"><meta http-equiv="X-Content-Security-Policy" content="default-src \x27self\x27; script-src \x27self\x27"><title>,g' musicblocks/index.html

