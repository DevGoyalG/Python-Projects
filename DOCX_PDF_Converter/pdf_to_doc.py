from pdf2docx import Converter

old_pdf = "ML.pdf"
new_doc = "ML.docx"

obj = Converter(old_pdf)
obj.convert(new_doc)
obj.close()