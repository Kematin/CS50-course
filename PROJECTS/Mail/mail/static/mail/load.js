export function loadMailbox(mailbox) {
	// Show the mailbox and hide other views
	document.querySelector("#emails-view").style.display = "block";
	document.querySelector("#compose-view").style.display = "none";
	document.querySelector("#displayMessage").style.display = "none";

	const templateData = getDOMTemplate(mailbox);
	document.querySelector("#emails-view").innerHTML = templateData;
}

function getDOMTemplate(mailbox) {
	const data = getInfoFromApi(mailbox);
	const template = createDOMTemplate(data, mailbox);
	return template;
}

function getInfoFromApi(mailbox) {
	fetch(`/emails/${mailbox}`)
		.then((response) => response.json())
		.then((emails) => {
			return emails;
		});
}

function createDOMTemplate(data, mailbox) {
	const content = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
	return content;
}
