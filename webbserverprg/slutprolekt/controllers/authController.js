const User = require("../models/User");


//Tar hand om errors
const handleErrors = (err) => {
    console.log(err.message, err.code);
    let errors = {
        email : "",
        password : ""
    };

    //Handterar duplicates
    if (err.code == 11000){
        errors.email = "That email is already registerd";
        return errors;

    }

    //Hanterar errors
    if (err.message.includes("user validation failed")){
        Object.values(err.errors).forEach(({properties})  => {
            // console.log(error.properties);
            errors[properties.path] = properties.message
        })
    }

    return errors;
}

module.exports.signup_get = (req, res) => {
    res.render("signup");
}

module.exports.login_get = (req, res) => {
    res.render("login");
}

module.exports.signup_post = async (req, res) => {
    const{ email, password } = req.body

    try{
        const user = await User.create({ email, password });
        res.status(201).json(user);
    }
    catch(err){
        const errors = handleErrors(err)
        res.status(400).json({errors})
    }
}

module.exports.login_post = async (req, res) => {
    const{ email, password } = req.body
    console.log("LOGIN INFO")
    console.log("Email:", email, "|" ,"Password:", password);

    res.send("user login");
}