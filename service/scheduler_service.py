from apscheduler.schedulers.background import BackgroundScheduler
from . import db_service

def get_game_objects():
        print("get_game_objects")
def test():
        print("test")
        
def scheduler_start():
    scheduler = BackgroundScheduler(daemon=True)
    scheduler.add_job(get_game_objects,'interval',seconds=1,id="update-game-objects")
    scheduler.add_job(test,'interval',seconds=1,id="test")
    scheduler.start()