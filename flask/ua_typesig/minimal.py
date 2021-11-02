from flask import Request
from werkzeug.user_agent import UserAgent

class MyUserAgent(UserAgent): pass

class MyRequest(Request):
    user_agent_class = MyUserAgent
