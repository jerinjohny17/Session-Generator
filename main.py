print("A Termux StringSession generator. ©https://t.me/imjerin")

print("p => Pyrogram (docs.pyrogram.org)")

print("t => Telethon (docs.telethon.dev)")

print("Select your required option: ")
s_l = input("enter p / t ? ?? ")

if s_l == "p":
  print("Pyrogram was selected")
  APP_ID = int(input("Enter APP ID here: "))
  API_HASH = input("Enter API HASH here: ")
  import pyrogram
  with pyrogram.Client(
    ":memory:",
    api_id=APP_ID,
    api_hash=API_HASH
  ) as app:
    session_str = app.export_session_string()
    s_m = app.send_message("me", session_str)
    s_m.reply_text("⬆️ This StringSession is generated using https://github.com/jerinjohny-ktnm/Session-Generator \nThrough Termux app. ", quote=True)
    print("Please check your Telegram Saved Messages for the StringSession ")

elif s_l == "t":
  print("Telethon was selected")
  # (c) https://t.me/TelethonChat/37677
  from telethon.sync import TelegramClient
  from telethon.sessions import StringSession
  APP_ID = int(input("Enter APP ID here: "))
  API_HASH = input("Enter API HASH here: ")
  with TelegramClient(
    StringSession(), 
    APP_ID, 
    API_HASH
  ) as client:
    session_str = client.session.save()
    s_m = client.send_message("me", session_str)
    s_m.reply("⬆️ This StringSession is generated using https://github.com/jerinjohny-ktnm/Session-Generator!")
    print("Please check your Telegram Saved Messages for the StringSession ")

else:
  print("?? please select only p / t, ")
