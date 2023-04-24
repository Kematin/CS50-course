export function listenerLikes() {
  console.log("Listen");
  const changeLikeButton = document.querySelector(".changeLike");
  console.log(changeLikeButton);
  changeLikeButton.addEventListener("click", changeLike);
}

function changeLike() {
  console.log("Change like");
  // TODO get id from div element
  const postId = 5;
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
