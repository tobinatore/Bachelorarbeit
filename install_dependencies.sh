#!/bin/bash

# Printing the setup text
echo '---------------------------------------------------'
echo '             _____      _                          '
echo '            /  ___|    | |                         '
echo '            \ `--.  ___| |_ _   _ ____             '
echo '             `--. \/ _ \ __| | | |  _ \            '
echo '            /\__/ /  __/ |_| |_| | |_) |           '
echo '            \____/ \___|\__|\__,_| .__/            '
echo '                                 | |               '
echo '                                 |_|               '
echo '---------------------------------------------------'

echo 'Installing dependencies...'

echo "======================="
echo "Getting konsole"
echo "======================="
echo " "
sudo apt install -y konsole keditbookmarks git

echo "==============="
echo "Setting up DTN"
echo "==============="
echo " "

echo "Checking for installed DTN..." 
ionstart -I test.rc 1> /dev/null
if [ $? -eq 0 ]
then    echo -e "\e[32mION already installed!" 
        directory=$(find / -type d -name "ion*4.0.0" -print -quit)
        pwd
        find ~/ -type d -name "ion*4.0.0"
else
    echo -e "\e[31mION not already installed!"
    echo -e "\e[39mInstalling ION-DTN."

    echo "Do you wish to run sudo apt update first?" 
    select yn in "Yes" "No"; do
        case $yn in
            Yes ) sudo apt update; break;;
            No ) echo "Skipping sudo apt update.";break;;
        esac
    done
    echo "Installing package build-essential..."
    apt install build-essential -y 1> /dev/null
    echo "Downloading build 4.0.0 of ION-DTN... "
    wget https://sourceforge.net/projects/ion-dtn/files/ion-4.0.0.tar.gz/download
    echo "Extracting files... "
    tar xzf download
    rm download
    echo "Changing directories -> ion-4.0.0/... "
    cd ion-open-source-4.0.0
    echo "Installing... "
    ./configure
    make
    sudo make install
    sudo ldconfig
    echo -e "\e[32mFinished installing ION-DTN."
    echo -e "\e[39mPlease set the ION_HOME environment variable to:"
    directory=$(pwd)
    echo $directory
    cd ..
fi

echo -e "\e[39m==============="
echo "Getting Python packages"
echo "==============="
echo " "
sudo apt install autotools-dev automake python3-dev python3-pip
pip3 install apscheduler cbor2 psutil

echo "Done."
echo ""
echo "Please run sudo gedit /etc/environment and add the line ION_HOME=$directory."
echo "After that you can run install_pyion.sh to install the pyion python package."

