!/bin/bash
declare title="$1"
#awk ' {print ($(NF - 3) ) }' |
#sort -k2 -g $title 

awk ' { print substr( $(NF -3), 2), $0}' $title | sort -g  | cut -d' ' -f2- > matt
mv matt $title

