batch_check_heartbleed
======================

A tiny Python script to "batch check" your hosts if they are affected by HEARTBLEED

Requirements
============

* This script has been tested on Linux __ONLY__
* You will need a recent version of Nmap (tested: Nmap 6.40) on your machine
* This script is (obviously) written in Python so you will also need Python2.7
* Nmap is invoked with an additional LUA script you can find it
 * Here: http://nmap.org/nsedoc/lib/tls.html
 * Copy the script in LUA's nselib folder, i.e. __/usr/share/nmap/nselib/__

Usage
=====

* Clone this repository
* Firstly, fill the hosts.cfg as exemplarily shown in the hosts.cfg in this repo
 * Make sure you use unique ids
* Secondly in the cloned folder, this is important because the script assumes
that the hosts.cfg and the *.nse file reside next to it, invoke:

* `python heartbleed_check.py`

* The output of this script is straight forward, it reports VULNERABLE hosts at the
end (if found)
* IMPORTANT: If you check against hosts that don't have an SSL port open you will get a 
__false positive__, same goes for hosts which are unreachable.
