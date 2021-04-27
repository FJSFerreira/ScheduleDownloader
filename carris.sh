#!/bin/sh

WORKING_DIR=`pwd`
TEMP_DIR=`mktemp -d`

cd $TEMP_DIR

python3 $(dirname "$0")/carris.py

pdfunite *.pdf $WORKING_DIR/carris.pdf

cd $ORIGINAL_DIR

rm -r $TEMP_DIR