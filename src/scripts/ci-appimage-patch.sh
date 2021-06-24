#!/usr/bin/env bash

set -eux

cd dist/
./*.AppImage --appimage-extract

# HACK: the electron builder, for some reason doesn't copy the asar
# into the appimage
cp linux-unpacked/resources/app.asar squashfs-root/resources/.

# repack the appimage
wget https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage
chmod +x appimagetool-x86_64.AppImage

# remove the old appimage
rm Musicblocks*.AppImage

# repackage the appimage 
./appimagetool-x86_64.AppImage squashfs-root -n -u 'gh-releases-zsync|sugarlabs|musicblocks-launcher|continuous|Musicblocks*.AppImage'
rm -rf squashfs-root
cd ..