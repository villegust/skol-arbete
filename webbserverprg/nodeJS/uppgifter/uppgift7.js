const getArgs = require("minimist");
const {stdout:log} = require("single-line-log");
const Timer = require("tiny-timer")

const {tid} = getArgs(process.argv);

if (!tid){
    throw new Error("--tid måste finnas");
}

if (!parseInt(tid)){
    throw new Error("--tid får endast innehålla siffror");
}

const count = parseInt(tid);
let meddelande = "";

for(let i = 0; i < count; i++){
    meddelande += "."
}

const timer = new Timer({interval: 1000});

timer.on("tick", () => {
    log(meddelande);
    meddelande = meddelande.slice(1);
});

timer.start(count * 1000);