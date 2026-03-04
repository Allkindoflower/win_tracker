from util import get_formatted_time


def log(event):
    ze_time = get_formatted_time()
    with open("logs.txt", "a") as f:
        f.write(f"{ze_time} - {event}\n") 