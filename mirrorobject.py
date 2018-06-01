#!/bin/python2

import repolist

class MirrorObject(object):
    def __init__(self):
        self.name = ""
        self.urlpattern = ".*?"
        self.email = ""
        self.repos = []
        self.error = []
    def checkall(self):
        # TO DO

