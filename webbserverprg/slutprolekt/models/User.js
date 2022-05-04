const mongoose = require("mongoose");
const {isEmail} = require("validator");
const bcrypt = require("bcrypt");


//definierar dokumentets struktur i databasen 
const userSchema = new mongoose.Schema({

    username : {
        type: String,
        unique: true,
        required: [true, "Please enter a username"]
    },

    email: {
        type: String,
        required: [true, "Please enter a email"],
        unique: true,
        lowercase: true,
        validate: [isEmail, "Please enter a valid email"]
    },
    password:{
        type: String,
        required: [true, "Please enter a password"],
        minlength: [6, "Minimum length is 6 characters"]
    },
});

//krypterar ditt lösenord med en salt och med bcrypt (hash)
userSchema.pre("save", async function(next){
    const salt = await bcrypt.genSalt();
    this.password = await bcrypt.hash(this.password, salt)
    next();
});

//statisk login metod
userSchema.statics.login = async function(email, password){
    const user = await this.findOne({email});   

    if (user){
        const auth = await bcrypt.compare(password, user.password);
        if (auth){
            return user;
        }
        throw Error("Incorrect password");
    } 
    throw Error("Incorrect email")
}


const User = mongoose.model("user", userSchema);

module.exports = User;