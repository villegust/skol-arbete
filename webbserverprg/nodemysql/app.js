const express = require("express");
const mysql = require("mysql");

const db = mysql.createConnection({
    host : "localhost",
    user : "root", 
    password : "Bandy2003",
    database : "nodemysql"
});

db.connect((err) => {
    if (err){
        throw err;
    }
    console.log("MySql Connected");
});

const app = express();

app.get("/createdb", (req, res) => {
    let sql = "CREATE DATABASE nodemysql"
    db.query(sql, (err, result) => {
        if (err) throw err;
        console.log(result);
        res.send("Database created");
    });
});

app.get("/createpoststable", (req, res) => {
    let sql = "CREATE TABLE posts(id int AUTO_INCREMENT, title VARCHAR(255), body VARCHAR(255), PRIMARY KEY (id))";
    db.query(sql, (err, result) => {
        if(err) throw err;
        console.log(result);
        res.send("Posts table created");

    });
});

app.get("/addpost1", (req, res) => {
    let post = {title:"Post One", body:"This is post number one"};
    let sql = "INSERT INTO post SET ?";
    let query = db.query(sql, post, (err, result) => {
        if(err) throw err;
        console.log(result);
        res.send("Posts 1 added");

    });
});

app.listen("3000", () => {
    console.log("Servern startade på port 3000");
});
