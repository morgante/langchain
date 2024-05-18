from typing import List, Tuple

def split_package(package: str) -> Tuple[str, str]:
    """Split a package name into the containing package and the final name"""
    parts = package.split(".")
    return ".".join(parts[:-1]), parts[-1]

def dump_migrations_as_grit(name: str, migration_pairs: List[Tuple[str, str]]):
    """Dump the migration pairs as a Grit file."""
    output = "language python"
    remapped = ",\n".join([
        f"    [`{split_package(from_module)[0]}`, `{split_package(from_module)[1]}`, `{split_package(to_module)[0]}`, `{split_package(to_module)[1]}`]"
        for from_module, to_module in migration_pairs
    ])
    output = f"""
language python

pattern {name}() {{
  find_replace_imports(list=[
{remapped}
  ])
}}

# Add this for invoking directly
{name}()
"""
    return output