# tellme
Very simple sensor logger and viewer for Tellstick Net devices

##Description
The Tellstick Net wireless home automation devices communicate data to the Telldus Live service. The Telldus Live service does not provide any sensor logging functionality, only the last reading is available through the web GUI. These scripts communicate with the Telldus Live API and poll, store and display the sensor history for a registered user.

The display of the data is web based and uses the Flot charts framework; this means access to visual treats like e.g. detailed data on mouse-over, zooming into selected areas in the graph and extensive customization capabilities...

| File | Comment |
| ---- | ------- |
| tdtool.py | Script enabling Telldus Live API communication |
| data.txt | Raw sensor data file, human readable, would benefit from some compression |
| flot-filter.py | Script that massages the data.txt file ito something that Flot charts can consume |
| data-temperature.json | Filtered sensor data file |
| data-humidity.json | Filtered sensor data file |
| index.html | Contains the flot charts configuration |
| main.css | Self explanatory |

##Usage
1. Install the following dependencies

  `sudo apt-get install python-oauth python-configobj pyhton-pip`

  `sudo pip install tabulate`

2. Run tdtool.py manually to complete the authentication process and accuire the appropriate user keys. 

3. Add cron job, run every 5th minute (Telldus Live free account polls sensors every 10th minute)

  `\#   */5 *  *   *   *     PYTHONIOENCODING=utf-8 <path-to-tellme>/tdtool.py --list sensors | grep "^[^N[:space:]\-]" >> <path-to-tellme>/data.txt`

4. Install and configure a web server of choice to serve the `index.html`, `main.css` and `data-*.json` files

## References
* [Tellstick Net](http://www.telldus.se/products/tellstick_net)
* [Telldus Live](http://live.telldus.com/)
* [Telldus Live API](https://api.telldus.com/)
* [Original tdtool.py implementation](http://developer.telldus.com/browser/examples/python/live/tdtool/tdtool.py?rev=a35ad875d20fd8935be7c87426ab33cc231528f7)
* [Flot](http://www.flotcharts.org/)
