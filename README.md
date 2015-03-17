# tellme
Very simple sensor logger and viewer for Tellstick Live devices

##Description

| File | Comment |
| ---- | ------- |
| | |

##Usage
Install the following dependencies
`sudo apt-get install python-oauth python-configobj pyhton-pip`

`sudo pip install tabulate`

Add cron job, run every 5th minute (Telldus Live free account polls sensors every 10th minute)

`\#   */5 *  *   *   *     PYTHONIOENCODING=utf-8 <path-to-tellme>/tdtool.py --list sensors | grep "^[^N[:space:]\-]" >> <path-to-tellme>/data.txt`

## References
* Telldus Live
* Flot
