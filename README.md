**Печать квитанций Почты России**

- Requirements
```
python 2.7 
reportlab 2.7
```
- Install
```
pip install -e git+https://github.com/shantilabs/russian-post-receipts.git#egg=pdfrender
```

- Передача данных и формирование pdf файла
```python
from pdf_render.f116_pdf import F116Pdf, F116_data
from datetime import datetime
data = list()
#левая часть бланка
data1 = F116_data()
#все поля текст
data1.sum = u'5550 денег'
data1.to_name = u'ФИО кому'
data1.to_address = u'Адрес кому'
data1.to_zip_code = u'индекс кому'
data1.from_name = u"ФИО от кого"
data1.from_address = u'Адрес  от кого'
data1.from_zip_code = u'индекс  от кого'
data1.passport_type = u'паспорт - вид кокумента'
data1.passport_series = u'3939'
data1.passport_number = u'123456'
# тип datetime
tmp_date = datetime.now() #ДатаВыдачиДокумента
data1.passport_dt1 = tmp_date.strftime(u'%d.%m')
data1.passport_dt2 = tmp_date.strftime(u'%y')
data1.passport_by = u'кем выдан'

data.append(data1)

#правая часть бланка
tmp_date = datetime.now() #ДатаВыдачиДокумента
data_kwargs=[
			'sum': u'5550 денег'   
			'to_name': u'ФИО кому'
			'to_address': u'Адрес кому'
			'to_zip_code': u'индекс кому'
			'from_name': u"ФИО от кого"
			'from_address': u'Адрес  от кого'
			'from_zip_code': u'индекс  от кого'
			'passport_type': u'паспорт - вид кокумента'
			'passport_series': u'3939'
			'passport_number': u'123456'
			'passport_dt1': tmp_date.strftime(u'%d.%m')
			'passport_dt2': tmp_date.strftime(u'%y')
			'passport_by': u'кем выдан'
			]
data2 = F116_data(data_kwargs)

data.append(data2)

pdf = F116Pdf(data)
pdf.make_pdf_file(u'filename.pdf')
```
