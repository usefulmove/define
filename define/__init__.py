#!/usr/bin/env python

import requests
from rich.console import Console
from rich.markup import escape
import sys


URI_BASE = "https://api.dictionaryapi.dev/api/v2/entries/en/"
console = Console()


def main():
    if len(sys.argv) < 2:
        console.print("[red]error[/]: no word argument provided")
        sys.exit(1)

    uri = URI_BASE + " ".join(sys.argv[1:])

    try:
        response = requests.get(uri, timeout=10)
    except requests.RequestException:
        console.print("[red]error[/]: could not reach dictionary API")
        sys.exit(1)

    if response.status_code != 200:
        console.print("[red]error[/]: word not found")
        sys.exit(1)

    for idx, entry in enumerate(response.json()):
        data = entry

        word = data["word"]
        meanings = data["meanings"]

        console.print(f"\n[#87ffaf bold]{word}[/] [#666666][{idx+1}][/]")

        for meaning in meanings:
            part_of_speech = meaning["partOfSpeech"]
            definitions = meaning["definitions"]

            console.print(f"  [#fffc67]{part_of_speech}:[/]")

            for n, definition in enumerate(definitions, 1):
                console.print(f"    [#0080ff bold]{n}[/]. {escape(definition['definition'])}")

    console.print()


if __name__ == "__main__":
    main()
