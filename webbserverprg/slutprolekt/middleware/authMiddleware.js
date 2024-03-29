const jwt = require("jsonwebtoken");
const User = require("../models/User");

const requireAuth = (req, res, next) => {
    const token = req.cookies.jwt;

    //kollar om web token finns och är verifierad

    if (token){
        jwt.verify(token, "test test", (err, decodedToken) => {
            if (err){
                console.log(err.message);
                res.redirect("/login");
            }
            else{
                console.log(decodedToken);
                next();
            }
        })
    }
    else{
        res.redirect("/login");
    }
}

//kollar användaren om den är inloggad och token finns. 
const checkUser = (req, res, next) => {
    const token = req.cookies.jwt;
    
    if (token){
        jwt.verify(token, "test test", async (err, decodedToken) => {
            if (err){
                console.log(err.message);
                res.locals.user = null;
                next();
            }
            else{
                console.log(decodedToken);
                let user = await User.findById(decodedToken.id);
                res.locals.user = user;
                next();
            }
        })
    }
    else{
        res.locals.user = null;
        next();
    }    

}

module.exports = {requireAuth, checkUser};
