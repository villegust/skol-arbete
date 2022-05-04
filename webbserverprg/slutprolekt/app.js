const express = require("express");
const mongoose = require("mongoose");
const authRoutes = require("./routes/authRoutes");
const cookieParser = require("cookie-parser");
const {requireAuth, checkUser} = require("./middleware/authMiddleware");


const app = express();


// middleware
app.use(express.static("public"));
app.use(express.json());
app.use(cookieParser());

// view engine
app.set("view engine", "ejs");

// databas anslutningen
const dbURI = "mongodb+srv://new-user12:qwerty123456@cluster0.8z293.mongodb.net/node-auth";

//sätter upp en port på datorn som servern körs på
app.listen(3000, () => {
  console.log("Server är igång");
});

//ett error om mongoDB inte ansluter.
mongoose.connect(dbURI, (err) => {
    if (err) {
        throw err;
    }
    else {
      console.log("mongoDB ansluten");
    }
      
})
// routes
// "*" betyder att jag kommer att applicera koden till alla routs
// requireAuth gör att man måste vara inloggad för att kunna se sidan.
app.get("*", checkUser);
app.get("/", (req, res) => res.render("index"));
app.get("/", requireAuth, (req, res) => res.render("index"));
app.get("/otherSide", requireAuth, (req, res) => res.render("otherSide"));
app.get("/profile", requireAuth, (req, res) => res.render("profile"));
app.get("/editProfile", requireAuth, (req, res) => res.render("editProfile"));
app.use(authRoutes);
