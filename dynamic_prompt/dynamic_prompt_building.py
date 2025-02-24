import os
import re
import argparse


def inject_pipeline_into_template(template_file, final_document):
    """
    Injects content from pipeline files into a template document by replacing placeholders.

    This function reads a template file containing placeholders in the format {{inject:filename}},
    replaces each placeholder with the content of the corresponding pipeline file, and writes
    the result to a final document.

    Args:
        template_file (str): Path to the template file containing placeholders.
        final_document (str): Path where the final document with replaced content will be saved.

    Example:
        If template.txt contains:
        "Here is pipeline content: {{inject:pipeline1.txt}}"
        And pipeline1.txt contains "Hello World"
        Then the final document will contain:
        "Here is pipeline content: Hello World"

    Note:
        - Placeholders should be in the format {{inject:filename}}
        - If a referenced pipeline file is not found, an error message will be inserted
    """
    # Read the template file containing placeholders
    with open(template_file, "r") as template:
        template_content = template.read()

    # Function to replace placeholders with corresponding pipeline file content
    def replace_placeholder(match):
        pipeline_file_name = match.group(
            1
        ).strip()  # Extract file name from placeholder
        if os.path.exists(pipeline_file_name):
            with open(pipeline_file_name, "r") as pipeline_file:
                return pipeline_file.read()  # Insert the content of the pipeline file
        else:
            return f"[Error: Pipeline file '{pipeline_file_name}' not found]"

    # Replace all placeholders in the format {{inject:filename}}
    filled_template = re.sub(r"{{inject:(.+?)}}", replace_placeholder, template_content)

    # Write the final document with replaced placeholders
    with open(final_document, "w") as final_output:
        final_output.write(filled_template)


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Inject pipeline content into template file.')
    parser.add_argument('template', help='Path to the template file containing placeholders')
    parser.add_argument('output', help='Path where the final document will be saved')
    
    # Parse arguments
    args = parser.parse_args()

    # Run the pipeline injection with command line arguments
    inject_pipeline_into_template(args.template, args.output)
    print(f"The final document has been written to {args.output}")

if __name__ == "__main__":
    main()
