export function displayPosts() {
  getPosts();
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
  addElementForPost(newPost, "h4", post.creator);
  addHrefForPost(newPost);
  addElementForPost(newPost, "p", post.content);
  addElementForPost(newPost, "p", post.datetime);
  addElementForPost(newPost, "p", `Likes: ${post.likes}`);
  addButtonForPost(newPost);
  addCommentsForPost(newPost, post.comments);
}

function addHrefForPost(post) {
  let editUrl = document.createElement("a");
  editUrl.innerHTML = "Edit";
  editUrl.href = "";
  post.append(editUrl);
}

function addButtonForPost(post) {
  let button = document.createElement("button");
  button.className = "changeLike";
  button.innerHTML = "Like";
  post.append(button);
}

function addCommentsForPost(post, comments) {
  console.log(comments);
}

function addElementForPost(post, tag, content) {
  let newElement = document.createElement(tag);
  newElement.innerHTML = content;
  post.append(newElement);
}

async function getJsonData() {
  const response = await fetch("/api/posts");
  const data = await response.json();
  return data;
}
