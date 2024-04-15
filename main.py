#!/usr/bin/env python3
import os
import sys
from rag import LanceDBHandler
from paragraph import Paragraph

from fastapi import FastAPI
from pydantic import BaseModel

if "OPENAI_API_KEY" not in os.environ:
    sys.exit("Missing OPENAI_API_KEY environment variable")

handler = LanceDBHandler()
paragraphs = handler.create_table_with_schema(table_name="paragraphs", schema=Paragraph)

app = FastAPI()


class ParagraphBody(BaseModel):
    text: str


@app.post("/paragraphs")
async def create_paragraph(paragraph: ParagraphBody):
    paragraph_as_dict = paragraph.model_dump()

    try:
        paragraphs.add([paragraph_as_dict])
    except Exception as e:
        return {"result": []}

    return {"result": [paragraph.text]}


class QueryBody(BaseModel):
    query: str


@app.post("/query")
async def query_db(query: QueryBody):
    print("Got query", query)

    try:
        result = paragraphs.search(query=query.query, limit=1)[0]
    except Exception as e:
        return {"result": []}

    return {"result": [result.text]}
