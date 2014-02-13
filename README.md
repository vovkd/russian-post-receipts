**Печать квитанций Почты России**

- Requirements
>python 2.7; 
reportlab 2.7

Install
```
pip install -e git+https://github.com/shantilabs/russian-post-receipts.git#egg=pdf_render
```

- Передача данных и формирование pdf файла
```python
from f116_pdf_old import F116_data
from f116_pdf import F116Pdf
data = F116_data()
#все поля текст
data.sum = u'5550 денег'
...
pdf = F116Pdf(data)
pdf.make_pdf_file(u'filename.pdf')
```
