from langchain.memory import ChatMessageHistory

history = ChatMessageHistory()
history.add_user_message("Hello")
history.add_user_message("Understand the following code written in Python Flask App")
history.add_user_message("""import logging
import os

from flask import Flask, render_template
from flask_sse import sse
from dotenv import load_dotenv

from app.services.PubSubHelper import PubSubHelper
from subscriber import event_handler

load_dotenv()

app = Flask(__name__)
app.config["REDIS_URL"] = os.getenv('REDIS_URL')
app.register_blueprint(sse, url_prefix='/stream')


@app.route("/<uname>")
def index(uname):
    return render_template("index.html", uname=uname)


@app.route("/hello/<channel>")
def publish_hello(channel):
    print("publishing hello to channel %s" % (channel))
    sse.publish({"message": "Hello!"}, type='greeting', channel=channel)
    return "Message sent!"


def publish(message, channel):
    print("publishing hello to channel %s" % (channel))
    sse.publish(message, type='greeting', channel=channel)
    return "Message sent!"


def create_app():

    # with app.app_context():
    #     PubSubHelper().subscribe("sse", event_handler)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

    # with app.app_context():
    #     PubSubHelper().subscribe("sse", event_handler)
""")

print(history.messages)
