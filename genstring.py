import pyrogram
from pyrogram import Client

heiman_ = """

Copyright (C) 2021 by HeimanPictures@Github, < https://github.com/HeimanPictures >.
This file is part of dev project,
and is released under the "MIT License Agreement".
Please see < https://github.com/HeimanPictures/String-Session/blob/Main/LICENSE >
All rights reserved.
"""

print(heiman_)
api_id = input("Enter Your API ID: \n")
api_hash = input("Enter Your API HASH : \n")

with Client("Heiman", api_id=api_id, api_hash=api_hash) as bot_:
    first_name = (bot_.get_me()).first_name
    string_session_ = f"<b>String Session For {first_name}</b> \nThanks To @HeimanSupports \n<code>{bot_.export_session_string()}</code>"
    bot_.send_message("me", string_session_, parse_mode="html")
    print(f"String Has Been Sent To Your Saved Message : {first_name}")
