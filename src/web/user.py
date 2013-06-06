# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from core.user import business as user_business
from gaegraph import business
from zen import router


def list(_write_tmpl):
    list_users=user_business.ListUsers()
    business.execute(list_users)
    _write_tmpl("templates/result.html",{"result":list_users.result})

def save(_handler,_resp,name):
    save_user=user_business.SaveUser(name)
    business.execute(save_user)
    if save_user.errors:
        _resp.write(save_user.errors)
    else:
        _handler.redirect(router.to_path(list))


