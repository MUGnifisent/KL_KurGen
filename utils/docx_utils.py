from datetime import date

from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt


def title_page(document, PIB):
    style = document.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    document.add_paragraph('Міністерство освіти і науки України').alignment = WD_ALIGN_PARAGRAPH.CENTER
    document.add_paragraph('Національний університет "Львівська Політехніка"').alignment = WD_ALIGN_PARAGRAPH.CENTER
    document.add_paragraph('Кафедра ЕОМ').alignment = WD_ALIGN_PARAGRAPH.CENTER
    document.add_paragraph('\n\n\n\n\n\n\nЗвіт').alignment = WD_ALIGN_PARAGRAPH.CENTER
    document.add_paragraph('до курсової роботи').alignment = WD_ALIGN_PARAGRAPH.CENTER
    document.add_paragraph('з дисципліни "Комп\'ютерна логіка"').alignment = WD_ALIGN_PARAGRAPH.CENTER
    document.add_paragraph('\n\n\n\n\n\nВиконав:').alignment = WD_ALIGN_PARAGRAPH.RIGHT
    document.add_paragraph('ст. групи КІ-210').alignment = WD_ALIGN_PARAGRAPH.RIGHT
    document.add_paragraph(PIB.split(' ', 1)[0] + " " + PIB[PIB.find(" ",0)+1] + ". " + PIB[PIB.find(" ", PIB.find(" ",0)+1)+1] + ".").alignment = WD_ALIGN_PARAGRAPH.RIGHT
    document.add_paragraph('Прийняв:').alignment = WD_ALIGN_PARAGRAPH.RIGHT
    document.add_paragraph('доцент каф. ЕОМ').alignment = WD_ALIGN_PARAGRAPH.RIGHT
    document.add_paragraph('Голембо В. А.').alignment = WD_ALIGN_PARAGRAPH.RIGHT
    document.add_paragraph('\n\n\n\n\n\n\n\n\nЛьвів ' + str(date.today().year)).alignment = WD_ALIGN_PARAGRAPH.CENTER
    document.add_page_break()
