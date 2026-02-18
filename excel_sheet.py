import os
import json
import pandas as pd
from io import StringIO
from paddleocr import PaddleOCRVL

IMAGE_PATH = r"path_to\your_image.png"

image_dir   = os.path.dirname(IMAGE_PATH)
image_name  = os.path.splitext(os.path.basename(IMAGE_PATH))[0] 
base_dir    = os.path.dirname(image_dir)                          

json_dir    = os.path.join(base_dir, "output")
excel_dir   = os.path.join(base_dir, "excel")

json_path   = os.path.join(json_dir, f"{image_name}_res.json")
excel_path  = os.path.join(excel_dir, f"{image_name}.xlsx")

# Make sure output folders exist
os.makedirs(json_dir,  exist_ok=True)
os.makedirs(excel_dir, exist_ok=True)

print(f"Running OCR on: {IMAGE_PATH}")
pipeline = PaddleOCRVL(pipeline_version="v1")
output = pipeline.predict(IMAGE_PATH)

for res in output:
    res.print()
    res.save_to_json(save_path=json_dir)

print(f"JSON saved to: {json_path}")

print(f"Reading JSON: {json_path}")
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

all_tables = []

for block in data.get("parsing_res_list", []):
    if block.get("block_label") == "table":
        html_table = block.get("block_content", "")
        try:
            dfs = pd.read_html(StringIO(html_table))
            all_tables.extend(dfs)
        except Exception as e:
            print(f"Skipped a table block due to error: {e}")

if not all_tables:
    print("No table blocks found in the OCR output.")
else:
    final_df = pd.concat(all_tables, ignore_index=True)
    final_df.to_excel(excel_path, index=False)
    print(f"Excel created successfully: {excel_path}")