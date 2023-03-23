export function displayEmail() {
    // Show the mailbox and hide other views
	document.querySelector("#emails-view").style.display = "none";
	document.querySelector("#compose-view").style.display = "none";
	document.querySelector("#displayMessage").style.display = "none";
	document.querySelector("#email-view").style.display = "block";

    console.log("Mail!")
}
