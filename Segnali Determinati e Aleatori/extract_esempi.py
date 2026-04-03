import pypdf
import sys

try:
    reader = pypdf.PdfReader('esempioditesinasvolta.pdf')
    with open('esempioditesinasvolta_extracted.txt', 'w', encoding='utf-8') as f:
        for page in reader.pages:
            f.write(page.extract_text())
            f.write('\n')
except Exception as e:
    with open('esempioditesinasvolta_extracted.txt', 'w', encoding='utf-8') as f:
        f.write(str(e))
