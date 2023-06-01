function showPage(page) {
	disablePages();

	activePage = document.querySelector(`#${page}`);
	activePage.style.display = "block";
}

function disablePages() {
	pages = document.querySelectorAll(".pages");
	pages.forEach((page) => {
		page.style.display = "none";
	});
}

document.addEventListener("DOMContentLoaded", () => {
    showPage("page1")

	buttonsChangePage = document.querySelectorAll("button");
	buttonsChangePage.forEach((button) => {
		button.onclick = function () {
			page = this.dataset.page;
			showPage(page);
		};
	});
});
