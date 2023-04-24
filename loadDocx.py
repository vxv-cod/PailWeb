# from io import BytesIO
# from flask import Flask, make_response
# # from docx import Document


# app = Flask(__name__)

# @app.route("/download")
# def generate_docx(doc):

#     # Создаем объект BytesIO для записи документа в память
#     output = BytesIO()

#     # Сохраняем документ в объект BytesIO
#     doc.save(output)

#     # Создаем объект Response для отправки файла пользователю
#     response = make_response(output.getvalue())

#     # Задаем тип содержимого
#     response.headers["Content-Type"] = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

#     # Задаем имя файла
#     response.headers["Content-Disposition"] = "attachment; filename=example.docx"

#     return response

# if __name__ == "__main__":
#     app.run()


'''# --------------------------------------------------------------'''
# import base64
# from io import BytesIO

# def generate_docx(document):
    
#     # сохранить документ в памяти в формате docx
#     doc_file = BytesIO()
#     # BytesIO(byte_array)
#     document.save(doc_file)
#     doc_file.seek(0)

#     # прочитать двоичные данные документа и преобразовать их в строку base64
#     docx_file_data = doc_file.read()
    
#     docx_file_base64 = base64.b64encode(docx_file_data).decode('utf-8')
#     return docx_file_base64
'''# --------------------------------------------------------------'''

# from django.http import HttpResponse

# def download_docx(document):
#     response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#     response['Content-Disposition'] = 'attachment; filename=download.docx'
#     document.save(response)
#     print('!!!!!!!!! ', response)

#     return response


# from io import BytesIO
# from django.http import HttpResponse

# def generate_docx(document):

#     global doc
#     # Создаем объект BytesIO для записи документа в память
#     output = BytesIO()

#     # Сохраняем документ в объект BytesIO
#     document.save(output)

#     # Создаем объект HttpResponse для отправки файла пользователю
#     response = HttpResponse(
#         output.getvalue(),
#         content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
#     )

#     # Задаем имя файла
#     response['Content-Disposition'] = 'attachment; filename="example.docx"'

#     return response


# import base64
# import io
# from docx import Document



# def generate_docx(document):
#     document = Document()
#     # Добавляем текст в документ
#     document.add_paragraph('Привет, Мир!')

#     # Создаем объект BytesIO
#     buffer = io.BytesIO()

#     # Сохраняем документ в байт-код
#     document.save(buffer)

#     # Получаем байт-код в виде строки
#     bytecode = buffer.getvalue()

#     # Кодируем байт-код в base64
#     base64_data = base64.b64encode(bytecode).decode('utf-8')

#     # Передаем base64-кодированный документ в HTML-страницу
#     html = f'<img src="data:image/png;base64,{base64_data}" />'
    
    
import io
import base64
# from docx import Document

def generate_docx(document):

    # document = Document()

    # # Добавляем текст в документ
    # document.add_paragraph('Привет, Мир!')

    # Создаем объект BytesIO
    buffer = io.BytesIO()

    # Сохраняем документ в байт-код
    document.save(buffer)

    # Получаем байт-код в виде строки
    bytecode = buffer.getvalue()

    # Кодируем байт-код в base64
    base64_data = base64.b64encode(bytecode).decode('utf-8')

    # Формируем ссылку на документ
    link = f'data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,{base64_data}'
    # print(link)
    # print("---link---")

    # Формируем HTML-код ссылки
    html = f'<a href="{link}">Скачать документ</a>'

    # return html
    return link