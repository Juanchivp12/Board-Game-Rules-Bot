import fitz

doc = fitz.open("root.pdf")

print(f'Pages: {len(doc)}')

for page_num, page in enumerate(doc):
    print(f'---Page: {page_num + 1} ---')
    print(page.get_text())