re('request');
const endpoint = process.argv[2];

request(endpoint, (err, res, body) => {
  if (!err) console.log('code:', res.statusCode);
});
