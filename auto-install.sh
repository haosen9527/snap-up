##shell auto install
#! /bin/bash
if [ -f "./google-chrome.deb" ];then
  #statements
   echo "google-chrome.deb is exits"
else
  wget -O google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
fi
##install
sudo dpkg -i google-chrome.deb
sudo apt-get update
if [ -f "./chromedriver_linux64.zip"]; then
  #statements
else
  wget -O chromedriver_linux64.zip http://172.20.216.118/files/207200000031BCB1/npm.taobao.org/mirrors/chromedriver/71.0.3578.137/chromedriver_linux64.zip
fi
unzip ./chromedriver_linux64.zip

sudo cp chromedriver /usr/bin

sudo rm chromedriver
sudo rm chromedriver_linux64.zip
sudo rm google-chrome.deb
