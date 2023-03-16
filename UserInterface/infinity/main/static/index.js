// -------------------------------------------- REALIZIATION OF INFINITE SCROLL -----------------------------------------

let counter = 1;

// How many posts will be get from server
const quantity = 15;

// Setup function on scroll
window.onscroll = checkBottomPage;
document.addEventListener("DOMContentLoaded", load);

function checkBottomPage() {
	if (window.scrollY + window.innerHeight >= document.body.offsetHeight) {
		load();
	}
}

function load() {
	start = counter;
	end = start + quantity - 1;
	counter = end + 1;

	// Get data from server and put in json
	fetch(`/posts?start=${start}&end=${end}`)
		.then((response) => response.json())
		.then((data) => {
			// in forEach loop create posts
			data.posts.forEach(createPost);
		});
}

function createPost(content) {
	const newPost = document.createElement("div");
	newPost.className = "post";

	hideContent = "<button class='hide'>Hide</button>";
	newPost.innerHTML = `${content} ${hideContent}`;

	document.querySelector("#posts").append(newPost);
}

// -------------------------------------------- ANIMATION DELETE -----------------------------------------

function hide(element) {
	// Check if the user clicked on a hide button
	if (element.className === "hide") {
		// Change style for post (Post is parent element)
		element.parentElement.style.animationPlayState = "running";
		element.parentElement.addEventListener("animationend", () => {
			// Delete them, when animation end
			element.parentElement.remove();
		});
	}
}

document.addEventListener("click", (event) => {
	// Get elemenet from target
	element = event.target;
	// Call function for delete element
	hide(element);
});
