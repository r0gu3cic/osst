# Operating System Story Teller (OSST)

## TODO elaborate more on tool

Because every server has a story — OSST listens and tells it.

Operating System Story Teller (OSST) is a lightweight CLI tool that tells the story of a Linux server by collecting and displaying key system information — CPU, memory, disk, running services, network interfaces, and open ports.

### local development
pip3 install -r requirements.txt
test python3 -m osst.__main__

### install one way
sudo make install from project root dir
git clone https://github.com/r0gu3cic/osst.git
apt update
apt install make
apt install python3-pip
cd osst/
make install
osst = works

### install other way
download deb file
sudo dpkg -i /root/osst/moj_deb_folder/python3-osst_0.1.0-1_all.deb
#### notes for .deb file
sudo apt update
sudo apt install -y python3-stdeb python3-pip dh-python python3-all python3-setuptools python3-stdeb debhelper build-essential
sudo apt install python3-psutil
git clone https://github.com/r0gu3cic/osst.git
cd osst/
python3 setup.py --command-packages=stdeb.command bdist_deb
mkdir -p moj_deb_folder
mv deb_dist/*.deb moj_deb_folder/
sudo dpkg -i /root/osst/moj_deb_folder/python3-osst_0.1.0-1_all.deb
osst = works
