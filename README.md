**Печать квитанций Почты России**

- Requirements
>python 2.7; 
reportlab 2.7

- Передача данных и формирование pdf файла
```python
from post_receipts_pdf import F116_data
from post_receipts2 import PostReceipts2
data = F116_data()
#все поля текст
data.sum = u'5550 денег'
...
pdf = PostReceipts2(data)
pdf.make_pdf_file(u'filename.pdf')
```
