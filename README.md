TO DO
-----
Rewrite the p2pool in either Rust or Golang:
 * using modern **bitcoinrpc library** 
 * implement the **Stratum Protocol V2**
 * implement support for more shares announcement channels
    which includes social media (bots) and mail
 * implement support for unix domain sockets for reverse proxy
 * Front End Web
    * Boostrap Update
    * _Polling for certain server information such as network bandwidth via  API_  
</br>
</br>    


Requirements:
-------------------------
Generic:

* Qnodecoin >=2.0
* Python >=2.7
* Twisted >=13.0.0
* Zope.interface >=3.8.0

Linux:

    sudo apt-get install python-zope.interface python-twisted python-twisted-web python-dev
    sudo apt-get install gcc g++

Install Python modules:
-------------------------

qnodecoin_hash:

    cd qnodecoin_hash
    python setup.py install --user

Running P2Pool:
-------------------------
To use P2Pool, you must be running your own local qnodecoind. For standard
configurations, using P2Pool should be as simple as:

    python run_p2pool.py --p2pool-port <PORT_NUMBER>

Then run your miner program, connecting to 127.0.0.1 on port 7903 with any
username and password.

If you are behind a NAT, you should enable TCP port forwarding on your
router. Forward port 9998 to the host running P2Pool.
</br>
Run for additional options:

    python run_p2pool.py --help

Official wiki :
-------------------------
https://en.bitcoin.it/wiki/P2Pool

Alternate web front end :
-------------------------
* https://github.com/hardcpp/P2PoolExtendedFrontEnd
* https://github.com/johndoe75/p2pool-node-status
* https://github.com/justino/p2pool-ui-punchy

Sponsors:
-------------------------

Thanks to:
* The Bitcoin Foundation for its generous support of P2Pool
* The Litecoin Project for its generous donations to P2Pool
* The Vertcoin Community for its great contribution to P2Pool
* jakehaas, vertoe, chaeplin, dstorm, poiuty, elbereth  and mr.slaveg from the Darkcoin/Dash Community
* The Dash Project
