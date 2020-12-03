#ディレクトリの監視

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time

class ChangeHandler(FileSystemEventHandler):
    #全てのイベント
    def on_any_event(self, event):
        print('ディレクトリが更新されました')

observer = Observer()
observer.schedule(ChangeHandler(), 'upload_images',recursive=True)
observer.start()

while True:
    time.sleep(5)