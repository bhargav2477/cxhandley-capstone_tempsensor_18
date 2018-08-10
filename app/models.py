import datetime

from pony import orm
from pony.orm import db_session

db = orm.Database()

## Entity declarations
class Event(db.Entity):

    _table_ = 'Events'

    date = orm.Required(datetime.datetime, default=datetime.datetime.utcnow)
    type = orm.Required(str)
