# Image to Excel — Image Data Extraction and Excel Export

Lightweight Python utilities to extract text/data from images and export results to Excel. This repository contains scripts to run image extraction (OCR / processing), convert JSON results into Excel sheets, and helpers to build spreadsheets from extracted image data.

**Status:** Works locally. Run `python excel_sheet.py` to start the default flow.

---

## 🚀 Core Idea

Many times, we encounter:

- Screenshots of tables  
- Restricted portals where copy/download is disabled  
- Confidential documentation where data cannot be shared externally  

Instead of manually copying and formatting the table in Excel, this tool:

1. Takes a **table image (rows + columns)**  
2. Extracts structured data using OCR + processing  
3. Converts it into a properly formatted Excel sheet  
4. Saves everything locally (no external upload required)  

This makes it suitable for handling sensitive or restricted data environments.


## Features
- Extract text and structured data from images (OCR pipeline)
- Convert extraction JSON to Excel (`.xlsx`) files
- Organize outputs under `output/` and store images under `img/`

---

## Quick Start

1. Create and activate a virtual environment (Windows / bash):

```bash
python -m venv .venv
source .venv/Scripts/activate
```

2. Install dependencies (suggested packages):

```bash
pip install -U pip
pip install pandas openpyxl pillow pytesseract opencv-python paddleocr paddlepaddle
```

3. Run the main script that assembles Excel sheets:

```bash
python excel_sheet.py
```

This will read/process files according to the scripts' logic and write outputs into the `output/` folder.

---

## Files and Purpose
- `/excel_sheet.py`: Entry-point script that orchestrates the pipeline (reads intermediate JSON outputs and creates consolidated Excel sheets). Run this to produce the final Excel files.
- `/output/`: Folder that stores generated outputs. Example file: `images_res.json` (extraction JSON).
- `/img/`: Folder for input images used by the extraction script.

---

## Usage Examples

- To run extraction on images

```bash
python excel_sheet.py
```

---

## Contributing
- Create issues for bugs or feature requests.
- Send PRs with focused changes and a short description of the intent.

---

## License
Choose a license (MIT, Apache-2.0, etc.) and add a `LICENSE` file. If you want, I can add an MIT `LICENSE` for you.

---

## Contact
If you want help polishing the repo for GitHub (adding CI, `requirements.txt`, or a `setup.py`/`pyproject.toml`), tell me what you'd like and I can scaffold it.
