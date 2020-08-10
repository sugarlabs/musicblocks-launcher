Music Blocks Launcher
============

This repository contains the files needed to build the Flatpak application for Music Blocks.

### Installation
1. Install `flatpak-builder`, the freedesktop runtime and SDK, the electron baseapp, and the node10 SDK extension:

```
$ flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
$ flatpak install flathub org.flatpak.Builder
$ flatpak install flathub org.freedesktop.Platform//19.08 org.freedesktop.Sdk//19.08
$ flatpak install flathub org.electronjs.Electron2.BaseApp
$ flatpak install flathub org.freedesktop.Sdk.Extension.node10
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
