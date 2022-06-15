# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(first_name="Test", middle_name="Test", last_name="Test_name", nickname="", title="",
                company="", address="", tel_home="", tel_mobile="",
                tel_work="", tel_fax="", email="", email2="",
                email3="", homepage="", address2="", phone2="",
                notes=""))
    app.contact.modify_contact(
        Contact(first_name="Test_name", middle_name="Test_name", last_name="Test_name", nickname="", title="",
                company="", address="", tel_home="", tel_mobile="",
                tel_work="", tel_fax="", email="", email2="",
                email3="", homepage="", address2="", phone2="",
                notes=""))
