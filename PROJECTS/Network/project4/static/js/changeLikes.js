export function listenerLikes() {
  const changeLikeButton = document.querySelector(".changeLike");
  changeLikeButton.addEventListener("click", changeLike);
}

function changeLike() {
  const postId = 12;
  putApi(postId);
}

function putApi(postId) {
  fetch(`api/likes/${postId}`, {
    method: "PUT",
    // TODO set value for like - or like +
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

// TODO
function checkClicked() {}
