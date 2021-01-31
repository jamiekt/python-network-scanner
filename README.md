All based upon https://levelup.gitconnected.com/writing-a-network-scanner-using-python-a41273baf1e2


1. Setup a virtualenv
```bash
python3 -m venv venv
```

2. Activate it
```bash
source venv/bin/activate
```

3. Install dependencies
```bash
pip install scapy
```

4. run it
Can't use sudo inside a venv so deactivate the venv
```bash
deactivate
```
then use that python interpreter
```bash
sudo ./venv/bin/python network_scanner.py -t 172.23.198.251
```
or
```bash
sudo ./venv/bin/python network_scanner.py -t 172.23.198.251/24
```
