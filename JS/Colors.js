function changeColor (button) {
    button.onclick = () => {
        // Take color by color dataset atribute in button tag and change style in hello
        document.querySelector("#hello").style.color = button.dataset.color;
    };
};

function logArray (array) {
    console.log(array)
    console.log(`Length: ${array.length}`)
};

document.addEventListener("DOMContentLoaded", () => {
    // Find all elements with tag button and save their in Node List (array)
    buttonArray = document.querySelectorAll("button")
    logArray(buttonArray)

    // Method forEach passes through each item in the list and call anonymous function, which take button as argument
    // Anonymous function call changeColor function, which change color
    buttonArray.forEach((button) => {
        changeColor(button)
    });
});
