import click
from pathlib import Path

LUA = '''-- I use dap-python as I don't want to manually set `adapters.python`.
local dap_python = require('dap-python')

dap_python.setup(os.getenv('PYTHON_INTERPRETER_PATH'))

require('dap').configurations.python = {
    {
        type = 'python',
        request = 'launch',
        name = "Run current file",
        program = '${file}',
        justMyCode = false,
    },
    {
        type = 'python',
        request = 'launch',
        name = 'pytest run current file',
        module = 'pytest',
        args = {'${file}', '--log-cli-level=DEBUG'},
        justMyCode = false,
    },
    {
        type = 'python',
        request = 'launch',
        name = 'pytest run current file on many cores',
        module = 'pytest',
        args = {'-n', 'auto', '${file}', '--log-cli-level=DEBUG'},
        justMyCode = false,
    },
    {
        type = 'python',
        request = 'launch',
        name = 'pytest run all unit tests',
        module = 'pytest',
        args = {'tests/test_unit/', '--log-cli-level=DEBUG'},
        justMyCode = false,
    },
    {
        type = 'python',
        request = 'launch',
        name = 'pytest run godm unit tests',
        module = 'pytest',
        args = {'tests/test_unit/test_godm/', '--log-cli-level=DEBUG'},
        justMyCode = false,
    },
    {
        type = 'python',
        request = 'launch',
        name = 'Run current file with arguments',
        program = '${file}',
        args = {'--arg1', 'value1', '--arg2', 'value2'},
    },
}
'''


@click.command()
@click.option('--output', '-o', default='dap_config.lua', type=click.Path(), help='Output file path')
@click.option('--force', '-f', is_flag=True, help='Overwrite existing file if present')
def generate_dap_config(output, force):
    """Generate a dap_config.lua file with recommended Python dap configurations."""
    out = Path(output)
    if out.exists() and not force:
        click.echo(f"{out} already exists. Use --force to overwrite.")
        raise click.Abort()
    out.write_text(LUA)
    click.echo(f"Wrote dap config to: {out}")


if __name__ == '__main__':
    generate_dap_config()
