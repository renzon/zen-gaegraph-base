# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from core.user.business import SaveUser


def save_user_usecase(name):
    return [SaveUser(name)]
