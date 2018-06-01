#!/bin/python2

urlprefix = [ "https://mirrors.fedoraproject.org/" ]
repos = [ 'fedora-27', 'updates-released-f27', 'fedora-28', 'updates-released-f28' ]
archs = [ 'x86_64' ]

fedora = {}
fedora['name'] = "Fedora"
fedora['x86_64'] = ['https://mirrors.fedoraproject.org/metalink?repo=%s&arch=x86_64&country=cn' % s for s in repos ]


