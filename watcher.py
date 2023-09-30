import time
from utils.logger import logger
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

path = "./dockerfiles"

if __name__ == "__main__":
    event_handler = LoggingEventHandler()

    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()