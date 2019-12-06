const accountId = ''
const authToken =  ''

const client = require('twilio')(accountId, authToken)

//people participating in the secret santa
var whiteChristmas = ['Zach','Tony','Patrick','Haley', 'Steve', 'Deke', 'Marie', 'Monika'];

//phone numbers of the participants to send their gift recipient 
var phoneArray = ['+111','+222','+333','+444','+555','+666', '+777', '+888']

tehCompleteList = [];


function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}
shuffleArray(whiteChristmas)
// console.log(whiteChristmas)


whiteChristmas.forEach(function(v,i){
  var obj = {};
  obj.to = phoneArray[i];
  obj.body = v;
  obj.from = 888888 //twilio phone number
  tehCompleteList.push(obj);
});
// console.log(tehCompleteList)


//console logging the results of the shuffle
tehCompleteList.forEach((i) => {
    console.log(i.to, i.from, i.body)
})

// sending the message of to each of the recipient
tehCompleteList.forEach((i) => {
   client.messages.create({
       to: i.to,
       from: i.from,
       body: i.body
   })
   .then((message) => console.log(message))
 })
