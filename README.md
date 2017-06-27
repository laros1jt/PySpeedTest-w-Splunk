# PySpeedTest-w-Splunk

#1. Install fopina's pyspeedtest
sudo pip install pyspeedtest

#2. Place speedtestwrapper.py in /var/log/speedtest/

#3. Add the following entry to crontab ("crontab -e")
*/15 * * * * /usr/bin/python2.7 /var/log/speedtest/speedtestwrapper.py &>> /var/log/speedtest/speedtest.log

#4. Place inputs.conf, props.conf, and internet_speed.xml in the approriate directories for your Splunk instance

#5. Create a 'speedtest' index or modify inputs.conf to store events in a custom index
