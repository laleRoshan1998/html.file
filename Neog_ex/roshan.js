        // exercise.1
// console.log("hello");
var readlinesync = require("readline-sync");

         // exercise.2
// var userName = readlinesync.questionInt("Give me your name? ");
// var welcomeMassage = "welcome" + userName
// console.log(welcomeMassage)

//        exercise. 5


// var userMy_Age = readlinesync.question("I am older than 23? ");
// console.log('your entered' + userMy_Age);
// if (userMy_Age == "yes"){
//         console.log('your are right')
// } else {
//         console.log('your are wrong')
// }

        //   exercise. 6
// var score=0;
// var userMy_Age = readlinesync.question("I am older than 23? ");
// console.log('your entered' + userMy_Age);
// if (userMy_Age == "yes"){
//         console.log('your are right')
//         score+=1
//         console.log('socre is ' + score)
// } else {
//         console.log('your are wrong')
//         score = score-1
//         console.log('score is ' + score)
// }

        //      exrcise. 7
// function add(numberOne, numberTwo){
//         var sum = numberOne + numberTwo;
//         return sum;

// }
// var count = add (10,20);
// console.log('The sum of 10 and 20 is :' + count);

                // exrcise. 8
// score=0;
// function play(question,asnwer){
//         var userAnswer = readlinesync.question(question);
//         if ( userAnswer == asnwer){
//         console.log('your are right')
//         score+=1;
//         }else{
//                 console.log('your are wrong')
//                 score = score-1;
//         }
// }
// play("where I do work?", "software");
// play("where do I Live?", "nagpur")
// console.log('your score is', + score)

        // exrcise. 9
// for (var i=0; i < 5; i = i + 1){
//         console.log("Roshan")
// }

        // exrcise. 10
// var grocerylist = ["milk","egg","veg","maggi","pav bhaji"]
// console.log(grocerylist[0]);
// console.log(grocerylist[2]);
// console.log(grocerylist[4]);

// var howlongisAarry = grocerylist.length
// console.log(howlongisAarry)
// console.log(grocerylist[grocerylist.length - 1])

//         exrcise. 11
// function long(data){
//         console.log(data)
// }
// var grocerylist = ["milk","egg","veg","maggi","pav bhaji"]
// for (i=0; i < grocerylist.length; i++){
//         console.log(grocerylist[i]);
// } 

//         exrcese. 12
// var superman = {
//         name : "superman",
//         power : "flight",
//         costumercolor : "blue",
//         strenght : 10000,
//         stealth : 0,
//         intellingence : 100,
// }

// var batman = {
//         name : "batman",
//         power : "flight",
//         costumercolor : "black",
//         strenght : 100,
//         strealth : 100,
//         intellingence : 1000,
// }
// console.log(superman.strenght);
// console.log(batman.strenght);
// console.log(superman.strenght > batman.strealth)

        // exrcise. 13
// score=0;
// function play(question,asnwer){
//         var userAnswer = readlinesync.question(question);
//         if (userAnswer == asnwer){                                                                                                                                                                                                                                                                                         
//                 console.log("right")
//                 score+=1;

//         } else{
//                 console.log('wrong')
//         }

//         console.log("current score", + score);
//         console.log("------------------")
// }
//         exrcise. 14
// var score = 0;
// var userName = readlinesync.question("what is your name? ")
// console.log('welcome' + userName + "to Do you know roshan? ")
// function play(question,asnwer){
//         var userAnwer = readlinesync.question(question)
//         if (userAnwer == asnwer){
//                 console.log("right")
//                 score = score + 1
//         } else {
//                 console.log("wrong")
//         }
//         console.log("current score:",score)
//         console.log("-----------------")
// }
// play("where do i live? ","Dharmashala")
// play("my favorite superhero? ","vijay")

        // exercise. 15
// var score = 0;
// var highschore = [
//         {
        
//                 Name: "Akash",
//                 score: 3,      
//         },
//         {
//                 Name: "Satish",
//                 score: 2,
//         },
// ]

// var question = [{
//         question: "Where do I live?  ",
//         answer: "dharmashala"
// },{
//         question: "my favorite Superhero would be?  ",
//         answer: "Hritik roshan",
// },
// {
//         question: "Where do I work?  ",
//         answer: "Programming"
// }];

// function welcome() {
//         var userName = readlinesync.question("What is your name?  ");
//         console.log("welcome " + "to do know Roshan?  ");

// }
// function play(question, answer) {
//         var userAnswer = readlinesync. question(question);
//         if (userAnswer.toUpperCase() == answer.toUpperCase()){
//                 console.log("Right");
//                 score+=1;
//         } else {
//                 console.log("Wrong");
//         }
//         console.log("current score: ", score);
//         console.log("-------------")
// }

// function game (){
//         for (var i=0; i<question.length; i++) {
//                 var currentQuestion = question[i];
//                 play(currentQuestion.question,currentQuestion.answer)
//         }
// }

// function shoScores(){
//         console.log("yay! you scored: ", score);

//         console.log("cheack out the high scores, if you should be there ping me and I'll update it");

//         console.log(highschore[0].Name,score+'\n'+highschore[1].Name,score);
// }

// welcome();
// game();
// shoScores();
             




// const promp=require('prompt-sync')()
// const name=Number(promp("number "))




// const chalk = require('chalk');
// console.log(chalk.red("hello"))


// console.log(chalk.blue('Hello world!'));

// // const chalk = require('chalk');
// const log = console.log;
// log(chalk.blue('Hello') + ' World' + chalk.red('!'));
// log(chalk.green(
// 	'I am a green line ' +
// 	chalk.blue.underline.bold('with a blue substring') +
// 	' that becomes green again!'
// ));
// log(`
// CPU: ${chalk.red('90%')}
// RAM: ${chalk.green('40%')}
// DISK: ${chalk.yellow('70%')}

// var readlineSync = require("readline-sync");

// var score = 0;

// // data of high score
// var highScores = [
//   {
//     name: "Tanay",
//     score: 3,
//   },

//   {
//     name: "Akash",
//     score: 2,
//   },
// ]

// // array of objects
// var questions = [{
//   question: "Where do I live? ",
//   answer: "Bangalore"
// }, {
//   question: "My favorite superhero would be? ",
//   answer: "Dhruv"
// },
// {
//   question: "Where do I work? ",
//   answer: "Microsoft"
// }];

// function welcome() {
//  var userName = readlineSync.question("What's your name? ");

//   console.log("Welcome "+ userName + " to DO YOU KNOW Tanay?");
// }


// // play function
// function play(question, answer) {
//   var userAnswer = readlineSync.question(question);

//   if (userAnswer.toUpperCase() === answer.toUpperCase()) { // branching
//     console.log("right!");
//     score = score + 1;
    
//   } else {
//     console.log("wrong!");
   
//   }

//   console.log("current score: ", score);
//   console.log("-------------")
// }

// function game() {
//   for (var i=0; i<questions.length; i++) {
//     var currentQuestion = questions[i];
//     play(currentQuestion.question, currentQuestion.answer)
//   }
// }

// function showScores() {
//   console.log("YAY! You SCORED: ", score);

//   console.log("Check out the high scores, if you should be there ping me and I'll update it");

//   highScores.map(score => console.log(score.name, " : ", score.score))
// }


// welcome();
// game();
// showScores();


