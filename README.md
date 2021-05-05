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
2. Only for Linux if not working:
```shell=
sudo apt-get install libxkbcommon-x11-0
sudo apt install libxcb-xinerama0
```



### Install norse
```shell=
cd norse
conda env create -f environment.yml
conda activate norse
python setup.py install
```



### Check the install worked

Type (in the <strong>norse</strong> environment):

```
norse -v
```

### Basic usage

1. Activate the virtual environment ``conda activate norse``
2. Run ``norse -r``



