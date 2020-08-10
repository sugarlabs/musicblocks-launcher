from distutils.core import setup
import os

setup(name='Music Blocks Launcher',
    version='1.1.1',
    description='Flatpak launcher for Music Blocks',
    url="https://github.com/sugarlabs/musicblocks-launcher",
    data_files=[
        ('share/appdata', ['data/org.sugarlabs.MusicBlocks.appdata.xml']),
        ('share/icons/hicolor/scalable/apps', ['data/org.sugarlabs.MusicBlocks.svg']),
        ('share/applications', ['data/org.sugarlabs.MusicBlocks.desktop']),
        ]
    )
