import os
import re


def inject_pipeline_into_template(template_file, final_document):
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


# Specify the template and final document file names
template_with_placeholders = "prompt_template.md"
final_markdown_document = "final_document.md"

# Run the pipeline injection
inject_pipeline_into_template(template_with_placeholders, final_markdown_document)

print(f"The final document has been written to {final_markdown_document}")
