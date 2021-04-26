
from threading import Thread,Condition
import time
import random
queue=[]
max_num=5
condition=Condition()
class producerThread(Thread):
	def run(self):
		nums=range(5)
		global queue
		while True:
			condition.acquire()
			if len(queue)==max_num:
				print("queue is full producer is waiting")
				condition.wait()
				print("space in queue consumer notified to the producer")
				break
			num=random.choice(nums)
			queue.append(num)
			print("produced:",num)
			condition.notify()
			condition.release()
			time.sleep(random.random())
class consumerThread(Thread):
	def run(self):
		global queue
		while True:
			condition.acquire()
			if not queue:
				print("nothing is there in queue,consumer waiting")
				condition.wait()
				print("producer added something to the queue and notified the consumer")
			num=queue.pop()
			print("consumed",num)
			condition.notify()
			condition.release()
			time.sleep(random.random())
producerThread().start()
consumerThread().start()
