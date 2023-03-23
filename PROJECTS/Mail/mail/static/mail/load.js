import { displayEmail } from "./email.js";

export function loadMailbox(mailbox) {
	// Show the mailbox and hide other views
	document.querySelector("#emails-view").style.display = "block";
	document.querySelector("#compose-view").style.display = "none";
	document.querySelector("#displayMessage").style.display = "none";
	document.querySelector("#email-view").style.display = "none";

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
		// Create new elements
		const sender = createElementEmail("sender", "p", `${email.sender}:`);
		const subject = createElementEmail("subject", "p", email.subject);
		const timestamp = createElementEmail("timestamp", "p", email.timestamp);

		let emailDOM = document.createElement("div");
		emailDOM.className = "email";

		emailDOM.append(sender);
		emailDOM.append(subject);
		emailDOM.append(timestamp);

		if (email.read === true) {
			emailDOM.style.backgroundColor = "#e8e2e1";
		}

		arrayEmails.push(emailDOM);
	});

	return arrayEmails;
}

function createElementEmail(name, type, inner) {
	let newElement = document.createElement(type);
	newElement.className = name;
	newElement.innerHTML = inner;
    newElement.addEventListener("click", displayEmail) 
	return newElement;
}
