# Operating System Story Teller (OSST)

Operating System Story Teller (OSST) is a lightweight CLI tool that tells the story of a Linux server by collecting and displaying key system information such as CPU, memory, disk, running services, network interfaces, and open ports.

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

## Local development

To install dependacies use following command inside project root directory
`pip3 install -r requirements.txt`
To test run use inside project root directory
`python3 -m osst.__main__`
