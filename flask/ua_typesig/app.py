from flask import Request
from ua_parser import user_agent_parser
from werkzeug.user_agent import UserAgent


class MyUserAgent(UserAgent):
    def __init__(self, s: str) -> None:
        super().__init__(s)
        # for structure of parsed data, see
        # https://github.com/ua-parser/uap-core/blob/master/docs/specification.md#parser-output
        # and
        # https://github.com/ua-parser/uap-python#retrieve-data-on-a-user-agent-string
        parsed = user_agent_parser.Parse(s)
        self.platform = parsed["os"]["family"]
        self.broswer = parsed["user_agent"]["family"]
        # handle missing patch numbers for UA version
        version_info = [parsed["user_agent"][x] for x in ("major", "minor", "patch")]
        version_info = [x for x in version_info if x is not None]
        self.version = ".".join(version_info)


class MyRequest(Request):
    user_agent_class = MyUserAgent
