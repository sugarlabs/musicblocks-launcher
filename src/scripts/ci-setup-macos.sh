#!/usr/bin/env bash

set -eux 


cd src
yarn install
git clone https://github.com/sugarlabs/musicblocks
brew install gnu-sed
gsed -i 's/sed/gsed/g' patch.sh
sh ./patch.sh

