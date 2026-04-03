import pypdf
import sys

try:
    reader = pypdf.PdfReader('consegna.pdf')
    with open('consegna_extracted.txt', 'w', encoding='utf-8') as f:
        for page in reader.pages:
            f.write(page.extract_text())
            f.write('\n')
except Exception as e:
    with open('consegna_extracted.txt', 'w', encoding='utf-8') as f:
        f.write(str(e))
