#! /bin/bash

set -ex

config="my_config"

pushd ..
CONFIG_NAMES=$config python main_batch.py
popd