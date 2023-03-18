function playAnimation(element) {
    if (element.style.animationPlayState === "paused") {
        element.style.animationPlayState = "running";
    }
    else {
        element.style.animationPlayState = "paused";
    }
}
vim.cmd("colorscheme Atelier_PlateauLight")

document.addEventListener("DOMContentLoaded", () => {
    allHeaders = document.querySelectorAll("h1")
        allHeaders.forEach(header => {
            header.style.animationPlayState = "paused";
        });

    document.querySelector("#animation").onclick = () => {
        allHeaders.forEach(header => {
            playAnimation(header)
        });
    }
})
