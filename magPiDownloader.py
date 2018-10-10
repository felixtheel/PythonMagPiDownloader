# License

import urllib.request

version = 0.1
downloadURL = 'https://www.raspberrypi.org/magpi-issues/MagPi'
downloadIssue = ''

print('MagPi Downloader v' + str(version))
print('------------')

print('What is the first issue you want to download?')
firstIssue = input()
firstIssue = int(firstIssue)

print('And what is the last issue?')
lastIssue = input()
lastIssue = int(lastIssue) + 1

for i in range(firstIssue, lastIssue):
    if i <= 9:
        downloadIssue = downloadURL + '0' + str(i) + '.pdf'
    else:
        downloadIssue = downloadURL + str(i) + '.pdf'
        
    print('Downloading issue ' + str(i) + '.. (' + downloadIssue + ')')
    
    if i <= 9:
        urllib.request.urlretrieve (downloadIssue, '/magPi/MagPi0' + str(i) + '.pdf')
    else:
        urllib.request.urlretrieve (downloadIssue, '/magPi/MagPi' + str(i) + '.pdf')       
