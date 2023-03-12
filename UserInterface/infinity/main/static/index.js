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
		.then(data => {
            // in forEach loop create posts
            data.posts.forEach(createPost);
		});
}


function createPost(content) {
    const newPost = document.createElement("div");
    newPost.className = "post";
    newPost.innerHTML = content;

    document.querySelector("#posts").append(newPost);
}


