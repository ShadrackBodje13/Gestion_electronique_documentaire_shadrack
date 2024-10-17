from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time

class Watcher:
    DIRECTORY_TO_WATCH = "D:\\OCR_test_GED\\Gestion_electronique_documentaire_shadrack\\input_documents"


    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observation stopped")

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        if not event.is_directory:
            print(f"Received file - {event.src_path}")
            from ocr_classification import process_file
            result = process_file(event.src_path)
            print(f"Processing result: {result}")

if __name__ == "__main__":
    w = Watcher()
    w.run()
