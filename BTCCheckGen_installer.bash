#!/bin/bash
echo "Hi! I will install this script in semi-automatic mode."
echo "Привет! Я установлю этот скрипт в полуавтоматическом режиме".
sleep 1
apt update -y && apt upgrade -y
apt install git python -y
pip install requests
git clone https://github.com/OxideDevX/btc-vaucher-bruter.git
cd BTCVoucherGen
python BTCCheckGen.py
