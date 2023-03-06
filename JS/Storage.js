// ----------------------------------------------------------------------------------------------------------------
function setLocalStorageColor(element) {
    // Get color from local storage
    const color = localStorage.getItem("color");

    // Change header color
    element.style.color = color;
    element.innerHTML = color;
}


function changeColor(element, color) {
    // Change header color
    element.style.color = color;
    element.innerHTML = color;

    // Setup header color into local storage
    localStorage.setItem("color", color);
}


function FirstExample() {
    // Get header
    const header = document.querySelector("#color");

    // Setup color from local storage into header
    setLocalStorageColor(header);

    select = document.querySelector("select");
    select.onchange = function() {
        // Get new color from choosen option
        const color = this.value;
        changeColor(header, color);
    }
}
// ----------------------------------------------------------------------------------------------------------------


// ----------------------------------------------------------------------------------------------------------------

// Check existance of counter in local storage
if (!localStorage.getItem("counter")) {

    // Save 0 in storage if counter not exist
    localStorage.setItem("counter", 0);
}

function setupFirstCounter() {
    const header = document.querySelector("#num");
    const counter = localStorage.getItem("counter");

    header.innerHTML = counter;
}

function countPlus() {
    let counter = localStorage.getItem("counter");
    counter++;

    const header = document.querySelector("#num");
    header.innerHTML = counter;

    localStorage.setItem("counter", counter);
}

function countMinus() {
    let counter = localStorage.getItem("counter");
    counter--;

    const header = document.querySelector("#num");
    header.innerHTML = counter;

    localStorage.setItem("counter", counter);
}

function SecondExample() {
    setupFirstCounter()

    const buttonPlus = document.querySelector("#plus");
    const buttonMinus = document.querySelector("#minus");

    buttonPlus.onclick = countPlus;
    buttonMinus.onclick = countMinus;
}
// ----------------------------------------------------------------------------------------------------------------

document.addEventListener("DOMContentLoaded", () => {
    FirstExample();
    SecondExample();
})
