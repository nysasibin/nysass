# cron.py
import datetime

import pytz
from django_cron import CronJobBase, Schedule

from .models import Blog


class UpdatePostStatusCronJob(CronJobBase):
    RUN_EVERY_MINS = 1  # Change this to the desired interval (in minutes)

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'blog.update_post_status_cron_job'  # Replace 'your_app_name' with your app name

    def do(self):
        print("Cron job is running...")
        now = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
        print("Current time:", now)

        for blog in Blog.objects.all():
            if blog.post_published and blog.post_published <= now:
                print(f"Updating post status for blog '{blog.title}'")
                blog.post = True
                blog.save()
