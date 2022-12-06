# rib2routem
Python tool to convert IOS-XR RIB to routem configuration file for easy replay in the lab. It leverages Cisco pyATS to parse IOS-XR RIB output.
## Introduction
In order to test router's FIB, a common technique is to use a traffic generator such IXIA or Spirent and generate prefixes. While this is fast and easy to do, this doesn't represent customers' network reality.  
rib2routem is a tool used to:
- parse a production router RIB (show route ipv4 unicast, show route ipv6 unicast)
- extract prefixes, next-hop
- generate a routem configuration file to replay the RIB in a lab

## routem
routem is an old-school and proprietary Cisco tool to generate control plan. If you search hard enough on Internet, you'll find copies.
routem can be configured to replay a RIB, using ASCII file. In this mode, 2 configuration files are required.

### Establishing BGP peering with routem
RIB is replayed via a simple BGP session between SUT and routem. Following sample configuration is used for IPv4 unicast:

```
router bgp 65537
bgp_id 1.63.51.21
neighbor 1.63.51.51 remote-as 65537
neighbor 1.63.51.51 update-source 1.63.51.21
capability ipv4 unicast
capability refresh
capability 4bytes-as
replay file LER.IPv4.cfg ascii
```

Note the last line of this configuration file: this is where prefixes are stored.

### Replay prefixes

The replay file has following minimal format and requires BGP mandatory attributes:

```
 advertised 1.0.0.0/24
 origin igp
 aspath
```
next-hop inherits neighbor IP.

### RIB input

RIB is collected from customer's network with CLI. Output is stored in a txt file. genie offline parsing capacity is used to extract prefixes, next-hop, etc. The tools supports both IPv4 and IPv6. See https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers/show%2520route%2520ipv4 and https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers/show%2520route%2520ipv6.


## Generating routem replay file: rib2routem utilisation

1. Get 'show route ipv4 unicast' or 'show route ipv6 unicast' output and store it in a .txt file
2. Edit both python files to point to the .txt file location
3. Execute rib2routem and redirect to a file
```
python3 rib2routem.py > LER-v4.cfg
```

## Todo
- One file to handle both IPv4 and IPv6.
- Add next-hop support

## Acknowledgements
I'd like to thanks Antoine Orsoni for his support. You can check Antoine's work on xrdocs.io website: https://xrdocs.io/programmability/tutorials/pyats-series-parsing-like-a-pro/

