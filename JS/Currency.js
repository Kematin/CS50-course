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
    let myHeaders = new Headers();
    myHeaders.append("apikey", "0EmyLsVxix2jYrFPx6CFCd6MdVhseXjf");

    let requestOptions = {
      method: 'GET',
      redirect: 'follow',
      headers: myHeaders
    };

    let url = `https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=${currencyName}&amount=1`

    fetch(url, requestOptions)
        .then(response => response.json())
        .then(data => {
            const result = data.result
            displayElement(currencyName, result)            
          })
}


function displayElement(currencyName, data) {
    let displayDiv = document.querySelector("#displayValue");
    if (data === undefined) {
        displayDiv.innerHTML = "Invalid Currency Name.";
    }
    else {
        displayDiv.innerHTML = `1 ${currencyName} is equal to ${data.toFixed(2)} RUB`;
    }
}


function CurrencyExchange() {
    const inputName = document.querySelector("#currency");
    const currencyName = inputName.value.toUpperCase();

    callApi(currencyName);

    // disable autorefresh page
    return false
}


document.addEventListener("DOMContentLoaded", () => {
    submit = document.querySelector("#submit");
    inputName = document.querySelector("#currency");

    inputName.onkeyup = () => {
        disableSubmit(inputName, submit);
    }

    form = document.querySelector("form");
    form.onsubmit = CurrencyExchange;
})
