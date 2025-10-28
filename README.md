# Dynamic Governor

A python script that will dynamically set your CPU governor to 'powersave' or
'performance' depending on the load average. This lets you save on power when
doing low compute tasks while letting you get the most performance out of your
cpu when under heavy load.

# Modifying the thresholds
In the top of the script `dynamic-governor.py` there are two variables
`LOAD_THRESHOLD` and `CHECK_INTERVAL`.

When `/proc/loadavg` is less than or equal to `LOAD_THRESHOLD` the CPU governor will be set
to `powersave`. If it's greater than `LOAD_THRESHOLD` the CPU governor will be
set to `performance`. `/proc/loadavg` is checked every `CHECK_INTERVAL` seconds.

# How to install/uninstall
```
sudo make install
sudo systemctl enable --now dynamic-governor.service
```


```
sudo systemctl disable --now dynamic-governor.service
sudo make uninstall
```
