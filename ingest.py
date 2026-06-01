import re
import fitz


def extract_text(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)

    pages = []
    for page_num, page in enumerate(doc):
        # Page 0 is "how to use this site" — skip it
        # Page 1 is mixed: TOC at top, then real rules start (1.1)  keep
        if page_num < 1:
            continue
        pages.append(page.get_text())

    raw = "\n".join(pages)
    return clean_text(raw)


def clean_text(text: str) -> str:
    # Strip the repeated page footer that appears on every page.
    # The footer is always these four lines in order:
    #   <timestamp>  e.g. "6/1/26, 6:35 PM"
    #   "The Law of Root: A Woodland Game of Might and Right"
    #   "root.livingrules.io/..."
    #   "<n>/24"
    footer_pattern = re.compile(
        r"\d+/\d+/\d+,\s+\d+:\d+\s+[AP]M\n"
        r"The Law of Root:.*?\n"
        r"root\.livingrules\.io.*?\n"
        r"\d+/24\n",
        re.IGNORECASE,
    )
    text = footer_pattern.sub("", text)

    # Collapse runs of blank lines down to a single blank line
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def chunk_text(text: str, size: int = 700, step: int = 600) -> list[dict]:
    chunks = []
    start = 0

    while start < len(text):
        end = start + size
        chunk = text[start:end]

        # Find the last section number mentioned in this chunk for the citation.
        # Section numbers look like "1.1", "2.3.1", "9.5.3" etc.
        matches = re.findall(r"\b(\d+\.\d+(?:\.\d+)*)\b", chunk)
        section = matches[-1] if matches else "unknown"

        chunks.append({"text": chunk, "section": section})
        start += step

    return chunks


if __name__ == "__main__":
    text = extract_text("root.pdf")
    print(f"Total characters: {len(text)}")

    chunks = chunk_text(text)
    print(f"Total chunks: {len(chunks)}")
    print("\n--- Chunk 5 (sample) ---")
    print(f"Section: {chunks[5]['section']}")
    print(chunks[5]['text'])
    print("\n--- Chunk 6 (overlaps with 5) ---")
    print(f"Section: {chunks[6]['section']}")
    print(chunks[6]['text'])