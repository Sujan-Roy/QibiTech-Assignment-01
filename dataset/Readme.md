# ReadMe.
This folder conatins the RSS in text file.
This data is collected using iperf command in linux.
# Iperf 
Iperf is a commonly used tool for measuring network performance, including the received signal strength. To use Iperf to collect received signal strength data, you can follow these steps:

1. Install Iperf: If you haven't already done so, you'll need to install Iperf on the device that will be receiving the signal. Iperf is available for various platforms, including Windows, macOS, and Linux.

2. Connect to the network: Connect the device to the network whose signal strength you want to measure. Ensure that the device is positioned in the location where you want to measure the signal strength.

3. Run Iperf in server mode: On the device that will be sending the signal, run Iperf in server mode by entering the following command in a terminal or command prompt window
# Syntax
iperf -s

This will start Iperf in server mode and listen for incoming connections.

4. Run Iperf in client mode: On the device that will be receiving the signal, run Iperf in client mode by entering the following command in a terminal or command prompt window:
# Syntax
iperf -c [server IP address]

Replace [server IP address] with the IP address of the device running Iperf in server mode. This will start Iperf in client mode and initiate a connection to the server.

5. Monitor signal strength: As Iperf runs, it will display the measured network performance metrics, including the received signal strength. You can monitor the signal strength data as it is displayed in the Iperf output. The received signal strength is typically measured in units of dBm (decibels relative to one milliwatt).


