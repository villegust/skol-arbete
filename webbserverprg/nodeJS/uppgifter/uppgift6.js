
const fs = require("fs");

                            //Byter namn på filen:

// fs.renameSync("./Mina-Fina-filer/minaFarger.md", "./Mina-Fina-filer/Farger.md");

                            //Flyttar filer:

// fs.rename("./Mina-Fina-filer/nyText.md","./nya-fina-filer/nyText.md" , err =>{
//     if (err){
//         throw err;
//     }
// });

                            //Tar bort filen:
//fs.unlinkSync("./Mina-Fina-filer/minaFarger.md");

// const colorData = require("./farger.json");

// colorData.colorList.forEach(c => {
//     fs.appendFile("./Mina-Fina-filer/minaFarger.md", `${c.färg}: ${c.hex} \n`, err =>{
//         if (err){
//             throw err;
//         }
//     });
// });

fs.renameSync("./Mina-Fina-filer", "./filer")

fs.readdirSync("./filer").forEach(fileName => {
    fs.unlinkSync(`./filer/${fileName}`);
})

fs.rmdir("./filer", err => {
    if(err){
        throw err;
    }
    console.log("Mappen är raderad")
});