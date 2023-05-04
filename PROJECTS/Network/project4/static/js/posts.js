export function displayPosts() {
  getPosts();
}

```
<div class="post" id=12>
				<h4>Foo</h4>	
				<a href="">Edit</a>
				<p>Content</p>
				<p>March 29, 2023 10:40pm</p>
				<p>Icon likes</p>
				<div class="comments">
					<p>Comment 1</p>
					<p>Comment 2</p>
				</div>
				<button class="changeLike">Like +1</button>
			</div>
```;

function createPostElements(post, allPostsSection) {
  let newPost = document.createElement("div");
}

async function getPosts() {
  const posts = await getJsonData();
  let allPosts = document.querySelector("#displayPosts");
  Object.values(posts).forEach((post) => {
    createPostElements(post, allPosts);
  });
}

async function getJsonData() {
  const response = await fetch("/api/posts");
  const data = await response.json();
  return data;
}
