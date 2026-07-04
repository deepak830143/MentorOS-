from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from app.tasks.appsc_task import run_notification_engine

scheduler = BackgroundScheduler()


def start_scheduler():

    if scheduler.running:
        return

    scheduler.add_job(
        run_notification_engine,
        trigger=IntervalTrigger(minutes=1),
        id="notification_engine",
        replace_existing=True,
    )

    scheduler.start()

    print("✅ APScheduler Started")
    print("✅ Notification Engine Scheduled (Every 1 Minute)")