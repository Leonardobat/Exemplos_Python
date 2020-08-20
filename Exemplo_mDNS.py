import time
from multiprocessing import Process, Pipe
from zeroconf import ServiceBrowser, Zeroconf


class MyListener(object):
    def __init__(self):
        self.all_del_sub = []
        self.all_info_dict = {}
        self.all_sub_num = 0
        self.new_sub = False

    def remove_service(self, zeroconf, type, name):
        if name not in self.all_info_dict:
            return
        self.all_sub_num -= 1
        del self.all_info_dict[name]
        self.all_del_sub.append(name)

    def add_service(self, zeroconf, type, name):
        self.all_sub_num += 1
        info = zeroconf.get_service_info(type, name)
        self.all_info_dict[name] = info
        if name in self.all_del_sub:
            self.all_del_sub.remove(name)

    def update_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        self.all_info_dict[name] = info
        if name in self.all_del_sub:
            self.all_del_sub.remove(name)


def mDNS():
    zeroconf = Zeroconf()
    listener = MyListener()
    browser = ServiceBrowser(zeroconf, "teste._tcp.local.", listener)
    while True:
        try:
            if listener.all_sub_num > 0:
                dict = listener.all_info_dict.copy()
                for x in dict.keys():
                    info = dict[x]
                    info = zeroconf.get_service_info(info.type, x)
                    if info != None:
                        data = info.properties
                        cur_str = (
                            x[9:21]
                            + "\n"
                            + info.parsed_addresses()[0]
                            + "\n"
                            + str(info.port)
                            + "\n"
                            + str(data)
                        )
                        print(cur_str + "\n")
            if len(listener.all_del_sub) > 0:
                for x in listener.all_del_sub:
                    cur_str = x[9:21] + "\nDEL"
                    print(cur_str + "\n")
            time.sleep(0.5)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    mDNS()
