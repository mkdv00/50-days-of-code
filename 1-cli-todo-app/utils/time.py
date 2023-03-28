import time


def get_current_date_and_time():
    template = '%b %d, %Y %H:%M:%S'
    return time.strftime(template)
