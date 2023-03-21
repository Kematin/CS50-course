document.addEventListener("DOMContentLoaded", function () {
	// Use buttons to toggle between views
	document
		.querySelector("#inbox")
		.addEventListener("click", () => loadMailbox("inbox"));
	document
		.querySelector("#sent")
		.addEventListener("click", () => loadMailbox("sent"));
	document
		.querySelector("#archived")
		.addEventListener("click", () => loadMailbox("archive"));

    // If compose button was clicked, display compose email
	document.querySelector("#compose").addEventListener("click", composeEmail);

	// By default, load the inbox
	loadMailbox("inbox");
});

function composeEmail() {
	// Show compose view and hide other views
	document.querySelector("#emails-view").style.display = "none";
	document.querySelector("#compose-view").style.display = "block";

	// Clear out composition fields
	document.querySelector("#compose-recipients").value = "";
	document.querySelector("#compose-subject").value = "";
	document.querySelector("#compose-body").value = "";
}

function loadMailbox(mailbox) {
	// Show the mailbox and hide other views
	document.querySelector("#emails-view").style.display = "block";
	document.querySelector("#compose-view").style.display = "none";

	const templateData = getDOMTemplate(mailbox);
	document.querySelector("#emails-view").innerHTML = templateData;
}

function getDOMTemplate(mailbox) {
	return `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
}

function getInfoFromApi(mailbox) {
	// Show the mailbox name
	fetch(`/emails/${mailbox}`)
		.then((response) => response.json())
		.then((emails) => {
			// Print emails
			console.log(emails);
		});
}

function createDOMTemplate(data) {}
