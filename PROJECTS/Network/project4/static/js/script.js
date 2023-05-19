import { displayPosts } from "./posts.js";
import { listenerForm } from "./newPost.js";
import { listenerLikes } from "./changeLikes.js";
import { listenerDelete } from "./deletePost.js";

document.addEventListener("DOMContentLoaded", () => {
  displayPosts();
  listenerForm();
  listenerLikes();
  setTimeout(listenerDelete, 500);
});
