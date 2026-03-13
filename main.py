from gui.app import run
from database.db import create_table
import database.db as db

create_table()
run()

rows = db.get_all()
for row in rows:
    print(row)