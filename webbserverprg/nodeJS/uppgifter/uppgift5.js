const md = `
I'm loaded, and I got stacks bruh bruh, all my homies from da trap bruh bruh.

`;


const fs = require("fs");

if(fs.existsSync("Mina-Fina-Filer")){
    console.log("Mappen finns redan!")

}else{
    fs.mkdir("Mina-fina-filer", err => {
        if (err){
            throw err;
        }
    
        console.log("Mappen skapad.")
    });
    
}

if (fs.existsSync(".//Mina-Fina-Filer/nyText.md")){
    console.log("Filen finns redan!")
}else{
    fs.writeFile(".//Mina-Fina-Filer/nyText.md", md.trim(), err =>{
        if (err){
            throw err;
        }
        console.log("Filen sparad")
    });
}
