const collectAnswers = require("./module");

const questions = [
    "Vad heter du? ",
    "Vad tycker du om att göra? ",
    "Vad vill du jobba som? "
];

const answerEvents = collectAnswers(questions);

answerEvents.on("answer", answer =>
    console.log(`Frågan besvarad: ${answer}`)
);

answerEvents.on("complete", answers => {
    console.log("Tack för dina svar! ");
    
    let text = "";
    for (let i = 0; i < answers.length; i++) {
        text += answers[i] + "<br>";
        console.log(answers[i]);
    }
    console.log(`Hej ${answers[0]}. Roligt att du gillar ${answers[1]} och att du vill jobba med ${answers[2]}`)
    process.exit();
})


