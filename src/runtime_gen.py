# -*- coding: utf-8 -*-
'''
Created on 28 ���. 2014 �.

@author: oak
'''

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import red
from reportlab.platypus.flowables import Image
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import cm

#init
A4_Width, A4_Height = A4
pdf = canvas.Canvas(u"runtime_gen.pdf",pagesize=landscape(A4))

#render
pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))
pdf.setFont('DejaVuSans', 12)

im = Image(u'post1.JPG',width=A4_Height, height=A4_Width)
im.drawOn(pdf, 0, 0)

pdf.setFillColor(red)
pdf.drawString(10, 10, u"text")
pdf.drawString(3.5*cm, 12.05*cm, u"Печеньев Иван Пертрович")


#close save
pdf.showPage()
pdf.save()
 


if __name__ == '__main__':
    pass
    
    