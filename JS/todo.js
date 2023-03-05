function disabledSubmit (newTask, submit) {
    if (newTask.value.length > 0) {
        submit.disabled = false
    }
    else {
        submit.disabled = true
    };
};

function addTask (newTask, submit) {
    // find ul list of tasks_elemets
    const tasks_element = document.querySelector("#tasks");
    // create li element for list
    const new_element = document.createElement("li");

    const task = newTask.value; 

    // append new element in list
    new_element.innerHTML = task;
    tasks_element.append(new_element);

    // reset new task input value and disabled submit input
    newTask.value = "";
    submit.disabled = false;
};

document.addEventListener("DOMContentLoaded", () => {
    // Find new task input and submit input
    const newTask = document.querySelector("#task");
    const submit = document.querySelector("#submit");

    // Setup function disableSubmit on onkeyup atribute
    newTask.onkeyup = () => {
        disabledSubmit(newTask, submit)
        return false
    };

    // Find form
    form = document.querySelector("form");

    // Setup function addTask on onsubmit atribute
    form.onsubmit = () => {
        addTask(newTask, submit)
        return false
    };
});
