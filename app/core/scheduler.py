from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

def start_scheduler():
    # Example job
    # scheduler.add_job(some_sync_task, 'interval', seconds=60)
    scheduler.start()
