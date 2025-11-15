#!/usr/bin/env python3
import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

# Read the markdown file
with open('AI_Virtual_Assistant_Presentation.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Convert markdown to HTML
html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite', 'tables'])

# Create a styled HTML document
styled_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        @page {{
            size: A4;
            margin: 2cm;
            @bottom-right {{
                content: counter(page);
            }}
        }}
        body {{
            font-family: 'Arial', 'Helvetica', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 100%;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-top: 30px;
            font-size: 28px;
            page-break-before: always;
        }}
        h1:first-of-type {{
            page-break-before: avoid;
        }}
        h2 {{
            color: #34495e;
            border-bottom: 2px solid #95a5a6;
            padding-bottom: 8px;
            margin-top: 25px;
            font-size: 22px;
        }}
        h3 {{
            color: #2980b9;
            margin-top: 20px;
            font-size: 18px;
        }}
        h4 {{
            color: #16a085;
            margin-top: 15px;
            font-size: 16px;
        }}
        p {{
            margin: 10px 0;
            text-align: justify;
        }}
        ul, ol {{
            margin: 10px 0;
            padding-left: 30px;
        }}
        li {{
            margin: 5px 0;
        }}
        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 90%;
        }}
        pre {{
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 15px;
            overflow-x: auto;
            page-break-inside: avoid;
        }}
        pre code {{
            background-color: transparent;
            padding: 0;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 15px 0;
            page-break-inside: avoid;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }}
        th {{
            background-color: #3498db;
            color: white;
            font-weight: bold;
        }}
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 15px;
            margin: 15px 0;
            color: #555;
            font-style: italic;
        }}
        hr {{
            border: none;
            border-top: 2px solid #ecf0f1;
            margin: 30px 0;
        }}
        .page-break {{
            page-break-after: always;
        }}
        strong {{
            color: #2c3e50;
        }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
"""

# Configure fonts
font_config = FontConfiguration()

# Convert HTML to PDF
HTML(string=styled_html).write_pdf(
    'AI_Virtual_Assistant_Presentation.pdf',
    font_config=font_config
)

print("✅ PDF created successfully: AI_Virtual_Assistant_Presentation.pdf")
