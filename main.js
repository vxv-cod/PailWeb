let formData = {}
const form = document.querySelector('form')
const LS = localStorage;
// LS.clear()
console.log(form.elements)
// eel.value_py(form.elements);

// получить данные из input
form.addEventListener('input', function(event){
    formData[event.target.name] = event.target.value;
    LS.setItem('formData', JSON.stringify(formData));
    eel.value_py(formData);
});

// Восстановить данные в ячейи
if (LS.getItem('formData')) {
    formData = JSON.parse(LS.getItem('formData'));
    // form.elements[name]
    for (let key in formData){
        form.elements[key].value = formData[key];
        // console.log(key, form.elements[key].value, formData[key])
    }
}


// eel.value_py(formData);
// document.querySelector('button').onclick = sendData;

// Отслеживание нажатие кнопки
let btn = document.querySelector("#submit");
btn.addEventListener("click", sendData);

let formDataPy = {}

function sendData() {
    eel.value_py('Данные собраны');
    eel.value_py(formData);
    for (let key in form.elements){
        console.log(form.elements[key].value);
        if (form.elements[key].value != ''  || form.elements[key].value != null) {
            formDataPy[key] = form.elements[key].value;
            // formDataPy[key] = JSON.stringify(form.elements[key].value);
        }

    }
    eel.value_py(formDataPy);
    // eel.value_py(form.elements);
    console.log(formData);
}


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

// // Отслеживаем размер окна для настройки
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