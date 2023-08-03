import subprocess

# subprocess.run('dir', shell=True)  # the 'dir' command is built into shell hence shell=True

# subprocess.run('dir systeminfo', shell=True)  

# subprocess.run(['dir', 'systeminfo'], shell=True)  

"""
p1 = subprocess.run('dir', shell=True, capture_output=True, text=True)

print(p1) # p1 returns a CompletedProcess() instance

print(p1.args) # returns the list of commands executed

print(p1.stdout.decode()) # returns a binary string to convert it into text use text=True in run, or use decode() in stdout. 
                            # to capture the stdout pass capture_output=True in run
print(p1.returncode) # returns the return code 0 == NoErrors

print(p1.stderr) # returns the error in executing commands
                    # pass check=True in run if you want python to throw an error
"""

# to save the stdout in a file
"""
with open("output.txt", 'w') as f:
    p2 = subprocess.run('dir', shell=True, stdout=f, text=True)
    # it is redirecting the output into the file now
"""

# Popen
"""
p3 = subprocess.Popen('ifconfig', shell=True, capture_output=True, text=True)  # it is similar to run but Popen don't wait for process to complete like .run()
std_out, std_err = p3.communicate()  # returns std_out and std_err
"""
