# Generate SCP Command faster for transfer files quickly

### Installation
Python3 is required to be installed in system, with path it's path added.
then run,
`sudo curl -o /usr/bin/gen-scp https://raw.githubusercontent.com/imdrr30/gen-scp/master/gen-scp.py`

### Usage
Output format
```scp <username>@<publicip>:<files/abosulte/path/in/server> .```

```
>gen-scp backup.zip
scp username@123.123.123.123:/home/username/backup.zip .
```