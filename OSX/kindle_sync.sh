#! /bin/bash
if [ -d /Volumes/Kindle/documents ]
then
    /bin/date >> /tmp/kindle_date
    cp /Volumes/Kindle/documents/My\ Clippings.txt /tmp
fi

