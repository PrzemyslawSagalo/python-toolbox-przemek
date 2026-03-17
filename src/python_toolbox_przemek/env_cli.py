import click
from pathlib import Path
import sys
import python_toolbox_przemek

@click.command()
@click.option('--output', '-o', default='.env', type=click.Path(), help='Output file path')
@click.option('--force', '-f', is_flag=True, help='Overwrite existing file if present')
def generate_env(output, force):
    """Generate a .env file for Neovim DAP."""
    out = Path(output)
    if out.exists() and not force:
        click.echo(f"{out} already exists. Use --force to overwrite.")
        raise click.Abort()

    pandas_config = Path(python_toolbox_przemek.__file__).parent / "pandas_config.py"
    
    # Try to find venv python
    # sys.executable is the venv python if running from a venv
    interpreter = sys.executable
    
    content = [
        f'PYTHONSTARTUP="{pandas_config.absolute()}"',
        f'PYTHON_INTERPRETER_PATH="{interpreter}"',
        'PYTHONPATH=""',
    ]
    
    out.write_text("\n".join(content) + "\n")
    click.echo(f"Wrote env config to: {out}")

if __name__ == '__main__':
    generate_env()
