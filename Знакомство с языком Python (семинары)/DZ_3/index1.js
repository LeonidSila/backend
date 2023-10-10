// function sayHi() {
//   let name = prompt('Your name?');
//   alert(`Hello ${name}`);
// }
// sayHi();

let helloBtn = document.querySelector('.hello-btn');
helloBtn.addEventListener('click', hadnleName);
function hadnleName() {
  let name = prompt('Your name?', 'vasya');
  console.log(typeof name);
  if (name === null) alert('Please, say you name!');
  else alert(`Hello ${name}`);
}

let indexBtn = document.querySelector('.index-btn');
indexBtn.addEventListener('click', hadnleIndex);
function hadnleIndex() {
  let youWeigth = prompt('Your weigth (kg)?', 0);
  let youHight = prompt('Your hight? (cm)', 0);
  youHight = (youHight / 100) ** 2;
  console.log(youHight);
  let index = Math.round(youWeigth / youHight);
  if (isNaN(index)) alert('Value is not correct!');
  else if (index <= 16.49) alert(`Your index - ${index}: Severe underweight `);
  else if (index >= 16.5 && index <= 18.49)
    alert(`Your index - ${index}: Insufficient (deficit) body weight `);
  else if (index >= 18.5 && index <= 24.99)
    alert(`Your index - ${index}: Norm `);
  else if (index >= 25 && index <= 29.99)
    alert(`Your index - ${index}: Overweight (preobesity) `);
  else if (index >= 30 && index <= 34.99)
    alert(`Your index - ${index}: Obesity of the first degree `);
  else if (index >= 35 && index <= 39.99)
    alert(`Your index - ${index}: Obesity of the second degree `);
  else if (index >= 40)
    alert(`Your index - ${index}: Obesity of the third degree (morbid) `);
}
