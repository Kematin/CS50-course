import { displayPosts } from "./posts.js";

export function listenerDelete() {
  const deleteButtons = document.querySelectorAll(".deletePost");
  deleteButtons.forEach((button) => {
    button.addEventListener("click", (event) => {
      let parentNode = event.target.parentNode;
      const postId = parentNode.id;
      deletePostApi(postId);
      setTimeout(displayPosts, 500);
    });
  });
}

function deletePostApi(postId) {
  fetch(`api/delete_post/${postId}`, {
    method: "DELETE",
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
