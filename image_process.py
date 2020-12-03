from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import os
import time
import cv2
import numpy as np


class ChangeHandler(FileSystemEventHandler):
    # すべてのイベント
    def on_any_event(self, event):
        print('[全て]',event)
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%s' % filename)


observer = Observer()
# 監視するフォルダを第２引数に指定
observer.schedule(ChangeHandler(), 'upload_images', recursive=True)
# 監視を開始する
observer.start()

while True:
    time.sleep(5)