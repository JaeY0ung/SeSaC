function cal(i){
    let sum = document.getElementById('sum');
    sum.placeholder = parseInt(sum.placeholder) + i;

    let sum2 = document.getElementById('sum2');
    sum2.innerText = parseInt(sum2.innerText) + i;
}