import os
import shutil
from markdown import markdown
from jinja2 import Environment, FileSystemLoader
import yaml

# Load configuration from config.yaml
def load_config():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    return config

# Function to extract metadata from YAML front matter
def extract_metadata(content_path):
    # read the parts between --- and ---
    with open(content_path, "r") as f:
        content = f.read()
        start_index = content.find("---")
        end_index = content.find("---", start_index + 3)
        if end_index == -1:
            return {}
        metadata_str = content[start_index + 3 : end_index]
        # parse the YAML front matter
        metadata = yaml.safe_load(metadata_str)
    return metadata


# Function to copy assets while preserving directory structure
def copy_assets(source_dir, destination_dir):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".md"):
                continue
            if file.endswith(".html"):
                continue
            source_path = os.path.join(root, file)
            relative_path = os.path.relpath(source_path, source_dir)
            destination_path = os.path.join(destination_dir, relative_path)
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            shutil.copyfile(source_path, destination_path)


# Define content and template root directories
config = load_config()

content_dir = config["directories"]["content"]
template_dir = config["directories"]["templates"]
output_dir = config["directories"]["output"]
default_template = config["default_template"]

# Load templates
env = Environment(loader=FileSystemLoader(template_dir))


def generate_html(content_path):
    # Extract metadata
    metadata = extract_metadata(content_path)

    # Read markdown content
    with open(content_path, "r") as f:
        # skip the frontmatter
        content = f.read()
        start_index = content.find("---")
        end_index = content.find("---", start_index + 3)
        if end_index == -1:
            markdown_content = content
        else:
            markdown_content = content[end_index + 3 :]

    # Convert markdown to HTML
    html_content = markdown(markdown_content)

    # Combine config, metadata and content for template rendering
    data = {**config, **metadata, "content": html_content}

    # Use extracted data directly in template rendering
    # get template from metadata if exists otherwise use default template "base.html"
    rendered_content = env.get_template(metadata.get("template")  or default_template).render(**data)

    # Derive output path and create directory structure
    output_path = os.path.join(
        output_dir, os.path.relpath(content_path, content_dir).replace(".md", ".html")
    )
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Write rendered content to output file
    with open(output_path, "w") as f:
        f.write(rendered_content)


# Process each content file
for root, _, files in os.walk(content_dir):
    for filename in files:
        if filename.endswith(".md"):
            content_path = os.path.join(root, filename)
            generate_html(content_path)

# Copy assets from content directory to build directory
copy_assets(content_dir, output_dir)
# Copy assets from template directory to build directory
copy_assets(template_dir, output_dir)

print(f"Static site generated successfully! Output in {output_dir}")
