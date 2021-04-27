#!/bin/sh

WORKING_DIR=`pwd`
TEMP_DIR=`mktemp -d`

cd $TEMP_DIR

python3 $(dirname "$0")/rl.py

for file in *.png
do
	convert $file ${file%.png}.pdf
done

pdfunite *.pdf $WORKING_DIR/rl.pdf

cd $ORIGINAL_DIR

rm -r $TEMP_DIR