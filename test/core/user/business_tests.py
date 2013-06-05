# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from core.user.business import ListUsers, SaveUser
from core.user.model import User
from gaegraph import business
from util.gae import GAETestCase


class UseCaseTest(GAETestCase):
    def test_list(self):
        list_users = ListUsers()
        business.execute(list_users)
        self.assertListEqual([], list_users.users)
        renzo = User(name="Renzo")
        renzo.put()
        foo = User(name="foo")
        foo.put()
        business.execute(list_users)
        self.assertListEqual([renzo, foo], list_users.users)

    def test_save(self):
        save_user = SaveUser("Renzo")
        business.execute(save_user)
        self.assertEqual("Renzo", save_user.user.name)

        # Repeated names no allowed
        errors=business.execute(save_user)
        self.assertDictEqual({"name": "REPEATED_NAME"}, save_user.errors)
        self.assertDictEqual({"name": "REPEATED_NAME"}, errors)
        self.assertIsNone(save_user.user)



