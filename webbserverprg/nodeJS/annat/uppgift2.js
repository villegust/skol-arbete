const question = [
    "vad heter du?",
    "Vad är ditt favoritspel?",
    "Vart vill du helst resa?"
];

const ask = (i=0) => {
    process.stdout.write(`\n ${question[i]}`)
    process.stdout.write(":")
}

ask();

const answers = []

process.stdin.on("data", data => {
    answers.push(data.toString().trim());

    if(answers.length <question.length){
        ask(answers.length)
    }

    else{
        process.exit()
    }
})

const myURL = new URL('/foo', 'https://example.org/');

process.on("exit", () => {
    const[name, game, city] = answers;

    console.log(`\n Hej!!\n\n Jag uppskattar ditt svar ${name}. Nu ta och åk till ${city} och rör lite gräs istället för att sitta och spela ${game}. Här är en bra hemsida ${myURL}`)
})