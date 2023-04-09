# Problem Statement

This program will calculate the average of Received Signal Strength (RSS) which is collected from the access point and host.

In WLAN, Received Signal Strength (RSS) is an important metric used to determine the quality of the wireless connection 
between a device and an access point. A strong RSS value indicates a good signal quality, while a weak RSS value indicates 
poor signal quality or a weak connection. It is also used to diagnose wireless network performance problems and optimize wireless 
network deployment. The RSS value can changed in every second. Therefore, the 30 second or 60 second rss data is the best option
to measure the signal quality between Acess point and user. Here, AP means router and user means laptop, PC, laptop.

The RSS is collected using the **iperf** the command and data is stored in .txt file. The .txt file include string and integer but
we need only integer value to calculte the average of these value because this integer value refers to the power level of the 
signal received by a wireless device, such as a laptop or smartphone, from an access point (AP) or router.

This program  meets  the following conditions
1. Use Python, and implement in an object-oriented manner.
2. Use a thread pool
3. must be abel to confrim that it is thread-safe.


# Details of the repository

1. The folder conatin the **main.py** program, **dataset** folder.
2. The **dataset** folder contains the sample input data which is collected by user from an AP using iperf command.


# How to run this repository

1. To use this project, clone the repository by following command: 
```sh
git clone https://github.com/Sujan-Roy/QibiTech-Assignment-01.git
```
2. After cloning, using the command prompt, go to the project directory and run **python main.py**.
Firstly, make sure you have installed latest python version 3.10 on your system.
3. The **Extract_Data_directory** folder will generate by the program which conatin only integer 
    data which is separtred from the Input **dataset** folder.
4. Finally, the program will display the output (Average of the RSS).