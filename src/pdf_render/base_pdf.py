# -*- coding: utf-8 -*-

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import red, pink, black
#from reportlab.platypus.flowables import Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

import os
_self_path = os.path.dirname(os.path.abspath(__file__))

class Base_data(object):
    
    def __init__(self, **kwagrs):
        #self.set_data(**kwagrs)
        pass
    
    def set_data(self, **kwargs):
        for key in kwargs:
            if hasattr(self, key):
                self.__dict__[key] = kwargs[key]
                #print "variables: %s = %s" % (key, kwargs[key])
        

class BasePdf(object):
    
    def __init__(self, pdf_data=None, debug=False):
        self.pdf = None
        self.data = pdf_data 
        self.base_x = 0
        self.base_y = 0
        self.debug = debug
    
    def x(self,x):
        return self.base_x + x

    def y(self,y):
        return self.base_y + y

    def drawClippingString(self,text,posx,posy,sizex,sizey):
        self.pdf.saveState()
        p = self.pdf.beginPath()
        p.rect(posx,posy,sizex,sizey)
        self.pdf.setStrokeColor(pink if self.debug else black)
        self.pdf.clipPath(p,stroke= 1 if self.debug else 0)
        self.pdf.drawString(posx,posy + 0.05*cm,text)
        self.pdf.restoreState()
    
    def drawClippingString2(self, text, posx, posy, text_length):
        self.pdf.saveState()
        p = self.pdf.beginPath()
        if len(text)< text_length:
            tmpStr = u''.join((text,("_" * (text_length - len(text)+1))))
            size_x = self.pdf.stringWidth(tmpStr) + 1
        else:
            size_x = self.pdf.stringWidth(text[:text_length]) + 1
        #size_xx =  self.pdf._fontsize / 1.56  * text_length;
        size_y = self.pdf._fontsize ;
        p.rect(posx - 1, posy - 1, size_x, size_y)
        self.pdf.setStrokeColor(pink if self.debug else black)
        self.pdf.clipPath(p, stroke= 1 if self.debug else 0)
        self.pdf.drawString(posx, posy, text)
        self.pdf.restoreState()
    
    def create_pdf_file(self, file_name, page_size=A4):
        self.base_x = 0;
        self.base_y = 0;
        self.pdf = canvas.Canvas(file_name,pagesize=page_size)
        
    def set_cyrillic_font(self):
        pdfmetrics.registerFont(TTFont('DejaVuSans', _self_path + '\\' 'DejaVuSans.ttf'))
        self.pdf.setFont('DejaVuSans', 10) # default font
        if self.debug:
            self.pdf.setFillColor(red)
        else:
            self.pdf.setFillColor(black)
            

    def write_pdf_file(self):
        self.pdf.showPage() # page end
        self.pdf.save()
        
    def _make_data(self):
        self.pdf.setFont('DejaVuSans', 8)
        self.pdf.drawString(self.x(100), self.y(800), u'Здесь могла быть Ваша реклама')
        
    def make_pdf_file(self, file_name=u'BasePdf.pdf'):
        self.create_pdf_file(file_name)
        self.set_cyrillic_font()
        self._make_data()
        self.write_pdf_file()
        
   
def test_base_pdf():
    #make test page
    page = BasePdf()
    page.make_pdf_file()     

if __name__ == '__main__':
    test_base_pdf()