# norse



**N**an**O**op**R**e **SE**quencing 
GUI for data transfer to server


## Quick links
  * [Requirements](#requirements)
  * [Install norse](#install-norse)
  * [Usage](#basic-usage)

## Requirements





## Installation
### via conda:
+ conda installation here{link}

```shell=
# choose a suitable install location (e.g home dir)
git clone https://github.com/t3ddezz/norse.git
cd norse
# conda installation
conda env create -f environment.yml
conda activate norse
python setup.py install
````


```shell=
sudo apt-get install libxkbcommon-x11-0
sudo apt install libxcb-xinerama0
``` 


* Check if the install worked
  * Type (in the <strong>norse</strong> environment):

```
conda activate norse
norse -v
```

### via docker:
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


## Basic usage

2. Run `norse -r `

