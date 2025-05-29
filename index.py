from src.notion_pdf_exporter import NotionExporter
from notion import Client

import os

notion_client = Client(token=os.getenv("NOTION_API_KEY"))

notion_exporter = NotionExporter(notion_client)

notion_exporter.export_page(filter="Test")