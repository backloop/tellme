# tellme
Very simple sensor logger and viewer for Tellstick Live devices

##Description

| File | Comment |
| ---- | ------- |
| | |

##Usage
Install the following dependencies
`sudo apt-get install python-oauth python-configobj pyhton-pip
 sudo pip install tabulate`

# Add cron job, run every 5th minute (Telldus Live free account polls sensors every 10th minute)
#   */5 *  *   *   *     PYTHONIOENCODING=utf-8 /home/backloop/telldus/tdtool.py --list sensors | grep "^[^N[:space:]\-]" >> /home/backloop/telldus/data.txt

## References
* Telldus Live
* Flot
