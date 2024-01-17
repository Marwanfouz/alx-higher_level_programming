#!/user/bin/node
const request = require('request');
const url = process.argv[2]
request(url, (err, res, body) => {
  if (err || res.statusCode !== 200) {
    console.error(err);
    return;
  }
  const userdi = {};
  const data = JSON.parse(body);
  for (const users of data) {
    if (users.completed) {
      if (users.userId in userdi) {
        userdi[users.userId]++;
      } else {
        userdi[users.userId] = 1;
      }
    }
  }
  console.log(userdi);
});
