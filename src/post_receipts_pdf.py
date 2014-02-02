# -*- coding: utf-8 -*-
'''
Created on 29 янв. 2014 г.

@author: dsv
'''

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import red
from reportlab.platypus.flowables import Image
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import cm


class Page_data():
    def __init__(self):
        self.sum = '' #">{{ order.real_total_rub|default:order.total_rub }} руб. 00 коп.</div>
        #self.sum_2 = '' #">{{ order.real_total_rub|default:order.total_rub }}</div>
        self.to_name = '' #">{{ order.name }}</div>
        #self.to_2 = '' #">{{ order.name }}</div>
        self.to_address = '' #">{{ order.address }}</div>
        self.to_zip_code = '' #">{{ order.zip_code }}</div>
        #self.to_address_2 = '' #">{{ order.address }}</div>
        #self.to_zip_code_2 = '' #">{{ order.zip_code }}</div>
        self.from_name = '' #">{{ from_address.name }}</div>
        self.from_address = '' #">{{ from_address.address }}</div>
        self.from_zip_code = '' # zip_code">{{ from_address.zip_code }}</div>
        self.passport_type = 'паспорт'
        self.passport_series = '' #">{{ from_address.passport_series }}</div>
        self.passport_numberv = '' #">{{ from_address.passport_number }}</div>
        self.passport_dt1 = '' #">{{ from_address.passport_date|date:"d.m" }}</div>
        #self.passport_dt2 = '' #">{{ from_address.passport_date|date:"y" }}</div>
        self.passport_by = '' #" = '' #>{{ from_address.passport_by }}</div>

        

class PostReceiptsPdf():
    
    def __init__(self, l_side_data, r_side_data=None):
        self.pdf = None
        self.lside_data = l_side_data
        self.rside_data = r_side_data
        self.base_x = 0
        self.base_y = 0
    
    def x(self,x):
        return self.base_x + x

    def y(self,y):
        return self.base_y + y

    def drawClippingString(self,text,posx,posy,sizex,sizey):
        self.pdf.saveState()
        p = self.pdf.beginPath()
        p.rect(posx,posy,sizex,sizey)
        self.pdf.clipPath(p,stroke=0)
        self.pdf.drawString(posx,posy,text)
        self.pdf.restoreState()        
    
    def create_pdf_file(self, file_name):
        self.pdf = canvas.Canvas(file_name,pagesize=landscape(A4))
        
    def set_cyrillic_font(self):
        pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))
        self.pdf.setFont('DejaVuSans', 10) # default font

    def render_page1_image(self):
        A4_Width, A4_Height = A4
        self.im = Image(u'post1.JPG',width=A4_Height, height=A4_Width)
        self.im.drawOn(self.pdf, self.x(0), self.y(0))

    def render_page1_data(self):
        self.pdf.setFont('DejaVuSans', 8)
        self.pdf.setFillColor(red)
        
        #self.pdf.drawString(2.05*cm, 15.4*cm, self.lside_data.sum)
        #self.pdf.drawString(3.5*cm, 12.05*cm, self.lside_data.to_name)
        #self.drawClippingString(self.lside_data.to_name, 3.5*cm, 9.05*cm, 6.2*cm, 1*cm)
        
        #money
        self.pdf.setFont('DejaVuSans', 12)
        self.pdf.drawString(self.x(2.05*cm), self.y(15.4*cm), self.lside_data.sum + u" руб. 00 коп.")
        self.pdf.drawString(self.x(3.53*cm), self.y(4*cm), self.lside_data.sum)
        
        #to
        self.pdf.setFont('DejaVuSans', 8)
        #name
        self.drawClippingString(self.lside_data.to_name, self.x(3.12*cm), self.y(13.85*cm), 5*cm, 0.5*cm)
        #address - need split
        self.drawClippingString(self.lside_data.to_address, self.x(3.12*cm), self.y(13.4*cm), 5*cm, 0.5*cm)
        #zip_code
        zip_code = self.pdf.beginText()
        zip_code.setTextOrigin(self.x(5.39*cm), self.y(12.55*cm))
        zip_code.setFont('DejaVuSans', 10)
        zip_code.setCharSpace(8)
        zip_code.textLine(self.lside_data.to_zip_code)
        zip_code.setCharSpace(0)
        self.pdf.drawText(zip_code)
        
        
    def write_pdf_file(self):
        self.pdf.showPage() # page end
        self.pdf.save()
        
    def make_page1_pdf_file(self, file_name=u'page1.pdf'):
        self.create_pdf_file(file_name)
        self.set_cyrillic_font()
        self.render_page1_image()
        self.render_page1_data()
        self.base_x += 14.8*cm
        self.base_y += -0.14*cm
        self.render_page1_data()
        self.write_pdf_file()
        
def make_test_data():
    #test data
    #lside_data={u'fio':u'Печеньев Иван Петрович',u'summa':u'2110 руб. 00 коп.'}
    page1_data = Page_data()
    page1_data.sum = u'2110'
    page1_data.to_name = u'Соболев Михаил Борисович - тринадцатый'
    page1_data.to_address = u'РФ, г. Москва, ул. Чебурашкина, д.13, кв. 13'
    page1_data.to_zip_code = u'107553'
    return page1_data
    
    
def main_test_lib():
    #make test page
    page1 = PostReceiptsPdf(make_test_data())
    page1.make_page1_pdf_file()     

if __name__ == '__main__':
    main_test_lib()