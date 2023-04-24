let formData = {}
const form = document.querySelector('form')
const LS = localStorage;
// LS.clear()
// console.log(form.elements)
// eel.value_py(form.elements);


// получить данные из input
form.addEventListener('input', function(event){
    formData[event.target.name] = event.target.value;
    LS.setItem('formData', JSON.stringify(formData));
    // eel.printpy('formData = ', formData)
});


// Восстановить данные в ячейи
if (LS.getItem('formData')) {
    formData = JSON.parse(LS.getItem('formData'));
    // form.elements[name]
    for (let key in formData){
        if (key != 'my-docx-content') {
            // eel.printpy('key = ', key)
            form.elements[key].value = formData[key];
        }
    }
}


// Отслеживание нажатие кнопки
document.querySelector("#submit").onclick = async function sendData(){ 
    let formDataPy = {};
    for (let key in form.elements){
        if (form.elements[key].value != ''  && form.elements[key].value != null) {
            formDataPy[key] = form.elements[key].value;
        }
    }
    let content = await eel.value_py(formDataPy)();
    let el = document.getElementById('my-docx-content');
    // el.innerHTML  = content[0];
    el.innerHTML  = content[0];
  
    // Вставляем картинку с геологическим разрезом
    const razrez = document.querySelector('.razrez');
    // razrez.innerHTML  = '<img class="geolograxrezimg" src="./image.png" alt="Картинка"></img>';
    razrez.innerHTML  = content[1];

    
// } 

// let qqq = document.querySelector('.qqq');
// qqq.innerHTML  = content[2];

    
    
    // // создать объект Blob для docx файла
    // const docxFileData = content[2];
    // // const blob = new Blob([docxFileData], { type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' });
    // const blob = new Blob([docxFileData], { type: 'application/msword' });

    // // // // создать URL для объекта Blob
    // // const url = URL.createObjectURL(blob);
    // // const url = '/result.docx';
    // const url = URL.createObjectURL(blob);
    // console.log(url)

    // // // создать ссылку на скачивание файла
    // const link = document.createElement('a');
    // link.href = url;
    // link.download = 'result.docx';

    // // добавить ссылку на страницу и кликнуть по ней, чтобы загрузить файл
    // document.body.appendChild(link);
    // link.click();

    // // освободить ресурсы, используемые URL-адресом объекта Blob
    // URL.revokeObjectURL(url);

    
    
    
    const link = document.createElement('a');

    link.href = content[2];
    link.download = 'result.docx';

    // добавить ссылку на страницу и кликнуть по ней, чтобы загрузить файл
    // document.body.appendChild(link);
    link.click();

    // освободить ресурсы, используемые URL-адресом объекта Blob
    URL.revokeObjectURL(url);

} 





























// =================================================================================
// // Размер экрана
// const screenWidth = window.screen.width
// const screenHeight = window.screen.height
// eel.value_py(screenWidth);
// eel.value_py(screenHeight);

// const windowOuterWidth = window.outerWidth
// const windowOuterHeight = window.outerHeight
// eel.value_py(windowOuterWidth);
// eel.value_py(windowOuterWidth);

// const windowInnerWidth = document.documentElement.clientWidth
// const windowInnerHeight = document.documentElement.clientHeight
// eel.value_py(windowInnerWidth);
// eel.value_py(windowInnerHeight);

// const pageWidth = document.documentElement.scrollWidth
// const pageHeight = document.documentElement.scrollHeight
// eel.value_py(pageWidth);
// eel.value_py(pageHeight);

// Отслеживаем размер окна для настройки
// window.addEventListener(`resize`, event => {
//     const windowOuterHeight = window.outerHeight
//     eel.value_py(windowOuterHeight);
// }, false);

// Отслеживание закрытие окна
// window.addEventListener('beforeunload', (event) => {
//     event.preventDefault();
//     let ааа = event.returnValue = LS.clear();
//     eel.value_py(ааа);
// });


