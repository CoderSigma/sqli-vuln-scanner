<h1 align="center">
  <br>
  Yet another lightweight tool to test an SQL Injection Vulnerability.
  <br>
</h1>

#### Installation and Usage:

Copy-paste this into your terminal:

```
git clone https://github.com/CoderSigma/sqli-vuln-scanner.git
```
```
cd sqli-vuln-scanner
```
```
python3 vuln.py -h
```

#### Usage
```
usage: vuln.py [-h] -u URL -p PAYLOADS

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     url
  -p PAYLOADS, --payloads PAYLOADS
                        payloads list
```

#### Example Usage
```

python3 vuln.py -u https://site.com/index.php?id=1{fuzz} -p payload.txt
```
