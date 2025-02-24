import os
from pathlib import Path
import fitz 
import time
import re 
import click
import csv

def highlight_text(pdf_path, target_text, page_number, exact, output_path):
    try:
        if not os.path.exists(pdf_path):
            raise FileNotFoundError()
        
        doc = fitz.open(pdf_path)
        if page_number and (page_number < 1 or page_number > len(doc)):
            raise ValueError("Invalid page number")
        pages_to_search = [doc[page_number - 1]] if page_number else doc
        word_pattern = rf"\b{re.escape(target_text)}\b" if exact else re.escape(target_text)
        for page in pages_to_search:
            text_instances = []
            text = page.get_text("text")
            
            for match in re.finditer(word_pattern, text, re.IGNORECASE):
                start, end = match.span()
                rects = page.search_for(text[start:end])
                text_instances.extend(rects)

            for inst in text_instances:
                highlight = page.add_highlight_annot(inst)
                highlight.update() 

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        doc.save(output_path)
        doc.close()

    except FileNotFoundError:
        click.echo('File not found in the specified location')
    except PermissionError:
        click.echo('The directory to be operated upon is not permissible.')
    except ValueError:
        click.echo(f'Invalid page number for pdf {pdf_path}')
    except Exception as e:
        click.echo(f"Error processing PDF")


def highlight_pdf(csv_path, output_path):
    try:
        dir_path = Path(output_path)
        data_dict = []
        with open(csv_path, "r", newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file) 
            for row in reader:
                data_dict.append(dict(row)) 
        for data in data_dict:
            file_path = data['file']
            word = data['word']
            exact = data['exact']
            page = data['page']
            page = page.replace(' ', '')
            exact = exact.replace(' ', '')
            page = int(page) if page else 1
            exact = str(exact).lower() in ('true', '1', 'yes')
            file_name = str(int(time.time())) + '_' +  os.path.basename(file_path)
            output_file = os.path.normpath(os.path.join(dir_path, file_name))
            highlight_text(file_path, word, page, exact, output_file)
        click.echo('operation successful')
    except Exception as ex:
        click.echo(f'Error processing pdf')
