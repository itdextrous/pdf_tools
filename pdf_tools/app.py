import click
from pdf_tools.hipdf import highlight_pdf
from pdf_tools.mkpdf import make_pdf


@click.group()
def cli():
    """PDF Tools Command Line Interface"""
    pass

@cli.command()
@click.argument('csv_path')
@click.argument('output_path')
def highlight(csv_path, output_path):
    """Process a PDF file"""
    click.echo(f"Processing PDF: {csv_path}")
    highlight_pdf(csv_path, output_path)


@cli.command()
@click.argument('output_dir')
@click.option('--content', help="Optional content")
@click.option('--pages', type=int, help='Pages in output. If content is also specified, it wil get priority')
@click.option('--name', help = "Name for your pdf file")
def generate(output_dir, content, pages, name):
    click.echo('generating pdfs')
    pages = int(pages) if pages else None
    make_pdf(output_dir, content, pages, name)


if __name__ == "__main__":
    cli()