var socket = io();

$(() => {
    $("#send").click(() => {
        var message = {name : $("#name").val(), message: $("#message").val()};
        postMessages(message);
    });
    getMessages();
});

socket.on("message", addMessages)

function addMessages(message){
    $("#messages").append(`<h4> ${message.name} </h4> <p> ${message.message} </p>`)
}

function getMessages(){
    $.get("http://localhost:3000/meddelanden", (data) => {
        data.forEach(addMessages);
    });
}

function postMessages(message){
    $.post("http://localhost:3000/meddelanden", message);
}