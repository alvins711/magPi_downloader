#!/usr/bin/python3

######################################################################
# Desc: download raspi magazine pdfs from a range based on issue number
# Author: Alvin Salalila
# Date: Sep 17 2023
######################################################################

import requests, os, time
from bs4 import BeautifulSoup
from multiprocessing import Pool


# example path to download "https://magpi.raspberrypi.com/issues/21/pdf/download"
# globals variables
BASEURL = 'https://hackspace.raspberrypi.com'
ISSUESPATH = '/issues/'
DOWNLOADPATH = '/pdf/download'
STARTINGISSUE = 1  # start at 
LASTISSUE = 129     # end at
PROCESSES = 30      # how many at a time

########## function creates a list of urls to download
def retrieveAllURLs():

    fileurllist = []
    #### one at a time ###    
    print("Getting the download URLs...")
    for issuenum in range(STARTINGISSUE, LASTISSUE): 
        issuenum = "%02d" % (issuenum,)
        absurl = BASEURL + ISSUESPATH + issuenum + DOWNLOADPATH
        fileurllist.append(getsource(absurl))
        print(f"issue {issuenum} - {fileurllist}")

    return fileurllist


########## function extracts the iframe source from html page
def getsource(sourceurl):

    response = requests.get(sourceurl, stream=True)
    soup=BeautifulSoup(response.content,'html.parser')
    iframes=soup.find_all('iframe')
    for iframe in iframes:
        src=iframe['src']
    src = BASEURL + src
    return src

# using wget to download
def downloader(myfile):
    #print(f'getting {myfile}')
    wget = "wget -q --show-progress --no-use-server-timestamps "
    os.system(wget + myfile)

# using request module to download
def downloader2(myfile):
    r = requests.get(myfile)
    filename = myfile.split("/")[-1]
    print(f'downloading {filename}...', end ="")
    start_time = time.time()
    open(filename, 'wb').write(r.content)
    print(f'done {format(time.time() - start_time)}')


def main():

### single thread wgets

#   for i in retrieveAll():
#        downloader(i)

### parallel wgets based on PROCESSES global var
    filelist = retrieveAllURLs()
    with Pool(PROCESSES) as p:
        # p.map(downloader,filelist) 
        p.map(downloader2,filelist) 


if __name__ == "__main__":
    #start_time = time.time()
    main()
    #print(f'time to finish {format(time.time() - start_time)}')
