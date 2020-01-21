import threading as trd
thread_status={}
thread_count={}
threads=[]
# Define a function for the thread
def print_time():
   thread=trd.current_thread().name
   count = 0
   status="incomplete"
   thread_status.update({thread:status})
   while count <= 5:
      thread_count.update({thread:count})
      count += 1
      if(count==5):
         status="complete"
         thread_status.update({thread:status})
         trd.current_thread().close()


# Create two threads as follows
try:
   for i in range(5):
      wynik=trd.Thread(target=print_time)
      threads.append(wynik)
      wynik.start()
except:
   raise
print(threads)
print(thread_status)

while 1:
   pass