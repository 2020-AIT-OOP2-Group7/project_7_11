from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import os
import time
import cv2
import numpy as np

class ChangeHandler(FileSystemEventHandler):
    # すべてのイベント
    def on_any_event(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%s を確認' % filename)
        #グレイスケール化
        gray(event.src_path)

#グレイスケール化
def gray(filepath):
    im = cv2.imread(filepath)
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('grayscale_images/' + os.path.basename(filepath), im_gray)
    print('%s をグレースケール化しました' % os.path.basename(filepath))

if __name__ == '__main__':
    while 1:
        observer = Observer()
        # 監視するフォルダを第２引数に指定
        observer.schedule(ChangeHandler(), "upload_images", recursive=True)
        # 監視を開始する
        observer.start()
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()