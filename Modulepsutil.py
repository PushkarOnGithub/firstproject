import psutil
import time

# psutil.net_io_counters(pernic=False, nowrap=True) #
# psutil.net_connections() # returns system wide socket connections as a list
# psutil.net_connections(kind='inet')
# psutil.net_if_addrs() # Return the addresses associated to each NIC (network interface card)



# sensors_battery() # returns a tuple of current charge percent,time left,is_plugged
# sensors_fans() # returns fan info and rpm
# sensors_temperatures(fahrenheit=False) # returns temperature readings of hardwares connected

# boot_time() # returns boot time in epoch seconds
# users() # Return users currently connected on the system

# psutil.pids() # Return a sorted list of current running PIDs
# psutil.process_iter(attrs=None, ad_value=None) # Return an iterator yielding a Process class instance for all running processes on the local machine.
"""import psutil
>>> for proc in psutil.process_iter(['pid', 'name', 'username']):
...     print(proc.info)
...
{'name': 'systemd', 'pid': 1, 'username': 'root'}
{'name': 'kthreadd', 'pid': 2, 'username': 'root'}
{'name': 'ksoftirqd/0', 'pid': 3, 'username': 'root'}"""

# psutil.pid_exists(pid) # obvious

# for _ in range(10):
#     print(psutil.net_connections(kind='inet'))
#     time.sleep(1)
print(psutil.net_if_addrs())