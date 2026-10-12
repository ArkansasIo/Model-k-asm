#!/bin/sh
set -eu
make clean
make
make test
