#! -*- coding=utf-8 -*-

from datetime import timedelta


def str_to_timedelta(str_time):
    """'HH:mm' 형태의 시간을 datetime.timedelta 형식으로 변환한다.
    """
    h, m = str_time.split(':')
    return timedelta(0, 3600 * int(h) + 60 * int(m))


class ShuttleBus:
    """Shuttle bus time table을 관리한다.
    """
    def __init__(self, start_time="09:00", n = 1, t = 1):
        self.time_table = []
        d = str_to_timedelta(start_time)
        self.time_table.append(d)
        for i in range(1, n):
            d += str_to_timedelta('00:' + str(t))
            self.time_table.append(d)

    def print_time_table(self):
        """셔틀 버스 시간표를 출력한다.
        """
        #print(self.time_table)
        for i, t in enumerate(self.time_table):
            print("%d : %s" % (i+1, t))

class BusStop:
    pass

