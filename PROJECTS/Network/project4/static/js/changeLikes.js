export function listenerLikes() {
  const postContainer = document.querySelector("#displayPosts");
  postContainer.addEventListener("click", (event) => {
    if (event.target.tagName === "IMG") {
      let parentNode = event.target.parentNode;
      const postId = parentNode.id;
      putApi(postId);
      changeLike(parentNode, postId);
    }
  });
}

async function changeLike(parentNode, postId) {
  const isLiked = await getIsLiked(postId);

  let likesContent = parentNode.querySelector(".likes").innerHTML;
  let likes = parseInt(likesContent.match(/\d+/)[0]);

  if (isLiked) {
    const src = "/static/images/unliked.png";
    changeLikeIcon(parentNode, src);
    likes -= 1;
  } else {
    const src = "/static/images/liked.png";
    changeLikeIcon(parentNode, src);
    likes += 1;
  }

  parentNode.querySelector(".likes").innerHTML = `Likes: ${likes}`;
}

function changeLikeIcon(parentNode, src) {
  let buttonLike = parentNode.querySelector(".changeLike");
  buttonLike.src = src;
}

async function putApi(postId) {
  const username = document.querySelector("#username").innerHTML;
  const isLiked = await getIsLiked(postId);

  fetch(`api/likes/${postId}`, {
    method: "PUT",
    body: JSON.stringify({
      isLiked: isLiked,
      username: username,
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

async function getIsLiked(postId) {
  const username = document.querySelector("#username").innerHTML;
  const data = await getApi(username);
  const idLikedPosts = data.liked;

  if (idLikedPosts.includes(parseInt(postId))) {
    return true;
  } else {
    return false;
  }
}

async function getApi(username) {
  const response = await fetch(`/api/liked/${username}`);
  const data = await response.json();
  return data;
}

// TODO
function checkLiked() {}
