from flask import request, abort, url_for, render_template, Blueprint
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
    ButtonsTemplate,
    TemplateSendMessage,
    PostbackAction,
    MessageAction,
    URIAction,
)

bot_api = Blueprint("bot_api", __name__)
"""
# CHANEL TOKEN
line_bot_api = LineBotApi(
    ""
)
# SECRET
handler = WebhookHandler("")
"""

@bot_api.route("/", methods=["GET"])
def index():
    return render_template("index.html")

"""
@bot_api.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = request.get_data(as_text=True)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print(
            "Invalid signature. Please check your channel access token/channel secret."
        )
        abort(400)

    return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if "register" in event.message.text:
        buttons_template_message = TemplateSendMessage(
            alt_text="Buttons template",
            template=ButtonsTemplate(
                thumbnail_image_url=url_for(
                    "static",
                    filename="img/cover.png",
                    _external=True,
                    _scheme="https",
                ),
                title="Menu",
                text="Please select",
                actions=[
                    PostbackAction(
                        label="postback",
                        display_text="postback text",
                        data="action=buy&itemid=1",
                    ),
                    MessageAction(label="message", text="message text"),
                    URIAction(label="uri", uri="http://example.com/"),
                ],
            ),
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
"""