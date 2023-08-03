import multiprocessing
import time
import concurrent.futures


"""
Multiprocessing should be used on the processes which are CPU bound. not I/O bound processes.
"""

def do_something(t=0):
    print("Sleeping for {time} second(s)")
    time.sleep(t)
    print("Done Sleeping!!!")
    return ("Done Sleeping!!!")

timer_start = time.perf_counter()

# multiprocessing using multiprocessing module
"""
processes = []

for _ in range(10):
    p = multiprocessing.Process(target=do_something)
    p.start()
    processes.append(p)

for process in processes:
    process.join()
"""
# multiprocessing using concurrent.futures module
"""
with concurrent.futures.ProcessPoolExecutor() as executor:
    results = [executor.submit(do_something, 1) for _ in range(10)]  # .submit() passes the arguments to function
    
    for f in concurrent.futures.as_completed(results):  # as_completed() will return the threads in order of their completion.
        print(f.result)  # printing the output of f
"""
# map in concurrent.futures module
"""
with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs) # it starts the processes with passing arguments from the list
    
    for result in results:  # if there is an error in executing func then the error will be thrown on looping on results
        print(result)
"""
# example : cropping the files in parallel to save time as it is CPU bound task
img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]

from PIL import Image, ImageFilter

size = (1200, 1200)
# using normal method
"""
for img_name in img_names:
    img = Image.open("C:\\Users\\pushk\\PycharmProjects\\firstproject\\TempFiles\\"+img_name)

    img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size=size)
    img.save(f"processed/{img_name}")
    print(f"{img_name} was processed")
"""
# using multiprocessing
"""
def process_image(img_name):
    img = Image.open("C:\\Users\\pushk\\PycharmProjects\\firstproject\\TempFiles\\"+img_name)

    img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size=size)
    img.save(f"processed/{img_name}")
    print(f"{img_name} was processed")

def main():  # we have to use main() because of freeze_support error.
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image, img_names)

if __name__=='__main__':
    timer_start = time.perf_counter()
    main()
timer_end = time.perf_counter()
print(f"The process took {round(timer_end - timer_start, 2) } second(s)")
"""