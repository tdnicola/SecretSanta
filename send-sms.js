const accountId = ''
const authToken =  ''

const client = require('twilio')(accountId, authToken)

//people participating in the secret santa
var whiteChristmas = ['zach','tony','patrick','haley', 'steve', 'deke',];

//phone numbers of the participants to send their gift recipient 
var phoneArray = ['+111','+222','+333','+444','+555','+666']


function shuffle(recipient) {
    var ctr = recipient.length, temp, index;

// While there are elements in the array
    while (ctr > 0) {
// Pick a random index
        index = Math.floor(Math.random() * ctr);

        ctr--;
// And swap the last element with it
        temp = recipient[ctr];
        recipient[ctr] = recipient[index];
        recipient[index] = temp;
    }
    return recipient;
}


var nameAndPhone = phoneArray.map((item,i) => { 
   return [item,[shuffle(whiteChristmas)[i]]]; 
 });

//sending the message of to each of the recipient
nameAndPhone.forEach((i) => {
   client.messages.create({
       to: i[0],
       from: 'twilioNumber',
       body: i[1]
   })
   .then((message) => console.log(message))
 })