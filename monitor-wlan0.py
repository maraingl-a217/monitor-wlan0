import subprocess
import optparse
import re

subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("iwconfig wlan0 mode monitor", shell=True)
subprocess.call("airmon-ng check wlan0", shell=True)
subprocess.call("airmon-ng check kill", shell=True)
