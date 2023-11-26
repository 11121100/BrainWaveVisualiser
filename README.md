BrainWaveVisualiser
===================

A project involving NeuroSky Mindwave (EEG), Raspberry Pi (SOC) and ApexCharts (GUI) to efficiently visualise Brain Wave activities in real-time.

| Linux  | Raspberry Pi | Windows |
| ------ | ------------ | ------- |
|        |              |         |


Python Version Support
----------------------

**This project is only supported by Python 3 (tested under 3.7).** Contributions are strongly desired to resolve compatibility problems on newer systems, address bugs, and improve platform support for various features.


### Dependencies & Inclusions:

-   [PyBluez](https://github.com/pybluez/pybluez) -
    The PyBluez module allows Python code to access the host machine's Bluetooth resources.
-   [Flask](https://flask.palletsprojects.com/en/3.0.x/) -
    Flask is a small and lightweight Python web framework allows creating web applications in Python.
-   [psutil](https://pypi.org/project/psutil/) -
    psutil is a cross-platform library for retrieving information on CPU, memory, disks, network, sensors) in Python. 
-   [python-mindwave-mobile](https://github.com/robintibor/python-mindwave-mobile) -
    Scripts to read data out of the Neurosky Mindwave Mobile unter Linux.
-   [apexcharts.js](https://github.com/apexcharts/apexcharts.js) -
    A modern JavaScript charting library that allows you to build interactive data visualizations with simple API.

### Known Bugs:

-   Intermittent Bluetooth Connectivity Dropout
-   Ajax Response DataType Mismatch on Raspbian
-   Python Queue managment inefficient and lagging


Installation
------------

Please refer to the instructions below.
-   Install Python 3.7 (tested version)
-   Install Chrome Browser (tested version)
-   py -3.7 -m pip install Flask
-   py -3.7 -m pip install psutil
- 	py -3.7 -m flask --app piserver run (launch)
-   On Browser, type url: "http://localhost:5000/dashboard"

License
-------

> BrainWaveVisualiser is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

> BrainWaveVisualiser is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

> You may have received a copy of the GNU General Public License along with BrainWaveVisualiser code package when cloning this repository.

