# -*- coding: utf-8 -*-
'''
Created on 29 янв. 2014 �.

@author: dsv
'''

from wsgiref.simple_server import make_server
from post_receipts_pdf import make_test_data, PostReceiptsPdf
import cStringIO

def test_pdf_gen_app(environ, start_response):
    status = '200 OK' # HTTP Status
    #headers = [('Content-type', 'text/plain')] # HTTP Headers
    headers = [('Content-type', 'application/pdf'), ('Content-Disposition', 'attachment'),
               ('filename', 'test_page.pdf')]
    start_response(status, headers)
    
    page =  PostReceiptsPdf(make_test_data())
    str_buf = cStringIO.StringIO()
    page.make_page1_pdf_file(str_buf)

    return str_buf.getvalue()

httpd = make_server('', 8000, test_pdf_gen_app)
print "Serving on port 8000..."

# Serve until process is killed
##httpd.serve_forever()

# Alternative: serve one request, then exit
httpd.handle_request()

if __name__ == '__main__':
    pass