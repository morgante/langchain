"""
Migrate LangChain to the most recent version with GritQL.
"""

import re
import shutil
import subprocess
from pathlib import Path
from typing import Optional

import typer
from typing_extensions import Annotated
from typer import Argument, Exit, Option, Typer

from gritql import run


migrate_cli = Typer(invoke_without_command=True, add_completion=False)

@migrate_cli.callback(
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
)
def run_migrate(
    diff: bool = Option(False, help="Show diff instead of applying changes."),
    # unknown_args: typer.Context = typer.Option(None)
):
    args = []
    if diff:
        args.append("--dry-run")
    final_code = run.apply_pattern(
        get_codemod_path(),
        args
    )

    raise typer.Exit(code=final_code)

def get_codemod_path():
    script_dir = Path(__file__).parent
    return script_dir / "migrations" / "sample.grit"
