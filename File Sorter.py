import logging
import os
import shutil
import time
from watchdog.events import LoggingEventHandler
from watchdog.observers import Observer

img_dest = "/home/shoham/Pictures"
pdf_dest = "/home/shoham/Documents/PDFs"
docs_dest = "/home/shoham/Documents/Docs"
presention_dest = "/home/shoham/Documents/Presentations"
source_dir = "/home/shoham/Downloads"

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, source_dir, recursive=True)
    observer.start()
    try:
         while True:
            time.sleep(1)
            with os.scandir(source_dir) as entries:
                for entry in entries:
                    if ".jpg" in entry.name or ".png" in entry.name:
                        shutil.move(entry.path, img_dest)
                    if ".pdf" in entry.name:
                        shutil.move(entry.path, pdf_dest)
                    
                    if ".pttx" in entry.name :
                        os.move(entry.path,presention_dest)

    except KeyboardInterrupt:
        observer.stop()
    observer.join()
