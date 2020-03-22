Instructions when doing in a new installation
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-dev python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel
sudo pip3 install Adafruit_DHT

sudo apt-get install build-essential python3-dev python3-smbus git
cd ~
git clone https://github.com/adafruit/Adafruit_Python_MCP3008.git
cd Adafruit_Python_MCP3008
sudo python setup.py install
sudo apt-get update
sudo apt-get install build-essential python3-dev python3-smbus python3-pip
sudo pip3 install adafruit-mcp3008
//Activate SPI and I2C doing sudo raspi-config
//reboot
python3 main.py

https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/
https://github.com/shubham0490/MQ-sensor-ppm-conversion
