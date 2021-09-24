'use strict';

const express = require('express');
const line = require('@line/bot-sdk');
const PORT = process.env.PORT || 3000;

const config = {
    channelAccessToken: '4rK2NXLs39EbTh6nXbaupT3B+ZPhB+2/z/hdp0deLA+kJWmb4nvep75QfbD4O4P4zRe1SI+7EIkZyZ7LnFjpBjNb1/hUdVwx1jNuR42ow7FKk9QtEkODQDFI4kd6NwGeN7VPjS4O9WwYmYFp0tY3eAdB04t89/1O/w1cDnyilFU=',
    channelSecret: '8c59ddf565d45b68dec7839ec63f6885'
};

const app = express();

app.post('/webhook', line.middleware(config), (req, res) => {
    console.log(req.body.events);
    Promise
      .all(req.body.events.map(handleEvent))
      .then((result) => res.json(result));
});

const client = new line.Client(config);

function handleEvent(event) {
  if (event.type !== 'message' || event.message.type !== 'text') {
    return Promise.resolve(null);
  }

  return client.replyMessage(event.replyToken, {
    type: 'text',
    text: event.message.text
  });
}

app.listen(PORT);
console.log(`Server running at ${PORT}`);
