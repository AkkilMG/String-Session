# Copyright (c) 2021 HEIMAN PICTURES

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from telethon.sessions import StringSession
from telethon.sync import TelegramClient

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

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("Check your Telegram Saved Messages to copy the STRING_SESSION value")
    session_string = client.session.save()
    saved_messages_template = """Support: @userbotindo
<code>STRING_SESSION</code>: <code>{}</code>
⚠️ <i>Please be carefull to pass this value to third parties</i>""".format(session_string)


#   print(client.session.save())
#    client.send_message("me", client.session.save())
