# magPi_downloader
Scripts in Python to download magPi and Hackspace magazines pdfs


# Files

magpi_downloader.py - downloads magazine issues of MagPi magazine
hackspace_downloader.py - downloads magazine issues of Hackspace magazine

# Usage
Install the following Python modules:

    pip3 install requests

    pip3 install beautifulsoup4

Run the script:

    magpi_downloader.py
 
    hackspace_downloader.py

By Default it will download all issues starting from the 1st to 129 of MagPi and issue 1 to 
69 of Hackspace magazines in the current directory.
To change the issue range modify the variables STARTINGISSUE and LASTISSUE.

The variable PROCESSES can also be modified to specify how many to download at a time. Default is 30.

