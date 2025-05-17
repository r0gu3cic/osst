# Operating System Story Teller (OSST)

## TODO elaborate more on tool

Because every server has a story — OSST listens and tells it.

Operating System Story Teller (OSST) is a lightweight CLI tool that tells the story of a Linux server by collecting and displaying key system information — CPU, memory, disk, running services, network interfaces, and open ports.

local development
pip3 install -r requirements.txt
test python3 -m osst.__main__

install one way
sudo make install from project root dir

install other way
notes for .deb file
user@server:~/osst/deb_dist$ history | grep install
   20  sudo apt install python3-stdeb fakeroot
   30  sudo apt install -y python3-all debhelper fakeroot build-essential
   34  sudo apt install dh-python
   36  pip3 install -r requirements.txt
   37  sudo apt install python3-pip
   38  pip3 install -r requirements.txt
   41  sudo apt install python3-psutil
   62  history | grep install
