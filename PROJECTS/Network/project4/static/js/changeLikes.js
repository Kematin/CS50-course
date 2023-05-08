export function listenerLikes() {
  const postContainer = document.querySelector("#displayPosts");
  postContainer.addEventListener("click", (event) => {
    if (event.target.tagName === "IMG") {
      let parentNode = event.target.parentNode;
      const postId = parentNode.id;
      putApi(postId);
      changeLike(parentNode, true);
    }
  });
}

function changeLike(parentNode, isLiked) {
  let likesContent = parentNode.querySelector(".likes").innerHTML;
  let likes = parseInt(likesContent.match(/\d+/)[0]);

  if (isLiked) {
    likes += 1;
  } else {
    likes -= 1;
  }

  parentNode.querySelector(".likes").innerHTML = `Likes: ${likes}`;
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
