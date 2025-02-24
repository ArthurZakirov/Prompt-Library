#!/bin/bash

# arguments
# MODEL=${1:-"llama3.2:latest"}
# PROMPT_TEMPLATE_FILE=${2:-"prompt_template.md"}

MODEL="llama3.2:latest"
PROMPT_TEMPLATE_FILE="prompt_template.md"

CLIPBOARD_FILE="clipboard_content.txt"
FINAL_PROMPT_FILE="final_prompt.txt"
LLM_OUTPUT_FILE="llm_output.txt"

# get clipboard content
paste="$(pbpaste)"
if [ -z "$paste" ]; then
    echo "Error: Clipboard is empty" >&2
    exit 1
fi

# store clipboard content into a temporary file
echo "$paste" > "$CLIPBOARD_FILE"

# Run dynamic prompt building script
python3 dynamic_prompt_building.py --template "$PROMPT_TEMPLATE_FILE" --output "$FINAL_PROMPT_FILE"

final_prompt=$(cat "$FINAL_PROMPT_FILE")
# echo "Final prompt:"
# echo "------------------------------------------------------------------"
# echo "$final_prompt"
# echo "------------------------------------------------------------------"


# echo "Running Ollama..."
if ! llm_output=$(/usr/local/bin/ollama run "$MODEL" "$final_prompt" 2>/dev/null); then
    echo "Error: Failed to run ollama" >&2
    exit 1
fi
# echo "------------------------------------------------------------------"
# echo "$llm_output" 
# echo "------------------------------------------------------------------"
echo "$llm_output" > "$LLM_OUTPUT_FILE"
echo "$llm_output" | pbcopy