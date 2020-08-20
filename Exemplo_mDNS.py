# -*- coding: utf-8 -*-
""" Model of a mDNS Service.

    This file has a generic implementation of a zeroconf mDNS service.
    :Author: Leonardo B.
"""
import time
from multiprocessing import Process, Pipe
from zeroconf import ServiceBrowser, Zeroconf

class MyListener(object):
    """
    This class is used for the mDNS browsing discovery device, 
    including calling the remove_service and add_service
    properties to ServiceBrowser, and also contains broadcasts 
    for querying and updating existing devices.
    
    Attributes
    ----------
    self.all_info_dict: dict
            Device information recovered from itself mDNS service.
    
    Methods
    -------
    remove_service(self, zeroconf, type, name)
        Remove a disconnected device
    add_service(self, zeroconf, type, name)
        Add a connected device.
    update_service(self, zeroconf, type, name)
        Update connected device information.
    """

    def __init__(self):
        self.all_del_sub = []
        self.all_info_dict = {}
        self.all_sub_num = 0
        self.new_sub = False

    def remove_service(self, zeroconf, type, name):
        """ This function is called for ServiceBrowser.
        
        This function is triggered when ServiceBrowser 
        discovers that some device has logged out.
        Parameters
        ----------
        zeroconf : Zeroconf
        type : str
        name : str
            all above parameters are inherited from ServiceBrowser.
        """
        if name not in self.all_info_dict:
            return
        self.all_sub_num -= 1
        del self.all_info_dict[name]
        self.all_del_sub.append(name)

    def add_service(self, zeroconf, type, name):
        """ This function is called for ServiceBrowser.
        
        This function is triggered when ServiceBrowser 
        finds a new device. When a subdevice is found, 
        the device information is stored into the all_info_dict.
        Parameters
        ----------
        zeroconf : Zeroconf
        type : str
        name : str
            all above parameters are inherited from ServiceBrowser.
        """
        self.all_sub_num += 1
        info = zeroconf.get_service_info(type, name)
        self.all_info_dict[name] = info
        if name in self.all_del_sub:
            self.all_del_sub.remove(name)

    def update_service(self, zeroconf, type, name):
        """ This function is called for ServiceBrowser.
        
        This function is triggered when ServiceBrowser 
        finds a new info from a known device.
        Parameters
        ----------
        zeroconf : Zeroconf
        type : str
        name : str
            all above parameters are inherited from ServiceBrowser.
        """
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
