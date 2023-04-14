


// Отслеживание нажатие кнопки
let btn = document.querySelector("#submit");
btn.addEventListener("click", sendData);


function sendData() {
    let el = document.getElementById('my-docx-content');
    content = '<button type="submit" id="submit2" >OOOOOOOOOOOOOOOOOOOO</button>'
    el.innerHTML  = content;


    
    // formData['my-docx-content'] = content;
    // LS.setItem('formData', JSON.stringify(formData));
    // eel.printpy('formData = ', formData);
    

}

// Отслеживание нажатие кнопки
let btn2 = document.querySelector("#Replace_text");
btn2.addEventListener("click", replacefun);

function replacefun() {
    text = '55555555555555555555555555';
    // document.getElementById('my-docx-content').innerHTML = text;
    let eee = document.getElementById('my-docx-content');
    eee.innerHTML = text;
}