Music Blocks Launcher
============

This repository contains the files needed to build the Flatpak application for Music Blocks.

### Installation
1. Install `flatpak-builder` and the GNOME runtime and SDK:

```
$ flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
$ flatpak install flathub org.flatpak.Builder
$ flatpak install flathub org.gnome.Platform//3.36 org.gnome.Sdk//3.36
```

2. Build and install the application:

```
$ flatpak-builder --force-clean --repo=repo build org.sugarlabs.Musicblocks.json
$ flatpak build-bundle repo musicblocks.flatpak org.sugarlabs.Musicblocks
$ flatpak install musicblocks.flatpak
```

3. Run the application:

You can either launch Music Blocks from the applications menu or run it directly from the command line:
```
$ flatpak run org.sugarlabs.Musicblocks
```

### Adding to the Launcher
To add screenshots:
* Screenshots must be generally 16x9 and no larger than 1600px by 900px.
* Add the screenshot to `org.sugarlabs.Musicblocks.appdata.xml`
* Screenshots should follow [AppStream specifications](https://www.freedesktop.org/software/appstream/docs/sect-Metadata-Application.html#tag-dapp-screenshots).
