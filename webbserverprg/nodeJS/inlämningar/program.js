const fs = require("fs");
const md = `
______________________
Test                  |
                      |
Test                  |
                      |
Test                  |
______________________|
`;

if (fs.existsSync("./Filer/bruh.md"))
{
    fs.mkdir("Nya_Filer", err => {
        if (err){
            throw err;
        }

        console.log("Mappen skapad")
    });
    
    fs.renameSync("./Filer/bruh.md", "./Nya_Filer/bruh.md", err => {
        if(err){
            throw err;
        }
        console.log("Filen är flyttad")
    });

    fs.renameSync("./Filer", "./Filer_att-ta-bort")

    fs.readdirSync("./Filer_att-ta-bort").forEach(fileName => {
        fs.unlinkSync(`./Filer_att-ta-bort/${fileName}`);
    })

    fs.rmdir("./Filer_att-ta-bort", err => {
        if(err){
            throw err;
        }
        console.log(`Mappen är raderad`)
    });
}
else
{
    if(fs.existsSync("Filer")){
        console.log("Mappen finns redan!")
    }
    else{
        fs.mkdir("Filer", err => {
            if (err){
                throw err;
            }
        
            console.log("Mappen skapad.")
        });
    }

    if (fs.existsSync("./Filer/bruh.md")){
        console.log("Filen finns redan!")
    }
    else
    {
        fs.writeFile("./Filer/bruh.md", md.trim(), err =>{
            if (err){
                throw err;
            }
            console.log("Filen sparad")
        });
    }
};

