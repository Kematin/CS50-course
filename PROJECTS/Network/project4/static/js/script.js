import { listenerForm } from "./newPost.js";
import { listenerLikes } from "./changeLikes.js";
import { displayPosts } from "./posts.js";

document.addEventListener("DOMContentLoaded", () => {
  displayPosts();
  listenerForm();
  listenerLikes();
});
