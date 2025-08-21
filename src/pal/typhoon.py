#evaluate in file 
import os
from typhoon_ocr import ocr_document

base_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(base_dir, "..", "..", "data", "Data Foundation List.pdf")
pdf_path = os.path.abspath(pdf_path)  

print("Using PDF:", pdf_path)
print("PDF exists:", os.path.exists(pdf_path))

print("🚀 Start Processing with Typhoon OCR...")
markdown = ocr_document(
    pdf_path,
    base_url="http://localhost:11434/v1",
    api_key="ollama",
    model="scb10x/typhoon-ocr-7b:latest",
    page_num=1
)
output_file = os.path.join(base_dir, "nectec1.md")
with open(output_file, "w", encoding="utf-8") as f:
    f.write(markdown)

print("✅ Processing complete!")
print(f"📄 OCR result saved to {output_file}")

