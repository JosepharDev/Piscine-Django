#!/bin/sh

if [ $# -gt 1 ]; then
    echo "bad formate\nusage ./myawesomescript.sh  url"
elif [ $# -eq 1 ]; then
    curl -L  -s -o /dev/null -w "%{url_effective}" "$1"
else
    echo "expect the url"
fi