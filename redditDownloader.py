import requests
import urllib.request
import random
import string
import time

#Function to create random strings of letters to name the video
def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

#adds .json to end of the video urls and appends them to the list
#replace vidfile.txt with text file that has the urls to the reddit pages
with open('vidfile.txt', 'r') as f:
    list = []
    for line in f:
        videolink = line.rstrip() + ".json"
        list.append(videolink)
    print(list)
    length_list = len(list)
    #loops through all the urls and gets the video address
    for i in range(length_list):
        url = list[i]
        print("Now downloading: " + str(url))
        r = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).json()
        video_data = r[0]['data']['children'][0]['data']['media']['reddit_video']['fallback_url']
        print(video_data)

        # Generates random names for the vids and downloads em
        randomchars = random_char(10)
        urllib.request.urlretrieve(video_data, randomchars + ".mp4")
        time.sleep(8)
