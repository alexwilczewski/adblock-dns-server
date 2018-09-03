# Credit
Original design and development created by ragibkl. See [the original Github](https://github.com/ragibkl/adblock-dns-server)

---
---

# Adblock DNS Server
Adblocking DNS server using bind service. The service is run inside a docker container.

## Overview
This project is created to help block Ads, at the DNS resolution level.
Using this project, you can quickly bring up a caching DNS server that also redirects Ads to a dead IP.
If you use this DNS server on your devices/wifi-router instead of your ISP's or other regular DNS servers (Google, OpenDNS), Ads wil be blocked.

## Requirements
To run this project, make sure your system/server has the following packages installed: 
- docker

## Running the server
Follow these steps to get this project up and running.

1. Clone this project   
   `git clone https://github.com/alexwilczewski/adblock-dns-server.git`

2. cd into the cloned project.  
   `cd adblock-dns-server`   

3. build the docker container  
   `sudo docker build -t adblock/bind:latest docker-bind`

4. run the container  
   `./load-container.sh`

5. update blacklist  
   `sudo docker exec adblockdns update`

6. do a quick test   
    ```shell
    # tests dns lookup against Google's dns server
    # should return regular/valid response
    $ nslookup zedo.com 8.8.8.8
    Server:		8.8.8.8
    Address:	8.8.8.8#53
    
    Non-authoritative answer:
    Name:	zedo.com
    Address: 64.41.197.44
    
    # tests dns lookup against our adblock dns server
    # should return our server's IP instead
    $ nslookup zedo.com X.X.X.X
    Server:		X.X.X.X
    Address:	X.X.X.X#53
    
    Non-authoritative answer:
    Name:	zedo.com
    Address: X.X.X.X
    ```

7. stopping the container  
    `sudo docker stop adblockdns`

## Configuring your device

### Short version
Option 1: WiFi Router level
- Affects all devices connected to said router.
- Instructions: 
    - Go to your router admin page, under WAN settings.
    - Edit DNS settings. Use your adblock-dns server's IP address instead of Automatic or Google's (8.8.8.8, 8.8.4.4)

Option 2: Personal Computer level
- Affects single device.
- Instructions: 
    - Go to your computer's network setting.
    - Change DNS settings. Use your adblock-dns server's IP address instead of Automatic or Google's (8.8.8.8, 8.8.4.4)
    
### Detailed tutorial
https://blog.bancuh.com/?p=71


## Contributing
This project could use some improvements and help in many areas, which includes, documentation, testing, code improvement, and deployment implementations.

If you have any suggestions, or would like to report and problem, create a Github issue to grab my attention.
