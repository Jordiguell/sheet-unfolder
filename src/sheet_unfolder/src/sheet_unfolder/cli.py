import typer
from pathlib import Path
from .pipeline import process_plan

app = typer.Typer(help="Sheet-Unfolder CLI")

@app.command()
def unfold(pdf: Path, output: Path = Path("output")):
    """Unfold a PDF plan and write DXF grouped by thickness."""
    output.mkdir(parents=True, exist_ok=True)
    process_plan(pdf, output)
    typer.echo(f"Done! Check {output}")

if __name__ == "__main__":
    app()
