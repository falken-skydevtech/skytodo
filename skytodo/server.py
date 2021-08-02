import logging
import logging.handlers
import sys, os
import threading
import time

formatter = logging.Formatter("%(asctime)s:%(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S")
handler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE", "./app.log"))
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)

cwd = os.getcwd()
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skytodo.settings-ovh')
logging.info("before start")

def background_process():
    while True:
        time.sleep(1)
        if os.path.exists("/home/freelap/skytodo/kill-order"):
            logging.info("kill file order exists")
            os.remove("/home/freelap/skytodo/kill-order")
            os.system("kill -9 %s" % os.getpid())

try:
    t = threading.Thread(target=background_process, args=(), kwargs={})
    t.setDaemon(True)
    t.start()
    application = get_wsgi_application()
except Exception as e:
    logging.info("start application failed on %s" % e)

logging.info("after start %s" % (application,))
