from genie import testbed

# Transform .txt output (file) into a string to be parsed by pyATS
with open('LER.IPv4.txt', 'r') as file:
    data = file.read().rstrip()

# Load testbed
testbed = testbed.load('./testbed.yaml')
ios1 = testbed.devices["ios1"]

# Parse output
ip_route = ios1.parse('show ip route', output=data)

for prefix in ip_route['vrf']['default']['address_family']['ipv4']['routes']:
    print(f" advertised {prefix}")
    print(" origin igp")
    print(" nexthop")
    print(" aspath")
    print(" timestamped 1511540052 387402")
    print()
