const dogs = [];

for (let i = 0; i < 6; i++) {
  const dog = prompt('Enter dog name:');
  dogs.push(dog);
}

dogs.sort();
dogs.reverse();

const target = document.querySelector('#target');

for (let i = 0; i < dogs.length; i++) {
  target.innerHTML += '<li>' + dogs[i] + '</li>';
}