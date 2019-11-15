from gunicorn.config import Config
from gunicorn.http.errors import InvalidHeaderName

cfg = Config()
cfg.set('strip_header_spaces', False)

request = InvalidHeaderName
