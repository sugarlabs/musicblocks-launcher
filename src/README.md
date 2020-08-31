# musicblocks-app
Electron 9 App for Musicblocks (https://github.com/sugarlabs/musicblocks)


## Build Instructions
```bash
git clone https://github.com/srevinsaju/musicblocks-app  # clone this repository
cd musicblocks-app
git clone https://github.com/sugarlabs/musicblocks [--depth=1]
yarn install
./patch.sh  # patches the musicblocks-app so that it is compatible with electron
npx electron-builder --linux appimage --publish never
mkdir -p dist/appimage
cd dist/
./*.AppImage --appimage-extract
cp linux-unpacked/resources/app.asar squashfs-root/resources/.  # necessary step, else the patched appimage won't load CSS
wget https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage
chmod +x appimagetool-x86_64.AppImage
rm Musicblocks*.AppImage
./appimagetool-x86_64.AppImage --comp gzip squashfs-root -n
ls 
rm -rf squashfs-root
mv Musicblocks*.AppImage appimage/.
chmod +x appimage/*.AppImage
cd ..
```

Well, you don't need to do all that hardwork, get the latest release from [Releases](https://github.com/srevinsaju/musicblock-app/releases)
which is continuously built using GitHub Action CI
