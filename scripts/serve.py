#!/usr/bin/env python

"""Serve the _site directory locally and open a browser."""

import os
import http.server
import threading
import webbrowser
from pathlib import Path

SITE_DIR = Path(__file__).resolve().parent.parent / "_site"
PORT = 8000


def main() -> None:
    if not SITE_DIR.exists():
        raise SystemExit(f"Error: {SITE_DIR} does not exist. Run 'rsconstruct build' first.")

    handler = http.server.SimpleHTTPRequestHandler
    server = http.server.HTTPServer(("localhost", PORT), handler)
    print(f"Serving {SITE_DIR} at http://localhost:{PORT}")
    print("Press Ctrl+C to stop.")

    os.chdir(SITE_DIR)

    threading.Timer(0.5, lambda: webbrowser.open(f"http://localhost:{PORT}")).start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
        server.server_close()


if __name__ == "__main__":
    main()
