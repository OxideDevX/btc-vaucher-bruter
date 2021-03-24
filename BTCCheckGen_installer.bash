apt update -y && apt upgrade -y
apt install git python -y
pip install requests
git clone https://github.com/OxideDevX/btc-vaucher-bruter.git
cd BTCVoucherGen
python BTCCheckGen.py