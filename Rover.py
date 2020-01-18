import os
import requests
from io import BytesIO

os.chdir('/Users/surgesm/Desktop/test') # first, set directory where files to be saved
print(os.getcwd()) # print to make sure it's set correctly 

# download from the list

url_list=[
    'https://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01927/soas/rdr/ccam/CR0_568556545PRC_F0671846CCAM01927L2.PNG',
    'https://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01927/soas/rdr/ccam/CR0_568557163PRC_F0671846CCAM01927L2.PNG',
    'https://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01927/soas/rdr/ccam/CR0_568557795PRC_F0671846CCAM01927L1.PNG',
    'https://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01927/soas/rdr/ccam/CR0_568557914PRC_F0671846CCAM02927L1.PNG',
    'https://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01927/soas/rdr/ccam/CR0_568558291PRC_F0671846CCAM02927L1.PNG',
    'https://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01927/soas/rdr/ccam/CR0_568559188PRC_F0671846CCAM02927L1.PNG',
    'https://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01928/soas/rdr/ccam/CR0_568651190PRC_F0671846CCAM03927L1.PNG',
    'https://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01928/soas/rdr/ccam/CR0_568651423PRC_F0671846CCAM04927L1.PNG',
    'https://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01928/soas/rdr/ccam/CR0_568651938PRC_F0671846CCAM04927L1.PNG',
    'https://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01928/soas/rdr/ccam/CR0_568652763PRC_F0671846CCAM04927L1.PNG',
    'https://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01928/soas/rdr/ccam/CR0_568652895PRC_F0671846CCAM05927L1.PNG',
    'https://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01928/soas/rdr/ccam/CR0_568653791PRC_F0671846CCAM05927L1.PNG'
]

for i in url_list:
    r = requests.get(i, stream = True)
    file_name = i.split('/')[-1]

    with open(file_name, 'wb') as f: 
            for chunk in r.iter_content(chunk_size = 1024*1024): 
                if chunk: 
                    f.write(chunk) 
                    print("%s downloaded!\n"%file_name)
