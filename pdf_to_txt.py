from pypdf import PdfReader

reader = PdfReader("/Users/abhinavmishra/Downloads/harrypotter.pdf")  # Replace with your PDF
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

with open("/Users/abhinavmishra/Downloads/harrypotter.txt", "w") as f:
    f.write(text)