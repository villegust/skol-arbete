const jwt = require("jsonwebtoken");

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

module.exports = {requireAuth};