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

    def render_page1_image(self):
        A4_Width, A4_Height = A4
        self.im = Image(u'2side.jpg',width=A4_Height, height=A4_Width)
        self.im.drawOn(self.pdf, self.x(0), self.y(0))
        self.pdf.line(A4_Height/2, 10, A4_Height/2, A4_Width-10)

    def make_page1_pdf_file(self, file_name=u'page1.pdf'):
        self.create_pdf_file(file_name, page_size=landscape(A4))
        self.set_cyrillic_font()
        self.render_page1_image()
        self.render_page1_data()
        self.base_x += 14.8*cm
        #self.base_y += -0.14*cm
        self.render_page1_data()
        self.write_pdf_file()

def main_test_lib():
    #make test page
    data = list()
    data.append(make_test_data())
    data.append(make_test_data())
    page1 = PostReceipts2(data, debug=True)
    page1.make_page1_pdf_file()     



if __name__ == '__main__':
    main_test_lib()
