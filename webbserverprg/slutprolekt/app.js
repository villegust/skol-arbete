const express = require("express");
const mongoose = require("mongoose");
const authRoutes = require("./routes/authRoutes")

const app = express();

// middleware
app.use(express.static("public"));

// view engine
app.set("view engine", "ejs");

// database connection
const dbURI = "mongodb+srv://new-user12:qwerty123456@cluster0.8z293.mongodb.net/node-auth";

mongoose.connect(dbURI, {  }) //useNewUrlParser: true, useUnifiedTopology: true, useCreateIndex:true
  // .then((result) => app.listen(3000))
  .catch((err) => console.log(err));

mongoose.connect(dbURI, (err) => {
    console.log("mongoDB ansluten", err);
})
// routes
app.get("/", (req, res) => res.render("home"));
app.get("/otherSide", (req, res) => res.render("otherSide"));
app.use(authRoutes);

app.listen(3000, () => {
  console.log("Server är igång");
})