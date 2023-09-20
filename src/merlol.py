from lcucomm import lcu_connector
import threading

if __name__ == "__main__":
    print('Merlol now running.')
    x = threading.Thread(target=lcu_connector.start)
    x.start()
