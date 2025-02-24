import os
import textwrap
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import lorem
import time
import click

def write_content_to_pdf_canvas(content, c):
    width, height = letter
    left_margin = 50
    right_margin = 50
    top_margin = height - 50
    bottom_margin = 50
    line_height = 16
    paragraph_spacing = 10
    max_width = width - (left_margin + right_margin)
    y_position = top_margin

    for paragraph in content.split("\n"):
        for line in textwrap.wrap(paragraph, width=90):  
            c.drawString(left_margin, y_position, line)
            y_position -= line_height  

            if y_position < bottom_margin:
                c.showPage()
                y_position = top_margin  

        y_position -= paragraph_spacing  

    c.showPage()


def make_pdf(output_dir, content, pages, file_name):
    try:
        os.makedirs(output_dir, exist_ok=True)
        file_name = f'auto_generated_pdf_{int(time.time())}.pdf' if not file_name else f'{file_name}.pdf'
        if(file_name[-4:] != '.pdf'):
            raise Exception('Invalid file name provided')

        file_path = os.path.join(output_dir, file_name)
        c = canvas.Canvas(file_path, pagesize=letter)
        if(content):
            write_content_to_pdf_canvas(content, c)
                
        else:
            content = lorem.text()
            if(not pages):
                pages = 1
            for i in range(pages):
                write_content_to_pdf_canvas(content, c)

        c.save()
        click.echo(f"PDF successfully created: {file_path}")
    except PermissionError:
        click.echo("Error: Permission denied for the specified output directory.")
    except Exception as ex:
        click.echo(f"An unexpected error occurred: {ex}")

