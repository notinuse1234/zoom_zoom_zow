#!/usr/bin/env bash

# Build and package the application for delivery

DIR=$(dirname $0)
NAME='ZoOm zOoM zOw'
OUT='zoom_zoom_zow.sh'

while true; do
    read -p "Compile $NAME? (y/n) " SURE
    case $SURE in
        y|Y|yes|YES)
            break;;
        n|N|no|No|NO)
            exit;;
        *)
            echo;;
    esac
done

# Compile the python application into a linux binary
pyinstaller --onefile --windowed $DIR/run.spec

# Initialise $OUT wrapper file
egrep "^####SKELETON####" -A $(wc -l $0 | cut -d' ' -f1) $0\
    | grep -v "####SKELETON####"\
    | base64 -d > $DIR/$OUT

# Add compiled binary to the wrapper script
echo "####BEGINB64####" >> $DIR/$OUT
base64 $DIR/dist/run >> $DIR/$OUT

# Make the script executable
chmod +x $DIR/$OUT
echo
echo "$NAME script generated."
echo "Located at ./$OUT"
exit

####SKELETON####
IyEvdXNyL2Jpbi9lbnYgYmFzaApESVI9JChkaXJuYW1lICQwKQppZiBbWyAhIC1kICRESVIvcnVu
X3RtcCBdXTsgdGhlbgogICAgbWtkaXIgJERJUi9ydW5fdG1wCmZpCmV4cG9ydCBUTVBESVI9JERJ
Ui9ydW5fdG1wCmVjaG8gJFRNUERJUgp1bnBhY2tfZXhlYygpIHsKICAgIGVncmVwICJeIyMjI0JF
R0lOQjY0IyMjIyIgLUEgJCh3YyAtbCAkMCB8IGN1dCAtZCcgJyAtZjEpICQwIHwgZ3JlcCAtdiAi
IyMjI0JFR0lOQjY0IyMjIyIgfCBiYXNlNjQgLWQgLSA+ICRUTVBESVIvcnVuX3NjcmlwdAogICAg
Y2htb2QgK3ggJFRNUERJUi9ydW5fc2NyaXB0Cn0KdW5wYWNrX2V4ZWMKZWNobyAiU3RhcnRpbmcu
Li4iCiRUTVBESVIvcnVuX3NjcmlwdCAkQApybSAkVE1QRElSL3J1bl9zY3JpcHQKcm0gLXIgJFRN
UERJUgpleGl0Cg==
