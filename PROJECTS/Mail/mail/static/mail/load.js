export function loadMailbox(mailbox) {
	// Show the mailbox and hide other views
	document.querySelector("#emails-view").style.display = "block";
	document.querySelector("#compose-view").style.display = "none";
	document.querySelector("#displayMessage").style.display = "none";

	const emailView = document.querySelector("#emails-view");
	emailView.innerHTML = `<h3>${
		mailbox.charAt(0).toUpperCase() + mailbox.slice(1)
	}</h3>`;

	getArrayEmails(mailbox).then((emails) => {
		emails.forEach((email) => {
			emailView.append(email);
		});
	});
}

async function getArrayEmails(mailbox) {
	const data = await getInfoFromApi(mailbox);
	const emails = createArrayEmails(data);
	return emails;
}

async function getInfoFromApi(mailbox) {
	const response = await fetch(`/emails/${mailbox}`);
	const emails = await response.json();
	return emails;
}

function createArrayEmails(data) {
	let arrayEmails = [];

	data.forEach((email) => {
		const content = email.body;
		let emailDOM = document.createElement("div");

		emailDOM.innerHTML = content;
		arrayEmails.push(emailDOM);
	});

	return arrayEmails;
}
