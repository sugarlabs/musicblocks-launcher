from setuptools import setup
import os

DATA_PATH = os.getenv('DATA_PATH')
APPDATA_PATH = os.path.join(DATA_PATH, 'metainfo')
ICON_PATH = os.path.join(DATA_PATH, 'icons/hicolor/48x48/apps')
DESKTOP_PATH = os.path.join(DATA_PATH, 'applications')
UI_PATH = os.path.join(DATA_PATH, 'musicblocks')
SCRIPTS_PATH = os.getenv('SCRIPTS_PATH')

setup(name='Music Blocks Launcher',
    version='1.0',
    description='Flatpak launcher for Music Blocks',
    url="https://github.com/sugarlabs/musicblocks-launcher",
    author="Christopher Liu",
    author_email="christopherliu@sorcero.com",
    scripts=[SCRIPTS_PATH, ['launcher']],
    data_files=[
        (APPDATA_PATH, ['data/org.sugarlabs.Musicblocks.appdata.xml']),
        (ICON_PATH, ['data/org.sugarlabs.Musicblocks.svg']),
        (DESKTOP_PATH, ['data/org.sugarlabs.Muiscblocks.desktop']),
        (UI_PATH, ['data/org.sugarlabs.Musicblocks.ui'])
        ]
    )
