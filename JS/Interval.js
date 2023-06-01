var tickTime = 1000
var count = 0;

function countNum () {
    count++;
    document.querySelector("#num").innerHTML = count;
}

function minusNum() {
    count = count - 10;
    if (count < 0) {
        count = 0
    };
    document.querySelector("#num").innerHTML = count;
}

function addSpeed() {
    tickTime = tickTime - 100;
    setInterval(countNum, tickTime);
}

document.addEventListener("DOMContentLoaded", function() {
    setInterval(countNum, tickTime);

    button_minus = document.querySelector("#count");
    button_speed = document.querySelector("#speed");

    button_minus.onclick = minusNum;
    button_speed.onclick = addSpeed;
})
