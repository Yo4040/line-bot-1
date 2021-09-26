# setting.pyで取得したアクセストークンとユーザーIDを代入
CHANNEL_ACCESS_TOKEN = "h2CKZQS7erEDKPX32LwBRsq79gRdR0Dx/z9jysdzLSmJNKp1UN9bBA5bWCi6wIGRI3pTVPmXzuNtd9DvtbAkrUMrR3DkTRv1GZVRU+6frocFEUlaUoAW4g1QO3w3SgYbWO3j8utiPWFanJrL6JteawdB04t89/1O/w1cDnyilFU="
USER_ID = "U81b5b53e09a2809a72b2a6c10d0e33eb"
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def push():
    # LINEで送る内容を記述
    messages = TextSendMessage(text="おはよう〜〜〜〜")
    line_bot_api.push_message(USER_ID, messages=messages)

# 実行！
push()