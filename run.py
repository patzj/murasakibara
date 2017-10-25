#!/usr/bin/python

import os

try:
    IP = '127.0.0.1'
    with open('sites.txt', 'r') as fin:
        sites = map(lambda x: x.strip(), list(fin))

    with open('/etc/hosts', 'a+') as fin:
        content = list(fin)
        fin.write('\n')
        for site in sites:
            entries = ['{} {}\n'.format(IP, site),
            '{} www.{}\n'.format(IP, site),
            '{} m.{}\n'.format(IP, site)]
            for entry in entries:
                if content.count(entry) < 1:
                    fin.write(entry)

    os.system('sudo service network-manager restart')
    print 'OK'
except IOError:
    print 'Run script as root'
except Exception as e:
    print str(e)
