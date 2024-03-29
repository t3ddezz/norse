# norse

##  **N**an**O**po**R**e **SE**quencing 
GUI for nanopore data transfer to a server and sample informations. All informations are collected in a `run_info.txt` file that is stored with the uploaded data.

![screen](data/interface.png)

## Content
  * [Install norse](#installation)
    * [via conda](#via-conda:)
    * [via docker](#via-docker:)
  * [Usage](#basic-usage)


## Installation
### via conda:
+ conda installation [here](https://docs.conda.io/en/latest/miniconda.html#system-requirements)

```shell=
# choose a suitable install location (e.g home dir)
git clone https://github.com/t3ddezz/norse.git
cd norse
# conda installation
conda env create -f environment.yml
conda activate norse
python setup.py install
````

* Troubleshooting with this error: "This application failed to start
because no Qt platform plugin could be initialized. 
Reinstalling the application may fix this problem.
Available platform plugins are: eglfs, linuxfb,xcb."

  * then try this:

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
  --network host \
  -v $HOME:/home/qtuser \
  -v $PWD:/upload \
  norse:build \
  norse -r
```
**or**
use the newest docker from [dockerhub](https://hub.docker.com/repository/docker/dataspott/norse/general):
```
# run docker image from dockerhub (insert respective VERSION)
docker run --rm \
  -u qtuser \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -e DISPLAY=unix$DISPLAY \
  --network host \
  -v $HOME:/home/qtuser \
  -v $PWD:/upload \
  dataspott/norse:VERSION \
  norse -r
```

## Basic usage

Run `norse -r` to start the program or `norse -v` to show the program version.

