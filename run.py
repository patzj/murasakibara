#!/usr/bin/python

import os
import socket

try:
    IP = '127.0.0.1'
    SCRIPT_COMMENT = '### murasakibara ###\n'

    with open('sites.txt', 'r') as fin:
        sites = map(lambda x: x.strip(), list(fin))

    with open('/etc/hosts', 'r') as fin:
        content = list(fin)

        if SCRIPT_COMMENT in content:
            i = content.index(SCRIPT_COMMENT)
            content = content[:i]

    with open('/etc/hosts', 'w') as fin:
        for line in content:
            fin.write(line)
        fin.write(SCRIPT_COMMENT)
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
