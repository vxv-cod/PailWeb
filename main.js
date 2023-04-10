async function create_cur_for_rub (){
    let value_rub = document.getElementById("Otmetka_verha").value;
    await eel.value_py(value_rub)
    
    // получаем список всех input'ов в таблице 1
    let list_curs = document.getSelection('td');
    await eel.value_py(list_curs);
    for (let div_cur of list_curs) {
        await eel.value_py(div_cur.value);

        // теперь передает значение в Python для обработки
        let name_cur = div_cur.getElementsByTagName("label")[0].textContent;
        // let name_cur = div_cur.getElementById("Otmetka_verha").value;
        // await eel.value_py(name_cur);
        // let inputxxx = div_cur.getElementsByTagName("label").children
        await eel.value_py(name_cur);


        // выводим на экран полученное значение
        // div_cur.getElementsByTagName("input")[0].value = value_cur;
    // }
    
}}


document.getElementById("submit").onclick = create_cur_for_rub;


// let btn = document.querySelector("#submit");
// btn.addEventListener("click", sendData);


// async function sendData() {
//     let value = document.querySelector("#Otmetka_verha").value;
//     await eel.value_py(value);
//     console.log(value);
// }

