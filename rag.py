from typing import Any, Dict, Type, List
import lancedb
from lancedb.pydantic import LanceModel
from lancedb import DBConnection


class LanceDBHandler:
    def __init__(self, db_path: str = "/tmp/db") -> None:
        self.db = lancedb.connect(db_path)

    def create_table_with_schema(
        self, table_name: str, schema: Type[LanceModel], mode: str = "overwrite"
    ):
        return Table(self.db, table_name, schema, mode)


class Table:
    def __init__(
        self,
        db: Type[DBConnection],
        table_name: str,
        schema: Type[LanceModel],
        mode: str,
    ) -> None:
        self.db = db
        self.schema = schema
        self.table = self.db.create_table(table_name, schema=schema, mode=mode)

    def add(self, data: List[Dict[str, Any]]) -> None:
        self.table.add(data)

    def search(self, query: str, limit: int = 1):
        return self.table.search(query).limit(limit).to_pydantic(self.schema)
