from threading import Thread, Lock
import logging
import webview
from time import sleep
from gnucash_portfolio_webui.app import run_server

# Configuration
server_ip: str = "127.0.0.1"
server_port: int = 5000
################

server_lock = Lock()

logger = logging.getLogger(__name__)


def url_ok(url, port):
    """ Check if the server has started """
    from http.client import HTTPConnection

    try:
        conn = HTTPConnection(url, port)
        conn.request("GET", "/")
        r = conn.getresponse()
        return r.status == 200
    except:
        logger.exception("Server not started")
        return False

def main():
    """ entry point for the setup """
    logger.debug("Starting server")
    t = Thread(target=run_server)
    t.daemon = True
    t.start()
    logger.debug("Checking server")

    while not url_ok(server_ip, server_port):
        sleep(0.1)

    logger.debug("Server started")
    webview.config.use_qt = True
    webview.create_window("GnuCash Portfolio",
                          f"http://{server_ip}:{server_port}",
                          min_size=(1024, 768))


if __name__ == '__main__':
    main()
