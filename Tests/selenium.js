function count() {
  let counter = 0;

  num = document.querySelector("h1");
  increaseBtn = document.querySelector("#increase");
  decraseBtn = document.querySelector("#decrease");

  increaseBtn.onclick = () => {
    counter++;
    num.innerHTML = counter;
  };

  decraseBtn.onclick = () => {
    counter--;
    num.innerHTML = counter;
  };
}

document.addEventListener("DOMContentLoaded", count);
