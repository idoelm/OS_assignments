import multiprocessing
import requests
import json

def getJsonFromLink(link, queue_counter, counter):
    len_of_json = len(json.dumps(requests.get(link).json()))
    print("Process " + str(counter) + " downloaded " + str(len_of_json) + " chars from: " + str(link) )
    queue_counter.put(len_of_json)

def main():
    queue = multiprocessing.Queue()
    queues = []
    sum = 0
    proc = []
    links = ['https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
        ]
    for counter, link in enumerate(links, start = 0):
        process = multiprocessing.Process(target = getJsonFromLink, args = (link, queue,counter, ))
        process.start()
        proc.append(process)
        queues.append(queue)
    
    for i in proc:
        i.join()

    for i in queues:
        sum += queue.get()

    print("Total number of chars downloaded is " + str(sum))

if __name__ == "__main__":
    main()