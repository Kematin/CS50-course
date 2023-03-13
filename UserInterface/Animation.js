function playAnimation(element) {
    if (element.style.animationPlayState === "paused") {
        element.style.animationPlayState = "running";
    }
    else {
        element.style.animationPlayState = "paused";
    }
}

document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("#animation").onclick = () => {
        allHeaders = document.querySelectorAll("h1")
        allHeaders.forEach(header => {
            playAnimation(header)
        });
    }
})
