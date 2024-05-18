from typing import List, Tuple


def dump_migrations_as_grit(name: str, migration_pairs: List[Tuple[str, str]]):
    """Dump the migration pairs as a Grit file."""
    return "\n".join([f"{from_module} -> {to_module}" for from_module, to_module in migration_pairs])