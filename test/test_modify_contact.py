# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify(
        Contact(first_name="Test_name", middle_name="Test_name", last_name="Test_name", nickname="", title="",
                company="", address="", tel_home="", tel_mobile="",
                tel_work="", tel_fax="", email="", email2="",
                email3="", homepage="", address2="", phone2="",
                notes=""))
    app.session.logout()
