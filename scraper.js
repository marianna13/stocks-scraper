import fetch from "node-fetch";

const url = 'https://finance.yahoo.com/quote/F';

fetch(url, {
    method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  },
})
.then((response) => {
    return response.text();
    })
.then((text)=> {
    console.log(text.toString().search('D(ib) Mend(20px)'));
})