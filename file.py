import os

file_path = "attention-is-all-you-need-Paper.pdf"

if os.path.getsize(file_path) == 0:
    raise ValueError("PDF file is empty!")

loader = PyPDFLoader(file_path)