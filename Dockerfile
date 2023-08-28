FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# Add user
RUN adduser --quiet --disabled-password qtuser && usermod -a -G audio qtuser

# This fix: libGL error: No matching fbConfigs or visuals found
ENV LIBGL_ALWAYS_INDIRECT=1

# Install Python 3, PyQt5
RUN apt-get update && apt-get install -y python3-pyqt5 \
					git \
					python3-pip \
					libxkbcommon-x11-0 \
					libxcb-xinerama0 \
					rsync \
					ssh-askpass-gnome \
					ssh-askpass \
					sshpass

RUN pip3 install install pandas requests paramiko openpyxl xlrd  argparse

RUN mkdir -p norse
COPY . norse/
RUN cd norse && python3 setup.py install

RUN mkdir -p /tmp/runtime-qtuser && chmod 777 /tmp/runtime-qtuser && chown qtuser /tmp/runtime-qtuser
ENV XDG_RUNTIME_DIR='/tmp/runtime-qtuser'

