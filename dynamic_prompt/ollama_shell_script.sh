#!/bin/bash

MODEL=${1:-"llama3.2:latest"}
paste="$(pbpaste)"

if [ -z "$paste" ]; then
    echo "Error: Clipboard is empty" >&2
    exit 1
fi

if ! copy=$(/usr/local/bin/ollama run "$MODEL" "$paste" 2>/dev/null); then
    echo "Error: Failed to run ollama" >&2
    exit 1
fi

echo "$copy" | pbcopy