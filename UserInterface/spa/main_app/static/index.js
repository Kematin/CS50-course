function showPage(pageNum) {
	disablePages();
	activePage = document.querySelector(`#page${pageNum}`);
	activePage.style.display = "block";

	fetch(`/section/${pageNum}`)
		.then((response) => response.text())
		.then((text) => {
			newP = document.querySelector(`#text${pageNum}`);
			newP.innerHTML = text;
			activePage.append(newP);
		});
}

function disablePages() {
	pages = document.querySelectorAll(".pages");
	pages.forEach((page) => {
		page.style.display = "none";
	});
}

document.addEventListener("DOMContentLoaded", () => {
	showPage("1");

	buttonsChangePage = document.querySelectorAll("button");
	buttonsChangePage.forEach((button) => {
		button.onclick = function () {
			page = this.dataset.page;
			showPage(page);
		};
	});
});
