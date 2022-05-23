from re import T
from xml.dom.pulldom import CHARACTERS
from docx import Document # type: ignore
from docx.enum.style import WD_STYLE_TYPE # type: ignore

doc = Document("../example_reports/Simply Ecology - Cassidy Ashton - 24 Low Moor Road Blackpool - Bat Building - March 2022.docx")
styles = doc.styles
paragraphs = doc.paragraphs

# for style in styles:
#     if style.type == WD_STYLE_TYPE.PARAGRAPH:
#         print(style.name)
#     # endif
# # endfor
results_text = False

for para in paragraphs:
    if para.style.name == "Simply Heading" and results_text:
        results_text = False
    # endif
    if para.style.name == "Simply Heading" and para.text == "Survey Results":
        results_text = True
    # endif
    if results_text and len(para.text) != 0:
        print(para.text + ":" + para.style.name)
    #endif
# endfor