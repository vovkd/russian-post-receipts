# -*- coding: utf-8 -*-
'''
Created on 29 янв. 2014 г.

@author: dsv
'''

#from reportlab.pdfbase import pdfmetrics
#from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus.flowables import Image
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import cm
#from reportlab.lib.colors import red, black
from datetime import datetime, date
from dateutil import parser

from base_pdf import BasePdf, _self_path, Base_data

class F116_data(Base_data):
    def __init__(self, **kwargs):
        super(F116_data, self).__init__(**kwargs)
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
        self.passport_type = u'паспорт'
        self.passport_series = '' #">{{ from_address.passport_series }}</div>
        self.passport_number = '' #">{{ from_address.passport_number }}</div>
        self.passport_dt1 = '' #">{{ from_address.passport_date|date:"d.m" }}</div>
        self.passport_dt2 = '' #">{{ from_address.passport_date|date:"y" }}</div>
        self.passport_by = '' #" = '' #>{{ from_address.passport_by }}</div>
        self._passport_date = date.today()
        self.set_data(**kwargs)
        if 'passport_date' in kwargs:
            self.passport_date = kwargs['passport_date']
    
    @property
    def passport_date(self):
        return self._passport_data
    
    @passport_date.setter
    def passport_date(self, value):
        if type(value) is datetime or type(value) is date:
            self._passport_date = value
        else: 
            if type(value) is str or type(value) is unicode:
                #self._passport_date = parser.parse(value, fuzzy=True)
                self._passport_date = parser.parse(value)
            else:
                raise ValueError
        self.set_dt1_dt2()
    
    def set_dt1_dt2(self):
        if self._passport_date:
            self.passport_dt1 = self._passport_date.strftime(u'%d.%m')
            self.passport_dt2 = self._passport_date.strftime(u'%y')

class F116PdfOld(BasePdf):
    
    def __init__(self, data, debug=False):
        super(F116PdfOld, self).__init__(data, debug)
        if data:
            self.lside_data = data[0]
            self.rside_data = data[1]

    def create_pdf_file(self, file_name, page_size=landscape(A4)):
        super(F116PdfOld, self).create_pdf_file(file_name, page_size)
    
    def render_page1_image(self):
        A4_Width, A4_Height = A4
        self.im = Image(_self_path+ '/' + u'post1.JPG',width=A4_Height, height=A4_Width)
        self.im.drawOn(self.pdf, self.x(0), self.y(0))

    def render_page2_image(self):
        A4_Width, A4_Height = A4
        self.im = Image(_self_path+ '/' + u'post2.JPG',width=A4_Height, height=A4_Width)
        self.im.drawOn(self.pdf, self.x(0), self.y(0))


    def render_page1_oneside_data(self, side_data):
        self.pdf.setFont('DejaVuSans', 8)

        #money
        self.pdf.setFont('DejaVuSans', 12)
        self.pdf.drawString(self.x(2.05*cm), self.y(15.4*cm), side_data.sum + u" руб. 00 коп.")
        self.pdf.drawString(self.x(3.53*cm), self.y(4*cm), side_data.sum)
        
        #to
        self.pdf.setFont('DejaVuSans', 8)
        #name
        self.drawClippingString(side_data.to_name, self.x(3.12*cm), self.y(13.8*cm), 5.1*cm, 0.5*cm)
        #address - if need split
        if len(side_data.to_address) >= 33: # 33chars for font size 8
            #split to 2 line
            self.drawClippingString(side_data.to_address[:33], self.x(3.12*cm), self.y(13.35*cm), 5.1*cm, 0.5*cm)
            #if len(side_data.to_address[34:] >= ?)# need 3 line?
            self.drawClippingString(side_data.to_address[33:], self.x(2.02*cm), self.y(12.95*cm), 6.1*cm, 0.5*cm)
        else:
            self.drawClippingString(side_data.to_address, self.x(3.12*cm), self.y(13.35*cm), 5.1*cm, 0.5*cm)
            
        #zip_code
        zip_code = self.pdf.beginText()
        zip_code.setTextOrigin(self.x(5.39*cm), self.y(12.55*cm))
        zip_code.setFont('DejaVuSans', 10)
        zip_code.setCharSpace(8)
        zip_code.textLine(side_data.to_zip_code)
        zip_code.setCharSpace(0)
        self.pdf.drawText(zip_code)
        
        #from
        #name
        self.drawClippingString(side_data.from_name, self.x(3.5*cm), self.y(12*cm), 9.05*cm, 0.5*cm)
        #address - if need split
        if len(side_data.from_address) >= 60: # chars for font size 8
            #split to 2 line
            self.drawClippingString(side_data.from_address[:60], self.x(3.12*cm), self.y(11.5*cm), 9.6*cm, 0.5*cm)
            #if len(side_data.to_address[34:] >= ?)# need 3 line?
            self.drawClippingString(side_data.from_address[60:], self.x(2.03*cm), self.y(11*cm), 7.5*cm, 0.5*cm)
        else:
            self.drawClippingString(side_data.from_address, self.x(3.12*cm), self.y(11.5*cm), 5.1*cm, 0.5*cm)
            
        #zip_code
        zip_code = self.pdf.beginText()
        zip_code.setTextOrigin(self.x(9.77*cm), self.y(11.04*cm))
        zip_code.setFont('DejaVuSans', 10)
        zip_code.setCharSpace(8)
        zip_code.textLine(side_data.from_zip_code)
        zip_code.setCharSpace(0)
        self.pdf.drawText(zip_code)


        #to_down
        self.pdf.setFont('DejaVuSans', 8)
        #name
        self.drawClippingString(side_data.to_name, self.x(3.12*cm), self.y(3.3*cm), 9.4*cm, 0.5*cm)
        #address - if need split
        if len(side_data.to_address) >= 60: # 60chars for font size 8
            #split to 2 line
            self.drawClippingString(side_data.to_address[:60], self.x(3.2*cm), self.y(2.75*cm), 9.4*cm, 0.5*cm)
            #if len(side_data.to_address[34:] >= ?)# need 3 line?
            self.drawClippingString(side_data.to_address[60:], self.x(2*cm), self.y(2.28*cm), 7.5*cm, 0.5*cm)
        else:
            self.drawClippingString(side_data.to_address, self.x(3.2*cm), self.y(2.75*cm), 9.4*cm, 0.5*cm)
            
        #zip_code
        zip_code = self.pdf.beginText()
        zip_code.setTextOrigin(self.x(9.77*cm), self.y(2.18*cm))
        zip_code.setFont('DejaVuSans', 10)
        zip_code.setCharSpace(8)
        zip_code.textLine(side_data.to_zip_code)
        zip_code.setCharSpace(0)
        self.pdf.drawText(zip_code)
        
        #passport data
        self.pdf.setFontSize(8)
        self.drawClippingString2(side_data.passport_type , self.x(3.9*cm), self.y(9.6*cm), 8)
        self.drawClippingString2(side_data.passport_series , self.x(6.35*cm), self.y(9.6*cm), 4)
        self.drawClippingString2(side_data.passport_number , self.x(7.5*cm), self.y(9.6*cm), 6)
        self.drawClippingString2(side_data.passport_dt1 , self.x(10.5*cm), self.y(9.6*cm), 5)
        self.drawClippingString2(side_data.passport_dt2 , self.x(12.2*cm), self.y(9.6*cm), 2)
        self.drawClippingString2(side_data.passport_by , self.x(2.1*cm), self.y(9.1*cm), 65)
        
     
    def _make_page1_pdf(self, file_name=u'page1.pdf'):
        self.create_pdf_file(file_name, page_size=landscape(A4))
        self.set_cyrillic_font()
        self.render_page1_image()
        self.render_page1_oneside_data(self.lside_data)
        self.base_x += 14.8*cm
        self.base_y += -0.14*cm
        self.render_page1_oneside_data(self.rside_data)
        self.pdf.showPage() # page end
        #page 2
        self.base_x = 0
        self.base_y = 0
        self.render_page2_image()
        self.end_page()
        self.write_pdf_file()
        
    def make_pdf_file(self, file_name=u'F116.pdf'):
        self._make_page1_pdf(file_name)
        
def make_test_data():
    #test data
    page1_data = F116_data(sum='55555555')
    page1_data.sum = u'2110'
    page1_data.to_name = u'Соболев Михаил Борисович - тринадцатый'
    page1_data.to_address = u'РФ, г. Москва, ул. Чебурашкина, д.13, кв. 13'
    page1_data.to_zip_code = u'107553'
    page1_data.from_name = u"его величество Бурухтан-Бурухтан второй второй его величество Бурухтан-Бурухтан второй второй"
    page1_data.from_address = u'Тридевятое царсктво, тридесятое государство, 3 изба справа, третий колокол звонить шесть раз по пять раз 123456789123456789'
    page1_data.from_zip_code = u'393939'
    page1_data.passport_type = u'паспорт'
    page1_data.passport_series = u'3939'
    page1_data.passport_number = u'123456'
    tmpDate = datetime.now()
    #page1_data.passport_dt1 = tmpDate.strftime(u'%d.%m')
    #page1_data.passport_dt2 = tmpDate.strftime(u'%y')
    page1_data.passport_by = u'Отделением по району Мордор ОУФМС России по г. Москва'
    page1_data.passport_date = tmpDate
    #page1_data.passport_date = u"2013/01/03"
    #page1_data.passport_date = u"Vasiliy"
    
    #long tst
    #page1_data.to_name = page1_data.from_name
    #page1_data.to_address = page1_data.from_address
    
    #page1_data.from_name = page1_data.to_name
    #page1_data.from_address = page1_data.to_address

    return page1_data
    
    
def test_F116Pdf():
    #make test page
    data = list()
    data.append(make_test_data())
    r_side = F116_data(passport_date = "1945/05/09")
    #data.append(make_test_data())
    data.append(r_side)
    page1 = F116PdfOld(data, debug=True)
    page1.make_pdf_file("test_f116.pdf")   

if __name__ == '__main__':
    test_F116Pdf()