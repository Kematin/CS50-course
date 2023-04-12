let counter = 0;
function count() {
    const header = document.querySelector("h1");
    counter++;
    header.innerHTML = counter;
    if (counter % 10 === 0) {
        alert(`Count is now ${counter}`)
    }
}

<!-- This code will not working, bcs js render script before render button -->
<!-- document.querySelector('button').onclick = count; -->

document.addEventListener("DOMContentLoaded", function() {
    // This will render if page load
    document.querySelector('button').onclick = count;
});


function hello() {
    // Take value of input with id name
    const name = document.querySelector("#name").value;
    alert(`Hello ${name}!`);
}

document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('form').onsubmit = hello 
});

