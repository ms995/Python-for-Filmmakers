import os
import requests
from io import BytesIO

os.chdir('/Users/surgesm/Desktop/cams/3_22/alaska') # first, set directory where files to be saved
print(os.getcwd()) # print to make sure it's set correctly 

# allsky alaska webcam, daily index @ http://allsky.gi.alaska.edu/tagged_cam/
# copy, reformat list in google sheets (see "webcam notes" PDF with instructions)

# download from the list 

url_list=[
'http://allsky.gi.alaska.edu/tagged_cam/200322115347.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322115447.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322115547.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322115756.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322115957.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322120257.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322120749.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322121751.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322122752.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322123754.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322124647.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322124755.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322124847.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322124947.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322125047.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322125147.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322125748.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322125957.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322130751.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322131752.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322132744.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322133754.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322134547.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322134747.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322134847.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322134947.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322135047.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322135147.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322135657.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322135757.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322140751.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322141247.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322141347.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322141749.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322142753.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322143547.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322143749.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322144754.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322145457.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322145754.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322150047.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322150749.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322151749.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322152247.jpg',
'http://allsky.gi.alaska.edu/tagged_cam/200322152751.jpg',
]

for i in url_list:
    r = requests.get(i, stream = True)
    file_name = i.split('/')[-1]

    with open(file_name, 'wb') as f: 
            for chunk in r.iter_content(chunk_size = 1024*1024): 
                if chunk: 
                    f.write(chunk) 
                    print("%s downloaded!\n"%file_name)
