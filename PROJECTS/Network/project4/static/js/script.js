import { listenerForm } from "./newPost";
import { listenerLikes } from "./changeLikes";

document.addEventListener("DOMContentLoaded", () => {
  listenerForm();
  listenerLikes();
});
