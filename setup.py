from distutils.core import setup
import os
import platform
from zipfile import ZipFile

arch = platform.machine()
if arch == 'aarch64':
    with ZipFile('build/MusicBlocks-aarch64.zip', 'r') as zipObj:
        zipObj.extractall('build')
        os.rename('build/MusicBlocks-aarch64', 'build/MusicBlocks')
elif arch == 'x86_64':
    with ZipFile('build/MusicBlocks-x86_64.zip', 'r') as zipObj:
        zipObj.extractall('build')
        os.rename('build/MusicBlocks-x86_64', 'build/MusicBlocks')
else:
    with ZipFile('build/MusicBlocks-arm.zip', 'r') as zipObj:
        zipObj.extractall('build')
        os.rename('build/MusicBlocks-arm', 'build/MusicBlocks')

os.chmod('build/MusicBlocks', 0o755)

setup(name='Music Blocks Launcher',
    version='1.1.1',
    description='Flatpak launcher for Music Blocks',
    url="https://github.com/sugarlabs/musicblocks-launcher",
    data_files=[
        ('share/metadata', ['data/org.sugarlabs.MusicBlocks.appdata.xml']),
        ('share/icons/hicolor/scalable/apps', ['data/org.sugarlabs.MusicBlocks.svg']),
        ('share/applications', ['data/org.sugarlabs.MusicBlocks.desktop']),
        ('bin', ['build/MusicBlocks'])
        ]
    )
