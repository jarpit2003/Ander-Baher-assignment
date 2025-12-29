def chunk_text(text, chunk_size=400):
    """
    Splits text into chunks of approximately `chunk_size` words.
    """
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i + chunk_size])


FILES = ["refund", "privacy", "terms"]

for name in FILES:
    with open(f"faq/{name}.txt", "r", encoding="utf-8") as f:
        text = f.read()

    chunks = list(chunk_text(text))

    with open(f"faq/{name}_chunks.txt", "w", encoding="utf-8") as out:
        out.write("\n\n".join(chunks))

    print(f"[OK] {name}: {len(chunks)} chunks created")


