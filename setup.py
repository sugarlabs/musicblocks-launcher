from distutils.core import setup
import os

setup(name='Music Blocks Launcher',
    version='1.0',
    description='Flatpak launcher for Music Blocks',
    url="https://github.com/sugarlabs/musicblocks-launcher",
    author="Christopher Liu",
    author_email="christopherliu@sorcero.com",
    data_files=[
        ('share/metainfo', ['data/org.sugarlabs.MusicBlocks.appdata.xml']),
        ('share/icons/hicolor/48x48/apps', ['data/org.sugarlabs.MusicBlocks.svg']),
        ('share/applications', ['data/org.sugarlabs.MusicBlocks.desktop']),
        ('share/musicblocks', ['data/org.sugarlabs.MusicBlocks.ui']),
        ('bin', ['launcher'])
        ]
    )
