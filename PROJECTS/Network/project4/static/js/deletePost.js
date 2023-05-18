export function listenerDelete() {
  const deleteButtons = document.querySelectorAll(".deletePost");
  deleteButtons.forEach((button) => {
    button.addEventListener("click", deletePost);
  });
}

function deletePost() {}
