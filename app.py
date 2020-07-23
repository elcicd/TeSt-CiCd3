import json
from datetime import datetime
import os
import logging
import time


class x():
    enbid = None
    @staticmethod
    def someMethod():
        print("Testing")

def main():
    """

    """

    logging.basicConfig(
        level=logging.os.environ.get('loglevel'),
        format="%(asctime)s:%(levelname)s:%(message)s"
    )

    x = 10
    while x > 0:
        print("hostname : %s" % os.uname()[1])
        print("cgroup value : %s" % os.environ.get('cgroup'))
        print("topicname value : %s" % os.environ.get('topicname'))
        time.sleep(10)
        x = x - 1


if __name__ == "__main__":
    main()
