import fitz

def extract_text(pdf_path, output_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += f"\n--- Page {page.number + 1} ---\n"
        text += page.get_text()
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    extract_text(r"c:\Users\yogi8\OneDrive\Desktop\skin_disease (5).pdf", r"c:\Users\yogi8\Skin_Disease_Chatbot\extracted_pdf_v5.txt")
