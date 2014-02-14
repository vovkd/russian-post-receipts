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
from f116_pdf_old import F116_data
from f116_pdf import F116Pdf
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
data2 = F116_data()
#все поля текст
data2.sum = u'5550 денег'
data2.to_name = u'ФИО кому'
data2.to_address = u'Адрес кому'
data2.to_zip_code = u'индекс кому'
data2.from_name = u"ФИО от кого"
data2.from_address = u'Адрес  от кого'
data2.from_zip_code = u'индекс  от кого'
data2.passport_type = u'паспорт - вид кокумента'
data2.passport_series = u'3939'
data2.passport_number = u'123456'
# тип datetime
tmp_date = datetime.now() #ДатаВыдачиДокумента
data2.passport_dt1 = tmp_date.strftime(u'%d.%m')
data2.passport_dt2 = tmp_date.strftime(u'%y')
data2.passport_by = u'кем выдан'

data.append(data2)

pdf = F116Pdf(data)
pdf.make_pdf_file(u'filename.pdf')
```
