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

def mDNS():
    zeroconf = Zeroconf()
    listener = MyListener()
    browser = ServiceBrowser(zeroconf, "_solutech_IR._tcp.local.", listener)
    while True:
        try:
            if listener.all_sub_num>0:
                dict = listener.all_info_dict.copy()
                for x in dict.keys():
                    info = dict[x]
                    info = zeroconf.get_service_info(info.type,x)
                    if info != None:
                        data = info.properties
                        cur_str =(x[9:21] + "\n" + parseAddress(info.address)
                                  + "\n" + str(info.port) + "\n" + str(data))
                        print(cur_str+'\n')
                        #conn.send(cur_str)
            if len(listener.all_del_sub)>0:
                    for x in listener.all_del_sub:
                        cur_str = x[9:21] + "\nDEL"
                        print(cur_str+'\n')
                        #conn.send(cur_str)
            time.sleep(0.5)
        except KeyboardInterrupt:
            break
            
def parseAddress(address):
    add_list = []
    for i in range(4):
        add_list.append(int(address.hex()[(i*2):(i+1)*2], 16))
    add_str = str(add_list[0]) + "." + str(add_list[1]) + "." + str(add_list[2])+ "." + str(add_list[3])
    return add_str

if __name__ == '__main__':
    mDNS()
