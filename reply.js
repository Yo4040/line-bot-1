const access_token = 'gCjrAxvvWfV0o9djt0C58rhxlLJKjgSzqaStJXMbjTsJLb+00iabszFxSbnMNQiyQIEA0kqC/Oo11hIO486ZWAJ9fYKZyuJXDu0UQwHz6Jitr8IQFn9hnFi6+Z/HGklwTKsgU2nr8lJSKwRVdyktTgdB04t89/1O/w1cDnyilFU=';

function doPost(e) {
  var events = JSON.parse(e.postData.contents).events;
  events.forEach(function (event) {
    switch (event.type) {
      case 'message':
        reply(event);
        break;
      case 'postback':
        postback(event);
        break;
      case 'join':
        join(event);
        break;
      default:
        ;
        break;
    }
  });
}

function reply(e) {
    let Message = e.message.text;
  if (Message=="test"){
      var message = {
      'replyToken': e.replyToken,
      'messages': [{
  "type": "text",
    "sender": {
    "name": "A",
  },
  "text":'On',
  "quickReply": {
     "items": [
       {
        "type": "action",
        "action": {
            "type": "message",
            "label": "問題",
            "text": "Q"
                  }
       },
             ]
           }
}]
    }
    }
    var replyData = {
      'method': 'post',
      'headers': {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_token
      },
      'payload': JSON.stringify(message)
    };
    UrlFetchApp.fetch('https://api.line.me/v2/bot/message/reply', replyData);
}