from datetime import datetime
from datetime import time
from time import sleep

import schedule
import os
import requests

os.chdir('/path/to/folder') # first, set directory where files to be saved
print(os.getcwd()) # print to make sure it's set correctly 

# using schedule library in combination with requests
# download image every 30 minutes from this url

def job():
    url = 'http://ivs.bkg.bund.de/vlbi/ohiggins/ohig-web2.jpg'
    r = requests.get(url, allow_redirects=True)
    open('ohig-web2.jpg', 'wb').write(r.content)

    # renaming files to add time of download
    # because we need unique file names to save multiples
    created_time = os.stat('ohig-web2.jpg').st_ctime   
    print(datetime.fromtimestamp(created_time))
    os.rename('ohig-web2.jpg', 'penguins2x' + str(datetime.fromtimestamp(created_time)) + '.jpg')

schedule.every(30).minutes.do(job)

# also possible to schedule per hour or minute...
# schedule.every().hour.do(job)
# schedule.every().minutes.do(job)

while True:
    schedule.run_pending()
    sleep(1)

# other Antarctic penguin cams to try (update every 15-30 min.)
# http://ivs.bkg.bund.de/vlbi/ohiggins/ohig-web1.jpg
# http://ivs.bkg.bund.de/vlbi/ohiggins/ohig-web3.jpg
# http://antarctica.martingrund.de/ohig-pingi-z.jpg
