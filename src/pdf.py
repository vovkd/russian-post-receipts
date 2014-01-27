# -*- coding: utf-8 -*-

import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import reportlab

from reportlab.pdfgen import canvas

pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))
from reportlab.lib.fonts import addMapping
addMapping('Helvetica', 0, 0, 'DejaVuSans')
addMapping('Helvetica', 1, 0, 'DejaVuSans')
addMapping('Helvetica', 0, 1, 'DejaVuSans')
addMapping('Helvetica', 1, 1, 'DejaVuSans')
#pdfmetrics.registerFont(TTFont('Helvetica', 'DejaVuSans.ttf'))

MyCanvas = canvas.Canvas("hello.pdf")

MyCanvas.setFont('DejaVuSans', 12)
MyCanvas.drawString(270, 410, u"превед!!!")
MyCanvas.drawString(270, 310, u"sergey!!!")
MyCanvas.showPage()
MyCanvas.save()