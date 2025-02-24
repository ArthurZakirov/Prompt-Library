# Default values
MODEL="llama3.2:latest"
PROMPT_TEMPLATE_FILE="prompt_template.md"

# Parse options with getopt
OPTS=$(getopt -o m:p: --long model:,prompt-template-file: -- "$@")

if [ $? != 0 ]; then
    echo "Failed to parse options... exiting."
    exit 1
fi

eval set -- "$OPTS"

while true; do
    case "$1" in
        -m | --model )
            MODEL="$2"
            shift 2
            ;;
        -p | --prompt-template-file )
            PROMPT_TEMPLATE_FILE="$2"
            shift 2
            ;;
        -- )
            shift
            break
            ;;
        * )
            echo "Invalid option: $1"
            exit 1
            ;;
    esac
done

# Now you can use the variables MODEL and PROMPT_TEMPLATE_FILE in your 
script
echo "Using model: $MODEL"
echo "Using prompt template file: $PROMPT_TEMPLATE_FILE"