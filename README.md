Music Blocks Launcher
============

This repository contains the files needed to build the Flatpak application for Music Blocks.

### Creating AppImage Binaries
1. Clone the [musicblocks-app](https://github.com/srevinsaju/musicblocks-app) GitHub repository and clone [musicblocks](https://github.com/sugarlabs/musicblocks.git) into the musicblocks-app directory (`musicblocks` should be nested insided `musicblocks-app`).

2. Ensure that the correct version of musicblocks is downloaded (however specified in the the metadata files for the flatpak app). To change versions, use the corresponding tag (while in the musicblocks directory):

```
$ git checkout tags/[tag_name]
```

3. Apply `musicblocks-app.patch` and `musicblocks.patch` to the respective directories:

```
$ git apply patches/musicblocks-app.patch
$ cd musicblocks
$ git apply ../patches/musicblocks.patch
```

4. Enter the following commands into a command line window in the `musicblocks-app` directory:

```
$ npm install
$ npm install -g electron-builder
$ electron-builder build --linux --armv7l
$ electron-builder build --linux --arm64
$ electron-builder build --linux x64
```

5. Rename the create AppImage files (found in the `dist` folder) to:
* MusicBlocks-[version]-aarch64.AppImage (for --armv7l)
* MusicBlocks-[version]-arm.AppImage (for --arm64)
* MusicBlocks-[version]-x86_64.AppImage (for --x64)

6. Create a release in this repository with the binaries attached.

### Installation
1. Install `flatpak-builder`, the freedesktop runtime and SDK, and the electron baseapp:

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

You can either launch Music Blocks from the applications menu or run it directly from the command line:
```
$ flatpak run org.sugarlabs.MusicBlocks
```

### Adding to the Launcher
To add screenshots:
* Screenshots must be generally 16x9 and no larger than 1600px by 900px.
* Add the screenshot to `org.sugarlabs.MusicBlocks.appdata.xml`.
* Screenshots should follow [AppStream specifications](https://www.freedesktop.org/software/appstream/docs/sect-Metadata-Application.html#tag-dapp-screenshots).
