# -*- coding: utf-8 -*-

'''
Created on 07 ����. 2014 �.

@author: dsv
'''

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.platypus.flowables import Image

from post_receipts_pdf import PostReceiptsPdf, make_test_data

class PostReceipts2(PostReceiptsPdf):
    def __init__(self, data, debug=False):
        PostReceiptsPdf.__init__(self, data, debug)

    def render_page_image(self):
        A4_Width, A4_Height = A4
        self.im = Image(u'2side.jpg',width=A4_Height, height=A4_Width)
        self.im.drawOn(self.pdf, self.x(0), self.y(0))
        self.pdf.line(A4_Height/2, 10, A4_Height/2, A4_Width-10)

    def render_page_data(self):
        self.pdf.setFont('DejaVuSans', 8)

        #money
        self.pdf.setFont('DejaVuSans', 12)
        self.pdf.drawString(self.x(0.9*cm), self.y(15.85*cm), self.lside_data.sum + u" руб. 00 коп.")
        self.pdf.setFont('DejaVuSans', 10)
        self.pdf.drawString(self.x(2.20*cm), self.y(3.92*cm), self.lside_data.sum)
        
        #to
        self.pdf.setFont('DejaVuSans', 8)
        #name
        self.drawClippingString2(self.lside_data.to_name, self.x(1.7*cm), self.y(14.4*cm), 47)
        #address - if need split
        if len(self.lside_data.to_address) >= 50: # 33chars for font size 8
            #split to 2 line
            self.drawClippingString2(self.lside_data.to_address[:50], self.x(1.79*cm), self.y(13.85*cm), 50)
            #if len(self.lside_data.to_address[34:] >= ?)# need 3 line?
            self.drawClippingString2(self.lside_data.to_address[50:], self.x(0.9*cm), self.y(13.2*cm), 55)
        else:
            self.drawClippingString2(self.lside_data.to_address, self.x(1.79*cm), self.y(13.85*cm), 50)
            
        #zip_code
        zip_code = self.pdf.beginText()
        zip_code.setTextOrigin(self.x(6.86*cm), self.y(12.55*cm))
        zip_code.setFont('DejaVuSans', 10)
        zip_code.setCharSpace(8)
        zip_code.textLine(self.lside_data.to_zip_code)
        zip_code.setCharSpace(0)
        self.pdf.drawText(zip_code)
        
        #from
        #name
        self.drawClippingString2(self.lside_data.from_name, self.x(2.0*cm), self.y(11.85*cm), 68)
        #address - if need split
        if len(self.lside_data.from_address) >= 72: # chars for font size 8
            #split to 2 line
            self.drawClippingString2(self.lside_data.from_address[:72], self.x(1.8*cm), self.y(11.12*cm), 72)
            #if len(self.lside_data.to_address[34:] >= ?)# need 3 line?
            self.drawClippingString2(self.lside_data.from_address[72:], self.x(0.9*cm), self.y(10.55*cm), 57)
        else:
            self.drawClippingString2(self.lside_data.from_address, self.x(1.8*cm), self.y(11.12*cm), 72)
            
        #zip_code
        zip_code = self.pdf.beginText()
        zip_code.setTextOrigin(self.x(10.33*cm), self.y(10.6*cm))
        zip_code.setFont('DejaVuSans', 10)
        zip_code.setCharSpace(8)
        zip_code.textLine(self.lside_data.from_zip_code)
        zip_code.setCharSpace(0)
        self.pdf.drawText(zip_code)


        #to_down
        self.pdf.setFont('DejaVuSans', 8)
        #name
        self.drawClippingString2(self.lside_data.to_name, self.x(1.7*cm), self.y(3.12*cm), 73)
        #address - if need split
        if len(self.lside_data.to_address) >= 60: # 60chars for font size 8
            #split to 2 line
            self.drawClippingString2(self.lside_data.to_address[:60], self.x(1.8*cm), self.y(2.35*cm), 70)
            #if len(self.lside_data.to_address[34:] >= ?)# need 3 line?
            self.drawClippingString2(self.lside_data.to_address[60:], self.x(0.9*cm), self.y(1.55*cm), 57)
        else:
            self.drawClippingString2(self.lside_data.to_address, self.x(1.8*cm), self.y(2.35*cm), 77)
            
        #zip_code
        zip_code = self.pdf.beginText()
        zip_code.setTextOrigin(self.x(10.4*cm), self.y(1.6*cm))
        zip_code.setFont('DejaVuSans', 10)
        zip_code.setCharSpace(8)
        zip_code.textLine(self.lside_data.to_zip_code)
        zip_code.setCharSpace(0)
        self.pdf.drawText(zip_code)
        
        #passport data
        self.pdf.setFontSize(8)
        self.drawClippingString2(self.lside_data.passport_type , self.x(2.9*cm), self.y(9.18*cm), 8)
        self.drawClippingString2(self.lside_data.passport_series , self.x(5.85*cm), self.y(9.18*cm), 4)
        self.drawClippingString2(self.lside_data.passport_number , self.x(7.6*cm), self.y(9.18*cm), 6)
        self.drawClippingString2(self.lside_data.passport_dt1 , self.x(10.5*cm), self.y(9.18*cm), 5)
        self.drawClippingString2(self.lside_data.passport_dt2 , self.x(12.5*cm), self.y(9.18*cm), 2)
        self.drawClippingString2(self.lside_data.passport_by , self.x(0.8*cm), self.y(8.6*cm), 75)
        
     

    def _make_page1_pdf_file(self, file_name=u'page1.pdf'):
        self.create_pdf_file(file_name, page_size=landscape(A4))
        self.set_cyrillic_font()
        self.render_page_image()
        self.render_page_data()
        self.base_x += 15.1*cm
        #self.base_y += -0.14*cm
        self.render_page_data()
        self.write_pdf_file()
    
    def make_pdf_file(self, file_name=u'F116.pdf'):
        self._make_page1_pdf_file(file_name)

def main_test_lib():
    #make test page
    data = list()
    data.append(make_test_data())
    data.append(make_test_data())
    page1 = PostReceipts2(data, debug=True)
    page1.make_pdf_file(u'test_f116.pdf')     


if __name__ == '__main__':
    main_test_lib()
