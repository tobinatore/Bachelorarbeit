#!/bin/bash

echo "Fetching git repository at https://github.com/msancheznet/pyion.git..."
git clone https://github.com/msancheznet/pyion.git
echo "Changing directories -> /pyion..."
cd pyion
git checkout v4.0.0
echo "Installing pyion locally..."
sudo -E python3 setup.py install
echo -e "\e[32mDone."
echo -e "\e[39m"
