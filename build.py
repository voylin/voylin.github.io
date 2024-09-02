import os
import json
import re
import shutil


PAGES_DIR = "pages"
DOCS_DIR = "docs"
TYPES_DIR = "types"
BLOCKS_DIR = "blocks"
DATA_FILE = "data.json"


with open(DATA_FILE, 'r') as f:
    data = json.load(f)


def build_page(template, content, metadata):
    template = template.replace("{{ CONTENT }}", content)

    block_pattern = re.compile(r"\{\{ BLOCK_([A-Z0-9_-]+) \}\}")
    for match in block_pattern.findall(template):
        block_path = os.path.join(BLOCKS_DIR, match.lower() + ".html")
        if os.path.exists(block_path):
            with open(block_path, 'r') as block_file:
                block_content = block_file.read()
            template = template.replace(f"{{{{ BLOCK_{match} }}}}", block_content)

    data_pattern = re.compile(r"\{\{ DATA_([A-Z0-9_-]+) \}\}")
    for match in data_pattern.findall(template):
        key = match.lower()
        if key in data:
            template = template.replace(f"{{{{ DATA_{match} }}}}", data[key])

    for key, value in metadata.items():
        template = template.replace(f"{{{{ {key.upper()} }}}}", value)

    return template


for root, dirs, files in os.walk(PAGES_DIR):
    for file in files:
        if file.endswith(".html"):
            page_path = os.path.join(root, file)
            with open(page_path, 'r') as page_file:
                content = page_file.read()

            meta_data, html_content = content.split('===', 1)

            metadata = {}
            for line in meta_data.strip().splitlines():
                key, value = line.split(":", 1)
                metadata[key.strip().lower()] = value.strip()

            relative_path = os.path.relpath(page_path, PAGES_DIR)
            output_path = os.path.join(DOCS_DIR, relative_path)
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            template_path = os.path.join(TYPES_DIR, f"{metadata['type']}.html")
            if os.path.exists(template_path):
                with open(template_path, 'r') as template_file:
                    template_content = template_file.read()

                final_content = build_page(template_content, html_content, metadata)

                if re.search(r"\{\{.*?\}\}", final_content):
                    print(f"Warning: Unresolved placeholders found in {output_path}")

                with open(output_path, 'w') as output_file:
                    output_file.write(final_content)
                print(f"Generated: {output_path}")
            else:
                print(f"Error: Template for type '{metadata['type']}' not found in {template_path}")

# Copy assets
shutil.copytree(src="assets/", dst="docs/assets", dirs_exist_ok=True)
