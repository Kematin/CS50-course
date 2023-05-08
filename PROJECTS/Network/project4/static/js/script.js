import { displayPosts } from "./posts.js";
import { listenerForm } from "./newPost.js";
import { listenerLikes } from "./changeLikes.js";

document.addEventListener("DOMContentLoaded", () => {
  displayPosts();
  listenerForm();
  listenerLikes();
});
