#!/bin/bash

DURATION=60
BAR_LENGTH=40

echo "Starting execution of suspicious files..."

for ((i=0; i<=DURATION; i++)); do
    percent=$(( i * 100 / DURATION ))
    blocks=$(( i * BAR_LENGTH / DURATION ))

    bar=""
    for ((j=0; j<blocks; j++)); do
        bar="${bar}#"
    done
    for ((j=blocks; j<BAR_LENGTH; j++)); do
        bar="${bar}-"
    done

    printf "\\r[%s] %d%%" "$bar" "$percent"
    sleep 1
done

echo -e "\\n\\nWARNING: Clicking on unknown files or links can compromise your system security!"
echo "Always verify file sources before executing anything suspicious."
