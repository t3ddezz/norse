# norse



**N**an**O**op**R**e **SE**quencing 
GUI for data transfer to server


## Quick links
  * [Requirements](#requirements)
  * [Install norse](#install-norse)
  * [Check the install worked](#check-the-install-worked)
  * [Usage](#basic-usage)

### Requirements

norse runs on MacOS and Linux(if not working isntall following libaries)
1. A conda version. Can be downloaded from [here](https://www.anaconda.com/products/individual)




### Install norse
```shell=
cd norse
conda env create -f environment.yml
conda activate norse
python setup.py install
````

Only for Linux if not working:
```shell=
sudo apt-get install libxkbcommon-x11-0
sudo apt install libxcb-xinerama0
``` 
via docker:
````
FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# Add user
RUN adduser --quiet --disabled-password qtuser && usermod -a -G audio qtuser

# This fix: libGL error: No matching fbConfigs or visuals found
ENV LIBGL_ALWAYS_INDIRECT=1

# Install Python 3, PyQt5
RUN apt-get update && apt-get install -y python3-pyqt5 git python3-pip

RUN pip3 install install  pandas requests paramiko openpyxl xlrd  argparse

RUN git clone -b docker_testing  https://github.com/t3ddezz/norse.git
RUN chmod 777 /norse/norse/norse_script.py
```



### Check the install worked

Type (in the <strong>norse</strong> environment):

```
norse -v
```

### Basic usage

1. Activate the virtual environment ``conda activate norse``
2. Run ``norse -r``



