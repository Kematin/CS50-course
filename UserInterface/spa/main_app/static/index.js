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

function disablepages() {
	pages = document.queryselectorall(".pages");
	pages.foreach((page) => {
		page.style.display = "none";
	});
}

document.addeventlistener("domcontentloaded", () => {
	showpage("1");

	buttonschangepage = document.queryselectorall("button");
	buttonschangepage.foreach((button) => {
		button.onclick = function () {
			page = this.dataset.page;
			showpage(page);
		};
	});
});
