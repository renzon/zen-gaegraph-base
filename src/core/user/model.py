# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node


class User(Node):
    name=ndb.StringProperty(required=True)

    def __eq__(self, other):
        if other and other.key and self:
            return self.key==other.key
        return False

