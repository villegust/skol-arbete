const express = require("express");
const bodyParser = require("body-parser");
const app = express();
const http = require("http").Server(app);
const io = require("socket.io")(http);
const mongoose = require("mongoose");
const { sendStatus } = require("express/lib/response");

app.use(express.static("./hemsida"));

app.use(bodyParser.urlencoded({extended: false}));

const dbUrl = "mongodb+srv://nti:@cluster0.asirz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

var Messages = mongoose.model("Message", {
    name: String,
    message: String
});

app.get("/meddelanden", (req, res) => {
    Messages.find({}, (err, messages) => {
        res.send(messages);
    });
});

var messages = []

app.post("/meddelanden", (req, res) => {
    
    var message = new Messages(req.body);

    message.save((err) => {
        if(err){
            sendStatus(500);
        }
        messages.push(req.body);
        io.emit("message", req.body);
        res.sendStatus(200);
    })
});


io.on("connection", (socket) => {
    console.log("En användare anslöt");
});

mongoose.connect(dbUrl, (err) => {
    console.log("Mongodb connection", err, "errors");
});

http.listen(3000, () => {
    console.log("Servern är igång, besök den på http://localhost:3000 ")
}); 