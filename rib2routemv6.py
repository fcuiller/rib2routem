from genie import testbed

# Transform .txt output (file) into a string to be parsed by pyATS
with open('LER.IPv6.txt', 'r') as file:
    data = file.read().rstrip()

# Load testbed
testbed = testbed.load('./testbed.yaml')
iosxr1 = testbed.devices["iosxr1"]

# Parse output
ip_route = iosxr1.parse('show route ipv6', output=data)

for prefix, details in ip_route['vrf']['default']['address_family']['ipv6']['routes'].items():
        print(f" mbgp_reach network {prefix}")
        print(" origin igp")
        print(" mbgp_reach unicast ipv6")
        print(" mbgp_reachnexthop")
        print(" aspath")
        print(" timestamped 1511540052 387402")
        print()
