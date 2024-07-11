#!/usr/bin/node

const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`, (error, _, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const charName = JSON.parse(body).char.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseError, __, charReqBody) => {
          if (promiseError) {
            reject(promiseError);
          }
          resolve(JSON.parse(charReqBody).name);
        });
      }));
    Promise.all(charName)
      .then(charNames => console.log(charNames.join('\n')))
      .catch(errors => console.log(errors));
  }
});
