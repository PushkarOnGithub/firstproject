import threading
import time
import concurrent.futures

"""
Threading should be used on the processes which are not CPU bound. On I/O bound processes.
"""

def do_something(t=0):
    print("Sleeping for {time} second(s)")
    time.sleep(t)
    print("Done Sleeping!!!")

timer_start = time.perf_counter()

# threading using threading module
"""
threads = []  # list to store the threads

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()  # start will start the thread 
    threads.append(t)

for thread in threads:
    thread.join()  # the program after join will not be executed until thread finishes
"""

# threading using concurrent.futures module
"""
with concurrent.futures.ProcessPoolExecutor() as executor:
    results = [executor.submit(do_something, 1) for _ in range(10)]  # .submit() passes the arguments to function
    
    for f in concurrent.futures.as_completed(results):  # as_completed() will return the threads in order of their completion.
        print(f.result)  # printing the output of f
"""
# map in concurrent.futures module
"""
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)
    
    for result in results:  # if there is an error in executing func then the error will be thrown on looping on results
        print(result)
"""
# example : downloading the files in parallel to save time as it is I/O bound task
img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

import requests
import os
import subprocess

# Normal Approach
"""
if not os.path.exists("TempFiles"):
    subprocess.Popen("mkdir TempFiles", shell=True)
for img_url in img_urls:
    img_bytes = requests.get(url=img_url).content
    img_name = img_url.split("/")[3]
    img_name = f"{img_name}.jpg"
    img_path = r"C:\\Users\\pushk\\PycharmProjects\\firstproject\\TempFiles"
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        subprocess.run(f"copy {img_name} {img_path}", shell=True)
        subprocess.Popen(f"del {img_name}", shell=True)
        print(f'{img_name} was downloaded')
"""

# using threading
"""
if not os.path.exists("TempFiles"):
    subprocess.Popen("mkdir TempFiles", shell=True)
def download_img(img_url):
    img_bytes = requests.get(url=img_url).content
    img_name = img_url.split("/")[3]
    img_name = f"{img_name}.jpg"
    img_path = r"C:\\Users\\pushk\\PycharmProjects\\firstproject\\TempFiles"
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        subprocess.run(f"copy {img_name} {img_path}", shell=True)
        subprocess.Popen(f"del {img_name}", shell=True)
        print(f'{img_name} was downloaded')

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_img, img_urls)
"""


timer_end = time.perf_counter()
print(f"The process took {round(timer_end - timer_start, 2) } second(s)")