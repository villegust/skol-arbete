const express = require("express");
const mongoose = require("mongoose");
const authRoutes = require("./routes/authRoutes");
const cookieParser = require("cookie-parser");
const {requireAuth} = require("./middleware/authMiddleware");


const app = express();


// middleware
app.use(express.static("public"));
app.use(express.json());
app.use(cookieParser());

// view engine
app.set("view engine", "ejs");

// database connection
const dbURI = "mongodb+srv://new-user12:qwerty123456@cluster0.8z293.mongodb.net/node-auth";

// mongoose.connect(dbURI, {  }) //useNewUrlParser: true, useUnifiedTopology: true, useCreateIndex:true
//   // .then((result) => app.listen(3000))
//   .catch((err) => console.log(err));


app.listen(3000, () => {
  console.log("Server är igång");
});

mongoose.connect(dbURI, (err) => {
    if (err) {
        throw err;
    }
    else {
      console.log("mongoDB ansluten");
    }
      
})
// routes
app.get("/", (req, res) => res.render("home"));
app.get("/otherSide", requireAuth, (req, res) => res.render("otherSide"));
app.use(authRoutes);
