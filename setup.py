from distutils.core import setup
import os

setup(name='Music Blocks Launcher',
    version='1.0',
    description='Flatpak launcher for Music Blocks',
    url="https://github.com/sugarlabs/musicblocks-launcher",
    author="Christopher Liu",
    author_email="christopherliu@sorcero.com",
    data_files=[
        ('share/metainfo', ['launcher/data/org.sugarlabs.Musicblocks.appdata.xml']),
        ('share/icons/hicolor/48x48/apps', ['launcher/data/org.sugarlabs.Musicblocks.svg']),
        ('share/applications', ['launcher/data/org.sugarlabs.Musicblocks.desktop']),
        ('share/musicblocks', ['launcher/data/org.sugarlabs.Musicblocks.ui']),
        ('bin', ['launcher/launcher'])
        ]
    )
