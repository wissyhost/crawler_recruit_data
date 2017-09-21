import sys, time, logging
from datetime import datetime

from dateutil.tz import tz, os


class ProgressBar:
    def __init__(self, count=0, total=0, keyword=""):
        self.count = count
        self.total = total
        self.keyword = keyword
        try:
            self.columns = os.get_terminal_size().columns
        except OSError as e:
            pass

    def moveTo(self, z):
        self.count = z

    def move(self, z=1):
        self.count += z

    def log(self, msg=""):
        if self.columns:
            width = self.getwidth()
            sys.stdout.write(' ' * (self.columns) + '\r')
            sys.stdout.flush()
            logging.info(msg)
            progress = int(width * self.count / self.total)
            sys.stdout.write('{0:3}/{1:3}: '.format(self.count, self.total))
            sys.stdout.write('#' * progress + '-' * (width - progress))
            sys.stdout.write(" :%s\r" % self.keyword)
            sys.stdout.flush()
            if progress == width:
                sys.stdout.write('\n')
            sys.stdout.flush()
        else:
            logging.info(msg)

    def getwidth(self):
        try:
            self.columns = os.get_terminal_size().columns
        except OSError as e:
            pass
        return self.columns - len(" :%s\r" % self.keyword) - len(
            '{0:3}/{1:3}: '.format(self.count, self.total)) - 9

    def __del__(self):
        if self.columns:
            sys.stdout.write(' ' * (self.columns) + '\r')
            sys.stdout.flush()


def getDateStr(tzName="CST"):  # 默认使用中国时区
    local = datetime.now(tz.gettz(tzName))
    return datetime.strftime(local, "%Y-%m-%d %H:%M:%S")
