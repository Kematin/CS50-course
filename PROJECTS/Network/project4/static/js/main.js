function newPost(form) {
  const content = form.querySelector("textarea").value;
  fetch("/api/new", {
    method: "POST",
    body: JSON.stringify({
      content: content,
    }),
  });
}

document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("#sendPostForm");
  form.onsubmit = () => {
    newPost(form);
    return false;
  };
});
