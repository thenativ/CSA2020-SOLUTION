#!/bin/bash

offset=0
frame_count=455846
img_size=675 # SQUARE ROOT OF 455846 FLOORED

rm result.bmp
rm tmp.bmp
touch result.bmp # Result picture
touch tmp.bmp # Temporary image to store rows

i=$offset
while [ $i -lt $frame_count ]
do
	convert +append tmp.bmp "frames/$i.bmp"
	if [ $(($i % $image_size)) -eq 0 ]
	then
		convert -append result.bmp tmp.bmp
		rm tmp.bmp
		touch tmp.bmp
	fi
	$i=$i+1
done
