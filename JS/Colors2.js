document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("select").onchange = function() {
        document.querySelector("#hello").style.color = this.value;
    };
});

