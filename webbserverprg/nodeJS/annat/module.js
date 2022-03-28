const readline = require("readline");

const {EventEmitter} = require("events");

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

module.exports = (questions, done) => {
    const answers = [];
    const [firstQuestion] = questions;

    const emitter = new EventEmitter();

    const questionAswered = answer => {
        emitter.emit("answer", answer);
        answers.push(answer);

        if (answers.length < questions.length){
            r1.question(questions[answers.length], questionAswered);
        }else{
            emitter.emit("complete", answers)
            done(answers);
        }
    };
    r1.question(firstQuestion, questionAswered)
    return emitter
};
