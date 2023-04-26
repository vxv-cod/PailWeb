
import io
import base64


def generate_docx(document):

    # Создаем объект буфера BytesIO
    buffer = io.BytesIO()

    # Сохраняем документ в байт-код
    document.save(buffer)

    # Получаем байт-код в виде строки
    bytecode = buffer.getvalue()

    # Кодируем байт-код в base64
    base64_data = base64.b64encode(bytecode).decode('utf-8')

    # Формируем ссылку на документ
    link = f'data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,{base64_data}'

    # Формируем HTML-код ссылки
    # html = f'<a href="{link}" download="555.docx" target="_blank">Скачать документ</a>'
    # html = f'<button type="button" id="loaddocx"><a href="{link}">Скачать документ</a></button>'
    # html = f'<a id="loaddocx" href="{link}">Скачать документ</a>'

    return link
    # return html