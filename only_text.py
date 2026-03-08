import os
import json
from paddleocr import PaddleOCRVL

IMG_DIR = r"your_img_path"

base_dir = os.path.dirname(IMG_DIR)

json_dir = os.path.join(base_dir, "output")
txt_dir  = os.path.join(base_dir, "text")

os.makedirs(json_dir, exist_ok=True)
os.makedirs(txt_dir, exist_ok=True)

print("Initializing OCR pipeline...")
pipeline = PaddleOCRVL(pipeline_version="v1")

# supported image formats
valid_ext = (".png", ".jpg", ".jpeg", ".bmp", ".webp")

for image_file in os.listdir(IMG_DIR):

    if not image_file.lower().endswith(valid_ext):
        continue

    image_path = os.path.join(IMG_DIR, image_file)
    image_name = os.path.splitext(image_file)[0]

    json_path = os.path.join(json_dir, f"{image_name}_res.json")
    txt_path  = os.path.join(txt_dir, f"{image_name}.txt")

    print(f"\nProcessing: {image_file}")

    output = pipeline.predict(image_path)

    for res in output:
        res.save_to_json(save_path=json_dir)

    # Read JSON
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    text_lines = []

    for block in data.get("parsing_res_list", []):
        text = block.get("block_content", "").strip()
        if text:
            text_lines.append(text)

    if text_lines:
        with open(txt_path, "w", encoding="utf-8") as f:
            for line in text_lines:
                f.write(line + "\n")

        print(f"Saved text: {txt_path}")
    else:

        print("No text found.")
