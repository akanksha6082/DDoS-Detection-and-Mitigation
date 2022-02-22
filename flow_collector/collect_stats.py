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
            dest_mac =flow['dest_mac']

            if src_mac not in mac_ip:
                mac_ip[src_mac] = {"source" : set(), "switch_port" : "none"}
            mac_ip[src_mac]['source'].add(src)
            
            if dest_mac not in mac_ip:
                mac_ip[dest_mac] = {"source" : set(), "switch_port" : "none"}
            mac_ip[dest_mac]['source'].add(dest)

        return (destination_count, src_dest_count, mac_ip)

               
    def get_adaptive_threshold(self):
        pass

    def get_entropy(self):
        pass
    
    def get_mac_ip(self):
        pass
        

    
