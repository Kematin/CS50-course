function checkBottomPage() {
	if (window.scrollY + window.innerHeight >= document.body.offsetHeight) {
		return true;
	} else {
		return false;
	}
}

function changeColor(section) {
	if (checkBottomPage() === true) {
		section.style.color = "green";
		section.innerHTML = "WOW YOU WAS IN THE BOTTOM OF PAGE!!!!";
	}
}

document.addEventListener("DOMContentLoaded", () => {
	body = document.querySelector("main");
	window.onscroll = () => {
		changeColor(body);
	};
});
