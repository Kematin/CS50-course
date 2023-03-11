function checkBottomPage() {
    console.log(111)
	if (window.scrollY + window.innerHeight >= document.body.offsetHeight) {
		return true;
	} else {
		return false;
	}
}

let counter = 1;
const quantity = 15;

function load() {
	start = counter;
	end = start + quantity - 1;
    counter = end + 1

	fetch(`/posts?start=${start}&end=${end}`)
		.then((response) => response.json)
		.then((data) => {
            document.querySelector("#posts").innerHTML = data.posts
		});
}

document.addEventListener("DOMContentLoaded", () => {
	window.onscroll = () => {
		if (!checkBottomPage() === true) {
			load();
		}
	};
});
