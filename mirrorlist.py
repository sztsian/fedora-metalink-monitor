#!/bin/python2

import mirrorobject

checklist = []
TUNA = MirrorObject()
TUNA.name = "TUNA"
TUNA.urlpattern = "tuna.tsinghua.edu.cn"
TUNA.email = "staff#tuna.tsinghua.edu.cn"
TUNA.repos.extend(fedora["x86_64"])
checklist.append(TUNA)
