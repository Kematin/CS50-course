export function displayEmail(emailId) {
	// Show the mailbox and hide other views
	document.querySelector("#emails-view").style.display = "none";
	document.querySelector("#compose-view").style.display = "none";
	document.querySelector("#displayMessage").style.display = "none";
	document.querySelector("#email-view").style.display = "block";

	const emailView = document.querySelector("#email-view");
	getInfoFromApi(emailId).then((mailElement) => {
		emailView.innerHTML = "";
		emailView.append(mailElement);
	});
}

async function getInfoFromApi(id) {
	const response = await fetch(`/emails/${id}`);
	const email = await response.json();
	const mailElement = createMailDOM(email);
	return mailElement;
}

function createMailDOM(email) {
	const bodySection = document.createElement("div");
	bodySection.innerHTML = email.body;
	const infoSection = createInfoSection(email);

	const section = document.createElement("div");
	section.append(infoSection);
	section.append(bodySection);
	return section;
}

function createInfoSection(email) {
	const infoSection = document.createElement("div");

	const fromField = document.createElement("p");
	fromField.innerHTML = `<b>From:</b> ${email.sender}`;
	infoSection.append(fromField);

	const toField = document.createElement("p");
	toField.innerHTML = `<b>To:</b> ${email.recipients}`;
	infoSection.append(toField);

	const subjectField = document.createElement("p");
	subjectField.innerHTML = `<b>Subject:</b> ${email.subject}`;
	infoSection.append(subjectField);

	const timeField = document.createElement("p");
	timeField.innerHTML = `<b>Timestamp:</b> ${email.timestamp}`;
	infoSection.append(timeField);

	const replyButton = createButtonReply();
	infoSection.append(replyButton);

	infoSection.append(document.createElement("hr"));
	return infoSection;
}

function createButtonReply() {
	let buttonReply = document.createElement("button");
	buttonReply.className = "btn btn-sm btn-outline-primary";
	buttonReply.innerHTML = "Reply";
	return buttonReply;
}

function buttonArchive() {}
