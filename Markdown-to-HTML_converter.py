import markdown2

def load_markdown(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def transform_to_html(markdown_data):
    return markdown2.markdown(markdown_data)

def create_html_page(content):
    html_structure = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Converted Markdown</title>
        <style>
            body {{
                font-family: 'Helvetica', sans-serif;
                line-height: 1.5;
                margin: 30px;
                background-color: #f4f4f4;
            }}
            h1, h2, h3 {{
                color: #2e3b4e;
            }}
            a {{
                color: #0275d8;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        {content}
    </body>
    </html>
    """
    return html_structure

def save_html(html_data, path_to_save):
    with open(path_to_save, "w", encoding="utf-8") as file:
        file.write(html_data)

def run_converter():
    print("Welcome to the Markdown to HTML Converter!")
    input_markdown = input("Enter the path to your Markdown file: ")
    output_html = input("Enter the desired output path for the HTML file: ")

    try:
        markdown_content = load_markdown(input_markdown)
        html_body = transform_to_html(markdown_content)
        complete_html = create_html_page(html_body)
        save_html(complete_html, output_html)
        print(f"Your HTML file has been successfully saved at {output_html}")
    except Exception as error:
        print(f"Error occurred: {error}")

if __name__ == "__main__":
    run_converter()
