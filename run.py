#!/usr/bin/python

import os

try:
    IP = '127.0.0.1'
    with open('sites.txt', 'r') as fin:
        sites = map(lambda x: x.strip(), list(fin))

    with open('/etc/hosts', 'a+') as fin:
        fin.write('\n')
        for site in sites:
            fin.write('{} {}\n'.format(IP, site))
            fin.write('{} www.{}\n'.format(IP, site))

    os.system('sudo service network-manager restart')
    print 'OK'
except IOError:
    print 'Run script as root'
except Exception as e:
    print str(e)
