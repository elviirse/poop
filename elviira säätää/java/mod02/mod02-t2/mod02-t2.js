//Write a program that asks the user for the number of participants.
// After this, the program asks for the names of all participants.
// Finally, the program prints the names of the participants on the web page
// in an ordered list (<ol>) in alphabetical order. (2p)

const participants = [];
const amount = prompt('How many participants?');

for (let i = 0; i < amount; i++) {
  const name = prompt('Enter participant name:');
  participants.push(name);
}

participants.sort();

const target = document.querySelector('#target');

for (let i = 0; i < participants.length; i++) {
  target.innerHTML += '<li>' + participants[i] + '</li>';
}