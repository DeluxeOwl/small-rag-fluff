#!/usr/bin/env python3
import os
import sys
from rag import LanceDBHandler
from paragraph import Paragraph

if "OPENAI_API_KEY" not in os.environ:
    sys.exit("Missing OPENAI_API_KEY environment variable")

handler = LanceDBHandler()
paragraphs = handler.create_table_with_schema(table_name="paragraphs", schema=Paragraph)

paragraphs.add([{"text": "hello, world"}, {"text": "goodbye, world"}])

try:
    print(paragraphs.search("greeting")[0].text)
except IndexError:
    print("No results found")
