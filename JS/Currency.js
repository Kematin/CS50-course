function disableSubmit(input, submit) {
    len = input.value.length
    if (len > 0) {
        submit.disabled = false
    }
    else {
        submit.disabled = true
    }
}


function callApi(currencyName) {
    // Create headers
    let myHeaders = new Headers();
    myHeaders.append("apikey", "0EmyLsVxix2jYrFPx6CFCd6MdVhseXjf");

    // Create options for request
    let requestOptions = {
      method: 'GET',
      redirect: 'follow',
      headers: myHeaders
    };

    // Base url
    let url = `https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=${currencyName}&amount=1`

    // Send get request to url with options
    fetch(url, requestOptions)

    // Format response to json format
    .then(response => response.json())

    // Get data and put its to displayElement func
    .then(data => {
        const result = data.result
        displayElement(currencyName, result)            
      })
}


function displayElement(currencyName, data) {
    let displayDiv = document.querySelector("#displayValue");

    // Error display
    if (data === undefined) {
        displayDiv.innerHTML = "Invalid Currency Name.";
    }
    // Normal display
    else {
        displayDiv.innerHTML = `1 ${currencyName} is equal to ${data.toFixed(2)} RUB`;
    }
}


function CurrencyExchange() {
    // Get currency name from input
    const inputName = document.querySelector("#currency");
    const currencyName = inputName.value.toUpperCase();

    callApi(currencyName);

    // disable autorefresh page
    return false
}


document.addEventListener("DOMContentLoaded", () => {
    // Get inputs and form
    submit = document.querySelector("#submit");
    inputName = document.querySelector("#currency");
    form = document.querySelector("form");

    // Disable submit if length of input = 0
    inputName.onkeyup = () => {
        disableSubmit(inputName, submit);
    }

    form.onsubmit = CurrencyExchange;
})
