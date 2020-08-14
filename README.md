Music Blocks Launcher
============

This repository contains the files needed to build the Flatpak application for Music Blocks.

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

### Creating AppImage Binaries
1. Clone the [musicblocks-app](https://github.com/srevinsaju/musicblocks-app) GitHub repository and clone [musicblocks](https://github.com/sugarlabs/musicblocks.git) into the musicblocks-app directory.

(The following are patch fixes that I'll create actual diff patches for – for now these are the changes)

2. As of 2020-08-14, musicblocks-app has a bug that creates an infinite loop when closing the app. To fix this, comment out the following code in `main.js`:

```
 mainWindow.on('close', function(e){
    var choice = require('electron').dialog.showMessageBoxSync(this,
        {
          type: 'question',
          buttons: ['Yes', 'No'],
          title: 'Confirm',
          message: 'Are you sure you want to quit? You might have unsaved changes.'
       });
       if (choice == 1) {
         e.preventDefault();
       }
  });
  ```
  
  3. You'll also have to add the following line underneath `mainWindow.loadFile('musicblocks/index.html')`:
  
  ```
  mainWindow.removeMenu()
  ```
  
  4. Next, set `filename` to `defaultfilename` at line 87 in `musicblocks/js/SaveInterface.js` and comment out the `window.onbeforeunload` function at the end of the file.
  
  5. Enter the following commands into a command line window in the `musicblocks-app` directory:
  
  ```
  $ npm install
  $ npm install -g electron-builder
  $ electron-builder build --linux --armv7l
  $ electron-builder build --linux --arm64
  $ electron-builder build --linux x64
  ```
  
  6. Rename the create AppImage files (found in the `dist` folder) to:
  * MusicBlocks-[version]-aarch64.AppImage (for --armv7l)
  * MusicBlocks-[version]-arm.AppImage (for --arm64)
  * MusicBlocks-[version]-x86_64.AppImage (for --x64)
  
  7. Create a release in this repository with the binaries attached.
