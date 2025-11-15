const fs = require('fs');
const pdf = require('pdf-parse');

const dataBuffer = fs.readFileSync('/vercel/sandbox/uploads/Smart traffic control system.pdf');

pdf(dataBuffer).then(data => {
  console.log(data.text);
}).catch(err => {
  console.error(err);
});