from database._db import session
from database.model.setting import Setting

settings = [
    Setting('DEFAULT_MAP_NAME', 'rootville'),
    Setting('MOVE_OBJECT_FREQUENCY_SEC', '0.1')
]

session.add_all(settings)
session.commit()

