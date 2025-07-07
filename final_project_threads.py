import threading
import requests
import json

sum = 0

def getJsonFromLink(link, counter, mutex):
    global sum
    len_of_json = len(json.dumps(requests.get(link).json()))
    print("Thread " + str(counter) + " downloaded " + str(len_of_json) + " chars from: " + str(link) )
    with mutex:
        sum += len_of_json

def main():
    mutex = threading.Lock()
    global sum
    links = ['https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
    ]
    threads = []

    for counter, link in enumerate(links, start = 0):
        thread = threading.Thread(target = getJsonFromLink, args = (link, counter, mutex, ))
        threads.append(thread)
        thread.start()
          
    for i in threads:
        i.join()

    print("Total number of chars downloaded is " + str(sum))

if __name__ == "__main__":
    main()