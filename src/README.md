# musicblocks-app
Electron 9 App for Musicblocks (https://github.com/sugarlabs/musicblocks)
Musicblocks desktop electron app for Windows, Linux and MacOS (untested). 

# Get Started
## Users
* Download the latest release

On Linux, make sure you give the `x` bit, for execution permission. 
```bash
chmod +x Musicblocks*.AppImage
```

On Windows, double click the .exe to run a portable version of musicblocks

On macOS, (untested), double click the `*.dmg` file and follow the on screen instructions

## Developers
If you are interested in distributing this electron package in some other format, 
you may like to use `./patch.sh`. Please reference the origin of the source to `./patch.sh` 
as it would be helpful for other developers to get an updated copy

The following are instructions to build AppImages (Linux), EXE (Windows).

### AppImages
AppImages are a portable executable binaries built on the oldest distribution for 
wider compatability. AppImages work out of the box without configuration, or any package manager.

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
this will create a Musicblocks AppImage in `./dist/appimage`


### Flatpak
See [Flatpak for Musicblocks](https://github.com/sugarlabs/musicblocks-launcher)


### Windows Executables
To build Musicblocks binaries on Windows, you need a CYGWIN / MSYS2 / WSL2 interface 
which provides the latest GNU sed. Make sure `sed` is executable from the terminal
before proceeding

```bash
git clone https://github.com/srevinsaju/musicblocks-app  # clone this repository
cd musicblocks-app
git clone https://github.com/sugarlabs/musicblocks [--depth=1]
yarn install
./patch.sh  # patches the musicblocks-app so that it is compatible with electron
npx electron-builder --win --publish never
```
Will automatically create a `dist` folder with a `Musicblocks*.exe`


### MacOS Executables
I do not own a macOS, so I cannot test macOS. Please let me know if `*.dmg` from the continuous
releases work on your macOS desktop, if not feel free to create an issue [here](https://github.com/srevinsaju/musicblocks-app/issues) and not 
at the Musicblocks repository.


## License 
This software is free, ["Free as in Freedom"](https://www.gnu.org/philosophy/free-sw.en.html). 
The original source code of the Musicblocks web interface is licensed under GNU AGPL.
The source code of the [Musicblocks](https://musicblocks.sugarlabs.org) is available
at [GitHub](https://github.com) repository: 
[https://github.com/sugarlabs/musicblocks](https://github.com/sugarlabs/musicblocks)


Continuous Integration, Electron configuration files proudly licensed under MIT
```

MIT License

Copyright (c) 2020 Srevin Saju

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
