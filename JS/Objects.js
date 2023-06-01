var model = {
    name: "Koohan-3000",
    version: 5.2,
    cost: 5,
}

function createLiElement(list, info) {
    newElement = document.createElement("li");
    newElement.innerHTML = info;
    list.append(newElement)
}


document.addEventListener("DOMContentLoaded", () => {
    listModel = document.querySelector("#list");

    // Get info from objects
    name = model.name;
    version = model["version"];
    cost = model.cost;
    
    // Create array with info
    infoModel = [name, version, cost];

    // In for loop create li elements
    for (let i in infoModel) {
        createLiElement(listModel, infoModel[i]) ;
    }
})
