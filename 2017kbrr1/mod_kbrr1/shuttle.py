#! -*- coding=utf-8 -*-

from datetime import timedelta
import logging

logging.basicConfig(level=logging.INFO)


def str_to_timedelta(str_time):
    """'HH:mm' 형태의 시간을 datetime.timedelta 형식으로 변환한다.
    """
    h, m = str_time.split(':')
    return timedelta(0, 3600 * int(h) + 60 * int(m))


class BusSupplier:
    """Shuttle bus를 생산한다?
    """
    def __init__(self, default_vacancy = 45):
        self.vacancy = default_vacancy

    def get_bus(self):
        """버스를 생산한다.
        """
        bus = ShuttleBus(self.vacancy)
        return bus


class ShuttleBus:
    def __init__(self, vacancy):
        self.vacancy = vacancy
        self.seat = []
    def load(self, person):
        if len(self.seat) < self.vacancy:
            self.seat.append(person)
        else:
            raise Exception("No Vacancy")
    def unload(self):
        self.seat = []
    def go(self):
        self.seat[len(self.seat):] = [ None ] * (self.vacancy - len(self.seat))
        logging.info("Bus is Going !! " + str(self.seat))


class BusAgency:
    """버스 배차 및 탑승을 관장하는 기관?
    """
    def __init__(self):
        self.bus_supplier = None

        self.bus_list = []
        self.passenger_list = []

    def set_bus_supplier(self, supplier):
        self.bus_supplier = supplier

    def schedule_bus(self, start_time="09:00", n = 1, t = 1):
        """
        """
        if not self.bus_supplier: raise Exception("There is no Bus supplier")
        d = str_to_timedelta(start_time)
        self.bus_list.append(dict((("time", d),("bus", self.bus_supplier.get_bus()))))
        for i in range(1, n):
            d += str_to_timedelta('00:' + str(t))
            self.bus_list.append(dict((("time", d),("bus", self.bus_supplier.get_bus()))))

    def guess_last_bus(self):
        """주어진, 버스 시간표와, 탑승객 명단을 가지고,
        마지막 버스를 탑승할 수 있는 시각을 알려준다.
        """
        shuttlable_vacancy = 0
        for bus in self.bus_list:
            shuttlable_vacancy += bus['bus'].vacancy
        logging.info("total vacancy : %d" % (shuttlable_vacancy))
        pass

    def _process_shuttle_bus(self):
        """셔틀 버스를 운영하면서, 현황을 출력한다.
        """
        for i, bus in enumerate(self.bus_list):
            logging.info("Bus %d Alived %s" % (i+1, bus))
        pass

    def _print_bus_time_table(self):
        """셔틀 버스 시간표를 출력한다.
        """
        for d in self.bus_list:
            #print("%s : %s" % (d['time'], d['bus']))
            print(d)
