import tempfile
import os
from llama_index.core.tools import FunctionTool
import aspose.words as aw


def generate_report(md_text, output_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".md") as temp_md:
        temp_md.write(md_text.encode('utf-8'))
        temp_md_path = temp_md.name
    pdf_file = "Azure-Function-Report.pdf"
    try:
        doc = aw.Document(temp_md_path)
        doc.save(pdf_file)

        return "Success"

    finally:
        os.remove(temp_md_path)


report_generator = FunctionTool.from_defaults(
    fn=generate_report,
    name="report_generator",
    description="This tool can generate PDF report from markdown text"
)
