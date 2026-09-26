"""`lens-serve` launcher (stub).

The Lens — serve: exposes the verified library for query, a read API plus an MCP
interface so people and agents can ask it questions. Read-only over verified.
Stdlib-only so `lens-serve --help` works the moment pip install completes. The
database is INJECTED via LENS_DB_URL — never hardcoded.

This is a scaffold: it validates inputs and prints the plan. The real read API +
MCP interface land in follow-up commits.
"""
from __future__ import annotations

import argparse
import os
import sys


def _cmd_serve(args: argparse.Namespace) -> int:
    db = args.db_url or os.environ.get("LENS_DB_URL")
    if not db:
        print("error: no database. Set LENS_DB_URL or pass --db-url "
              "(the connection is injected, never hardcoded).", file=sys.stderr)
        return 1
    print("==> lens-serve: serving the verified library (read-only)")
    print(f"    database:  {db.split('@')[-1] if '@' in db else '(set)'}")
    print()
    print("STUB: read API + MCP interface not implemented yet.")
    print("      Next commit exposes verified via a read API + MCP (read-only).")
    return 0


def _cmd_version(_args: argparse.Namespace) -> int:
    from lens_serve import __version__
    print(f"lens-serve {__version__}")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="lens-serve", description="The Lens — serve: query the verified library via API + MCP.")
    subs = p.add_subparsers(dest="command", metavar="<command>")

    srv = subs.add_parser("serve", help="Serve the verified library for query (API + MCP, read-only).")
    srv.add_argument("--db-url", default=None, help="Database URL (default: LENS_DB_URL env).")
    srv.set_defaults(func=_cmd_serve)

    subs.add_parser("version", help="Print version.").set_defaults(func=_cmd_version)

    args = p.parse_args(argv)
    if not getattr(args, "func", None):
        p.print_help()
        return 0
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
