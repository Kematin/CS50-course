import { getIsLikedValue } from "./changeLikes.js";

export function displayPosts() {
  clearPosts();
  getPosts();
}

function clearPosts() {
  let allPosts = document.querySelector("#displayPosts");
  allPosts.innerHTML = "";
}

async function getPosts() {
  const posts = await getJsonData();
  let allPosts = document.querySelector("#displayPosts");
  Object.values(posts).forEach((post) => {
    createPostElements(post, allPosts);
  });
}

function createPostElements(post, allPostsSection) {
  let newPost = document.createElement("div");
  newPost.id = post.id;
  newPost.className = "post";
  addContentForPost(newPost, post);
  allPostsSection.append(newPost);
}

function addContentForPost(newPost, post) {
  addElementForPost(newPost, "h4", post.creator, "creator");
  addHrefForPost(newPost);
  addElementForPost(newPost, "p", post.content, "content");
  addElementForPost(newPost, "p", post.datetime, "datetime");
  addElementForPost(newPost, "p", `Likes: ${post.likes}`, "likes");
  addChangeLikeButtonForPost(newPost, post.id);
  addDeleteButtonForPost(newPost);
  addCommentsForPost(newPost, post.comments, "comments");
}

function addHrefForPost(post) {
  let editUrl = document.createElement("a");
  editUrl.innerHTML = "Edit";
  editUrl.href = "";
  editUrl.className = "edit";
  post.append(editUrl);
}

async function addChangeLikeButtonForPost(postElement, postId) {
  let button = document.createElement("img");
  button.className = "changeLike";
  const isLiked = await getIsLikedValue(postId);
  if (isLiked) {
    button.src = "/static/images/liked.png";
  } else {
    button.src = "/static/images/unliked.png";
  }
  postElement.append(button);
}

function addDeleteButtonForPost(post) {
  let button = document.createElement("button");
  button.className = "deletePost";
  button.innerHTML = "Delete";
  post.append(button);
}

function addCommentsForPost(post, comments) {
  let commentsSection = document.createElement("div");
  commentsSection.className = "comments";
  commentsSection.innerHTML = "Comments:";
  comments.forEach((comment) => {
    const creator = comment.creator;
    const content = comment.comment;
    const newComment = document.createElement("p");
    newComment.innerHTML = `<b>${creator}</b>: ${content}`;
    commentsSection.appendChild(newComment);
  });

  if (comments.length === 0) {
    commentsSection.innerHTML = "No comments.";
  }

  post.append(commentsSection);
}

function addElementForPost(post, tag, content, className) {
  let newElement = document.createElement(tag);
  newElement.innerHTML = content;
  newElement.className = className;
  post.append(newElement);
}

async function getJsonData() {
  const response = await fetch("/api/posts");
  const data = await response.json();
  return data;
}
