export function loadMailbox(mailbox) {
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
