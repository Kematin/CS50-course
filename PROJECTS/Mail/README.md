# Mail

Front-end для почтового клиента, который выполняет вызовы
API для отправки и получения электронной почты.

Техническое задание в [specification.md](specification.md), 
или на [сайте cs50](https://cs50.harvard.edu/web/2020/projects/3/mail/#specification)

![Main Page](https://cs50.harvard.edu/web/2020/projects/3/images/inbox.png)
![Inbox](https://cs50.harvard.edu/web/2020/projects/3/images/email.png)

## Cборка

1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py runserver

## API документация (CS50)

- GET Emails
- GET Email
- POST Create email
- PUT Change email

### GET /emails/<str:mailbox>

Mailbox: inbox, sent, archive

**Response:**

```json
[
	{
		"id": 100,
		"sender": "foo@example.com",
		"recipients": ["bar@example.com"],
		"subject": "Hello!",
		"body": "Hello, world!",
		"timestamp": "Jan 2 2020, 12:00 AM",
		"read": false,
		"archived": false
	},
	{
		"id": 95,
		"sender": "baz@example.com",
		"recipients": ["bar@example.com"],
		"subject": "Meeting Tomorrow",
		"body": "What time are we meeting?",
		"timestamp": "Jan 1 2020, 12:00 AM",
		"read": true,
		"archived": false
	}
]
```

**Example js:**

```js
// Show the mailbox name
fetch("/emails/inbox")
	.then((response) => response.json())
	.then((emails) => {
		// Print emails
		console.log(emails);

		// ... do something else with emails ...
	});
```

<br>

### GET /emails/<int:email_id>

**Response:**

```json
{
	"id": 100,
	"sender": "foo@example.com",
	"recipients": ["bar@example.com"],
	"subject": "Hello!",
	"body": "Hello, world!",
	"timestamp": "Jan 2 2020, 12:00 AM",
	"read": false,
	"archived": false
}
```

**Example js:**

```js
// Show the mailbox name
fetch("/emails/1")
	.then((response) => response.json())
	.then((email) => {
		// Print email
		console.log(email);

		// ... do something else with email ...
	});
```

### POST /emails

**Response:**

```json
Success:
{
    "message": "Email sent successfully.",
    status: 201
}

Errors:
{
    "error": "At least one recipient required.",
    status: 400
}

{
    "error": "POST request required.",
    status: 400
}

{
    "error": "User with email baz@example.com does not exist.",
    status: 400
}
```

**Example js:**

```
fetch('/emails', {
  method: 'POST',
  body: JSON.stringify({
      recipients: 'baz@example.com',
      subject: 'Meeting time',
      body: 'How about we meet tomorrow at 3pm?'
  })
})
.then(response => response.json())
.then(result => {
    // Print result
    console.log(result);
});
```

### PUT /emails/<int:email_id>

**Example js:**

```js
fetch("/emails/100", {
	method: "PUT",
	body: JSON.stringify({
		archived: true,
	}),
});
```
