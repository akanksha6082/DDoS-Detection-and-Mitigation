import math
import sys

class CollectStats():
    
    def __init__(self) -> None:
        pass

    def get_count(self, flow_list):
        
        destination_count = {}
        src_dest_count = {}
        mac_ip = {}

        for flow in flow_list:

            dest = flow['dest_ip']
            src = flow['src_ip']

            if src == dest:
                continue
            
            #destination count
            if dest not in destination_count:
                destination_count[dest] = 0
            destination_count[dest] += 1

            #source-destination count
            if (src, dest) not in src_dest_count:
                src_dest_count[(src, dest)] = 0
            src_dest_count[(src, dest)] += 1

            #mac_ip mapping
            src_mac = flow['src_mac']
            dest_mac = flow['dest_mac']

            if src_mac not in mac_ip:
                mac_ip[src_mac] = {"source" : set(), "switch_port" : "none"}
            mac_ip[src_mac]['source'].add(src)
            

            if dest_mac not in mac_ip:
                mac_ip[dest_mac] = {"source" : set(), "switch_port" : "none"}
            mac_ip[dest_mac]['source'].add(dest)

        return (destination_count, src_dest_count, mac_ip)

    def get_adaptive_threshold_entropy(self,  destination_count, src_dest_count):
        
        threshold_dict = {}

        for current_dest in destination_count:
            threshold_dict[current_dest] = [destination_count[current_dest]]
            
        for tuple in src_dest_count:
            src, dest = tuple
            threshold_dict[dest].append([ src, src_dest_count[tuple]])

        dest_entropy = {}
        
        #destination entropy
        for dest in threshold_dict.keys():
            
            total_entropy = 0
            total_count = threshold_dict[dest][0]

            for index in range(1, len(threshold_dict[dest])):
                #calculate pi
                pi = threshold_dict[dest][index][1] /total_count
                total_entropy += pi * math.log(pi, 2)
            
            dest_entropy[dest] = -total_entropy
        
        #calculate mean and squared mean value
        c = 0
        c2 = 0

        for dest in destination_count:
            c += destination_count[dest]
            c2 += math.pow(destination_count[dest], 2)
        
        # total destination count
        total_dest_count = len(destination_count)
        
        # calulate standarad deviation and mean 
        mean = c / total_dest_count

        standard_deviation = math.sqrt((c2/total_dest_count) - (math.pow(mean, 2)))

        # threshold calculation
        window_threshold = mean + 3 * standard_deviation
        window_entropy = 0

        # calculation of window entropy
        for entropy in dest_entropy.values():
            window_entropy += entropy
        
        return(window_threshold, window_entropy)
            
    
    def get_mac_ip(self):
        pass

        

    
