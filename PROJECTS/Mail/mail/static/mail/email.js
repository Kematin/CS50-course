import { composeEmail } from "./compose.js";

export function displayEmail(emailId) {
	// Show the mailbox and hide other views
	document.querySelector("#emails-view").style.display = "none";
	document.querySelector("#compose-view").style.display = "none";
	document.querySelector("#displayMessage").style.display = "none";
	document.querySelector("#email-view").style.display = "block";

	// Setup email as readen
	setupReadenEmail(emailId);

	const emailView = document.querySelector("#email-view");
	getInfoFromApi(emailId).then((mailElement) => {
		emailView.innerHTML = "";
		emailView.append(mailElement);
	});
}

function setupReadenEmail(id) {
	fetch(`/emails/${id}`, {
		method: "PUT",
		body: JSON.stringify({
			read: true,
		}),
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

	const buttons = document.createElement("div");
	buttons.append(createButtonReply(email.sender, email.subject));
	buttons.append(createButtonArchive(email.archived, email.id));
	infoSection.append(buttons);

	infoSection.append(document.createElement("hr"));
	return infoSection;
}

function createButtonReply(sender, subject) {
	let buttonReply = document.createElement("button");

	buttonReply.className = "btn btn-sm btn-outline-primary";
	buttonReply.innerHTML = "Reply";
	buttonReply.addEventListener("click", () => {
		reply(sender, subject);
	});

	return buttonReply;
}

function createButtonArchive(isArchive, id) {
	let buttonArchive = document.createElement("button");
	buttonArchive.className = "btn btn-sm btn-outline-primary";

	changeArchiveButtonName(buttonArchive, isArchive);

	buttonArchive.addEventListener("click", () => {
		isArchive = !isArchive;
		archive(isArchive, id);
		changeArchiveButtonName(buttonArchive, isArchive);
	});

	return buttonArchive;
}

function reply(sender, subject) {
	composeEmail();
    console.log("Compose!")
    const inputRecipients = document.querySelector("#compose-recipients");
    const inputSubject = document.querySelector("#compose-subject");
	inputRecipients.value = sender;
	inputSubject.value = `Re: ${subject}`;
}

function archive(changeArchive, id) {
	fetch(`/emails/${id}`, {
		method: "PUT",
		body: JSON.stringify({
			archived: changeArchive,
		}),
	});
}

function changeArchiveButtonName(button, isArchive) {
	if (isArchive === true) {
		button.innerHTML = "Unarchive";
	} else {
		button.innerHTML = "Archive";
	}
}
