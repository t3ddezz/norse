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
#### via conda:

```shell=
cd norse
conda env create -f environment.yml
conda activate norse
python setup.py install
````

Only for Linux if its not working:
```shell=
sudo apt-get install libxkbcommon-x11-0
sudo apt install libxcb-xinerama0
``` 

#### via docker:
```
# clone git repository and navigate into the dir
git clone https://github.com/t3ddezz/norse.git && cd norse

# create docker image via
docker build -t norse:build .

# run docker image via (port mapping is missing here!!!)
docker run --rm \
  -u qtuser \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -e DISPLAY=unix$DISPLAY \
  norse:build \
  /norse/norse/norse_script.py -r
```



### Check the install worked

Type (in the <strong>norse</strong> environment):

```
norse -v
```

### Basic usage

1. Activate the virtual environment ``conda activate norse``
2. Run ``norse -r``



