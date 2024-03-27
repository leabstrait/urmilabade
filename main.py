import os
import shutil
from jinja2 import Environment, FileSystemLoader


def render_template(template_name, output_dir, context):
    # Load the template
    template = env.get_template(os.path.basename(template_name))

    # Render the template with context data
    rendered_output = template.render(context)

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Write the rendered output to a file in the output directory
    output_file = os.path.join(
        output_dir, os.path.basename(template_name).replace(".j2", ".html")
    )
    with open(output_file, "w") as f:
        f.write(rendered_output)

    print(f"Template rendered successfully. Output saved to: {output_file}")


def clear_output_dir(output_dir, skip=None):
    # Clear the output directory
    for filename in os.listdir(output_dir):
        if skip and filename in skip:
            continue
        file_path = os.path.join(output_dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print("Failed to delete %s. Reason: %s" % (file_path, e))
    print(f"Output directory cleared successfully.")
    return output_dir


def copy_assets(source_dir, dest_dir):
    # Ensure the destination directory exists
    os.makedirs(os.path.join(dest_dir, source_dir), exist_ok=True)

    # Copy all files and directories from source directory to destination directory
    shutil.copytree(source_dir, os.path.join(dest_dir, source_dir), dirs_exist_ok=True)

    print(f"Assets copied from {source_dir} to {dest_dir}")


if __name__ == "__main__":
    # Define the templates directory
    templates_dir = "templates"
    env = Environment(loader=FileSystemLoader(templates_dir))

    # Define the output directory
    output_dir = "docs"  # Update with your desired output directory

    # Define the source directory for styles
    styles_dir = "styles"  # Update with the directory containing your styles

    # Define the source directory for scripts
    scripts_dir = "scripts"  # Update with the directory containing your scripts

    # Define the source directory for portfolio
    portfolio_dir = "portfolio"  # Update with the directory containing your portfolio

    # Define the source directory for media
    media_dir = "media"  # Update with the directory containing your media files

    # Define the source directory for pdfs
    pdfs_dir = "pdfs"  # Update with the directory containing your pdfs files

    # Clear output directory
    clear_output_dir(output_dir, skip=["CNAME"])

    import index

    template_name = index.config["template"]
    context = {
        **index.config,
        "page": "index",
    }
    # Render the template
    render_template(template_name, output_dir, context)

    import about

    template_name = about.config["template"]
    context = {
        **about.config,
        "page": "about",
    }
    # Render the template
    render_template(template_name, output_dir, context)

    # Copy assets
    copy_assets(styles_dir, output_dir)
    copy_assets(portfolio_dir, output_dir)
    copy_assets(scripts_dir, output_dir)
    copy_assets(media_dir, output_dir)
    copy_assets(pdfs_dir, output_dir)

    print("All templates rendered successfully.")
    print(f"Output saved to: {output_dir}")
