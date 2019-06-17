##shell auto install
#! /bin/bash
if [ -f "./google-chrome.deb" ];then
  #statements
   echo "google-chrome.deb is exits"
else
  wget -O google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  ##install
  dpkg -i google-chrome.deb
fi
#sudo apt-get update
if [ -f "./chromedriver_linux64.zip"];then
  #statements
  echo "google-chrome.deb is exits"
else
  wget -O chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/75.0.3770.90/chromedriver_linux64.zip
  unzip ./chromedriver_linux64.zip
fi

sudo cp chromedriver /usr/bin

sudo rm chromedriver
sudo rm chromedriver_linux64.zip
sudo rm google-chrome.deb
