# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from core.user.model import User
from gaebusiness.business import UseCase


class ListUsers(UseCase):
    def set_up(self):
        self._future=User.query().order(User.creation).fetch_async()

    def do_business(self):
        self.result=self._future.get_result()

class SaveUser(UseCase):
    def __init__(self,name):
        super(SaveUser,self).__init__()
        self.name=name

    def set_up(self):
        self._future=User.query(User.name==self.name).count_async()
        self.result=None

    def do_business(self):
        if self._future.get_result()>0:
            self.errors["name"]= "REPEATED_NAME"
        else:
            self.result=User(name=self.name)

    def commit(self):
        return self.result
