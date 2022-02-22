"""
A packet analyzing POX component.
Add this file in pox/ext folder.
run pox controller as ./pox.py entropy_detection
change the location of the file
"""

# Import some POX stuff
from time import sleep
from pox.core import core                     # Main POX object
import pox.openflow.libopenflow_01 as of      # OpenFlow 1.0 library
import pox.lib.packet as pkt                  # Packet parsing/construction
from pox.lib.addresses import EthAddr, IPAddr # Address types
import pox.lib.util as poxutil                # Various util functions
import pox.lib.revent as revent               # Event library
import pox.lib.recoco as recoco               # Multitasking library
import requests, json, signal
from pox.lib.revent import *
from collect_stats import CollectStats

# Create a logger for this component
log = core.getLogger()

class EntropyDetection(EventMixin):
    
    def __init__(self):
        self.listenTo(core)
        self.listenTo(core.FlowCollector)
        self.window_count = 1
   
    def _handle_WindowFull(self, event):
        print("entropy detection window : {0}".format(self.window_count))
        
        collect_stats = CollectStats()
        destination_count, src_dest_count, mac_ip = collect_stats.get_count(event.flow_list)
        
        print(destination_count)
        print(src_dest_count)
        print(mac_ip)

        #send to calculate the adaptive threshold
        #send to calculate entropy
        #detect
        #mitigate karaychay
        
        self.window_count += 1

def launch():
    core.registerNew(EntropyDetection)