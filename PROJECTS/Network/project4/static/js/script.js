import { listenerForm } from "./newPost.js";
import { listenerLikes } from "./changeLikes.js";

document.addEventListener("DOMContentLoaded", () => {
  listenerForm();
  listenerLikes();
});
