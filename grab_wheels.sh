#!/bin/sh
pip download humanize --dest ./source/wheels --only-binary=:all: --python-version=3.11 
pip download pillow --dest ./source/wheels --only-binary=:all: --python-version=3.11 --platform=win_amd64
pip download pillow --dest ./source/wheels --only-binary=:all: --python-version=3.11 --platform=macosx_10_16_x86_64
pip download pillow --dest ./source/wheels --only-binary=:all: --python-version=3.11 --platform=macosx_12_0_arm64
pip download pillow --dest ./source/wheels --only-binary=:all: --python-version=3.11 --platform=manylinux2014_x86_64
