function newPost(form) {
  const content = form.querySelector("textarea").value;
  fetch("/api/new", {
    method: "POST",
    body: JSON.stringify({
      content: content,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(response.statusText);
      }
      return response.json();
    })
    .then((data) => {
      // TODO Handle succesfull
      console.log(data.message);
    })
    .catch((error) => {
      // TODO Handle error
      console.error(error);
    });
}

function displayMessage(message) {}

document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("#sendPostForm");
  form.onsubmit = () => {
    newPost(form);
    return false;
  };
});
