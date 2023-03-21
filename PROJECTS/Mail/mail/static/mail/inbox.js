import { composeEmail } from './compose.js';
import { loadMailbox } from './load.js';

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


