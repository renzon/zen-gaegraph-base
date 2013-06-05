# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph import business_base
from gaegraph import business


def index(_resp, id):
    node_search = business_base.NodeSearch(id)
    business.execute(node_search)
    if node_search.errors:
        _resp.write(node_search.errors)
    elif node_search.node:
        _resp.write(node_search.node.to_dict())
    else:
        _resp.write("Node not found")

