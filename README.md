# Operating System Story Teller (OSST)

Because every server has a story — OSST listens and tells it.

Operating System Story Teller (OSST) is a lightweight CLI tool that tells the story of a Linux server by collecting and displaying key system information — CPU, memory, disk, running services, network interfaces, and open ports.

## Install

```bash
apt update
apt install make
apt install python3-pip
git clone https://github.com/r0gu3cic/osst.git
cd osst/
sudo make install
```

After install you can run the tool with  
`osst`

## Install from deb package

download deb file
sudo dpkg -i /root/osst/moj_deb_folder/python3-osst_0.1.0-1_all.deb

### notes for .deb file

sudo apt update
sudo apt-get install -y debhelper python3-all devscripts build-essential dh-python
git clone <https://github.com/r0gu3cic/osst.git>
cd osst/
python3 setup.py --command-packages=stdeb.command bdist_deb
mkdir -p moj_deb_folder
mv deb_dist/*.deb moj_deb_folder/
sudo dpkg -i /root/osst/moj_deb_folder/python3-osst_0.1.0-1_all.deb
osst

## Local development

To install dependacies use following command inside project root directory
`pip3 install -r requirements.txt`
To test run use inside project root directory
`python3 -m osst.__main__`
