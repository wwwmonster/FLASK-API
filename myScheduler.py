import schedule
import time


def job():
    print("I'm working...")


# schedule.every(10).seconds.do(job)
schedule.every(3).seconds.do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
