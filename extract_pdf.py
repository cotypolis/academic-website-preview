import sys

try:
    import fitz  # PyMuPDF
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pymupdf"])
    import fitz

def extract_pdf(pdf_path, search_term=None):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text() + "\n"
    
    if search_term:
        lines = text.split("\n")
        start_idx = -1
        for i, line in enumerate(lines):
            if search_term.lower() in line.lower():
                start_idx = i
                break
        if start_idx != -1:
            print(f"Found '{search_term}' at line {start_idx}. Snippet:")
            print("\n".join(lines[start_idx:min(len(lines), start_idx+100)]))
        else:
            print(f"Term '{search_term}' not found.")
    else:
        print(text)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf_path")
    parser.add_argument("--search", default=None)
    args = parser.parse_args()
    extract_pdf(args.pdf_path, args.search)
