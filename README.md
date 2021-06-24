# Music Blocks Launcher

Electron 13 desktop app for Music Blocks
(https://github.com/sugarlabs/musicblocks) for Linux, Windows, and MacOS.

# Get Started

## Users

* Download the latest release

On Linux (AppImage), make sure you give the `x` bit for execution permission. 

```bash
chmod +x MusicBlocks*.AppImage
```

On Windows, double click the .exe to run a portable version of musicblocks.

On MacOS, double click the .dmg file and follow the on screen instructions.
When opening the app for the first time, open from the Applications folder by
right-clicking and pressing "Open" (this may require clicking "Open" twice).
This is because the .dmg binaries are unsigned.

## Developers

If you are interested in distributing this Electron package in some other
format, you may like to use `./src/patch.sh`. Please reference the origin of
the source to `./src/patch.sh` as it would be helpful for other developers to
get an updated copy.

The following are instructions to build AppImages (Linux), Flatpak (Linux),
EXE (Windows), and DMG (MacOS) binaries.

### AppImages

AppImages are a portable executable binaries built on the oldest distribution
for wider compatability. AppImages work out of the box without configuration
or any package manager.

```bash
git clone https://github.com/sugarlabs/musicblocks-launcher  # clone this repository
cd musicblocks-launcher
cd src
yarn install
git clone https://github.com/sugarlabs/musicblocks [--depth=1]
sh ./patch.sh # patches the app so that it is compatible with electron
npx electron-builder --linux appimage --publish never # defaults to current arch, use a flag for other archs
```

This will create a Music Blocks AppImage in `./dist/`.

### Flatpak

To build the Flatpak app for Music Blocks, you must have the Flatpak manifest
`./data/org.sugarlabs.MusicBlocks.yaml` in your current working directory.

1. Install `flatpak-builder`, the freedesktop runtime and SDK, and the electron
baseapp:

```
$ flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
$ flatpak install flathub org.flatpak.Builder
$ flatpak install flathub org.freedesktop.Platform//19.08 org.freedesktop.Sdk//19.08
$ flatpak install flathub org.electronjs.Electron2.BaseApp
```

2. Build and install the application:
   
```
$ flatpak-builder --force-clean --repo=repo build org.sugarlabs.MusicBlocks.yaml
$ flatpak build-bundle repo musicblocks.flatpak org.sugarlabs.MusicBlocks stable
$ flatpak install musicblocks.flatpak
```

3. Run the application:
   You can either launch Music Blocks from the applications menu or run it
   directly from the command line:
   
```
$ flatpak run org.sugarlabs.MusicBlocks
```

#### Adding to the Launcher

To add screenshots:

* Screenshots must be generally 16x9 and no larger than 1600px by
  900px.
* Add the screenshot to `org.sugarlabs.MusicBlocks.appdata.xml`.
* Screenshots should follow [AppStream specifications](https://www.freedesktop.org/software/appstream/docs/sect-Metadata-Application.html#tag-dapp-screenshots).

### Windows Executables

To build Music Blocks binaries on Windows, you need a CYGWIN / MSYS2 / WSL2
interface which provides the latest GNU sed. Make sure `sed` is executable from
the terminal before proceeding.

```bash
git clone https://github.com/sugarlabs/musicblocks-launcher  # clone this repository
cd musicblocks-launcher
cd src
git clone https://github.com/sugarlabs/musicblocks [--depth=1]
yarn install
./patch.sh  # patches the app so that it is compatible with electron
npx electron-builder --win --publish never
```

This will automatically create a `dist` folder with a `MusicBlocks*.exe`.

### MacOS Executables

To build Music Blocks binaries on MacOS, you will need the Homebrew package
manager or to otherwise install `gnu-sed` in order to patch musicblocks to be
compatible with electron.

```bash
git clone https://github.com/sugarlabs/musicblocks-launcher  # clone this repository
cd musicblocks-launcher
cd src
npm i
brew install gnu-sed # required to apply patch.sh
git clone https://github.com/sugarlabs/musicblocks [--depth=1]
gsed -i 's/sed/gsed/g' patch.sh
sh ./patch.sh # patches the musicblocks-app so that it is compatible with electron
npx electron-builder --mac --publish never
```

This will automatically create a `dist` folder with a `MusicBlocks*.dmg`.

## License

This software is free, ["Free as in Freedom"](https://www.gnu.org/philosophy/free-sw.en.html). 
The original source code of the Music Blocks web interface is licensed under GNU AGPL.
The source code of the [Music Blocks](https://musicblocks.sugarlabs.org) is available
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
