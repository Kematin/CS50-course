export function composeEmail() {
	// Show compose view and hide other views
	document.querySelector("#emails-view").style.display = "none";
	document.querySelector("#displayMessage").style.display = "none";
	document.querySelector("#email-view").style.display = "none";
	document.querySelector("#compose-view").style.display = "block";

	// Clear out composition fields
	document.querySelector("#compose-recipients").value = "";
	document.querySelector("#compose-subject").value = "";
	document.querySelector("#compose-body").value = "";

	const form = document.querySelector("#compose-form");
	form.addEventListener("submit", (event) => {
		event.preventDefault();
		submitForm();
	});
}

function submitForm() {
	const inputData = {
		recipients: document.querySelector("#compose-recipients").value,
		subject: document.querySelector("#compose-subject").value,
		body: document.querySelector("#compose-body").value,
	};

	if (checkData(inputData) === false) {
		const errorMessage = "No input data!";
		displayErrorMessage(errorMessage);
	} else {
		sendEmail(inputData);
	}
}

function sendEmail(data) {
	fetch("/emails", {
		method: "POST",
		body: JSON.stringify({
			recipients: data.recipients,
			subject: data.subject,
			body: data.body,
		}),
	})
		.then((response) => {
			if (!response.ok) {
				return response.json().then((data) => {
					throw new Error(data.error);
				});
			}
			return response.json();
		})
		.then((result) => {
			displaySuccesMessage(result.message);
		})
		.catch((error) => {
			displayErrorMessage(error.message);
		});
}

function checkData(data) {
	let isValid = true;

	for (let prop in data) {
		if (data[prop].trim() === "") {
			isValid = false;
		}
	}

	return isValid;
}

function displayErrorMessage(message) {
	const displayError = document.querySelector("#displayMessage");

	displayError.innerHTML = message;
	displayError.style.display = "block";
	displayError.style.backgroundColor = "#ffe6e6";
	displayError.style.border = "1px solid #ff4d4d";
	displayError.style.color = "#ff4d4d";

	setTimeout(function () {
		displayError.style.display = "none";
	}, 8000);
}

function displaySuccesMessage(message) {
	const displaySuccess = document.querySelector("#displayMessage");

	displaySuccess.innerHTML = message;
	displaySuccess.style.display = "block";
	displaySuccess.style.backgroundColor = "#e7f5ea";
	displaySuccess.style.border = "1px solid #52c41a";
	displaySuccess.style.color = "#52c41a";

	setTimeout(function () {
		displaySuccess.style.display = "none";
	}, 8000);
}
