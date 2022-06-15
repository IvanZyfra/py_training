# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_name"))
    app.group.modify_first_group(Group(name="test_test"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_name"))
    app.group.modify_first_group(Group(header="test_header"))
