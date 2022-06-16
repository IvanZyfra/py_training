# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(first_name="Test", middle_name="Test", last_name="Test_name", nickname="", title="",
                company="", address="", tel_home="", tel_mobile="",
                tel_work="", tel_fax="", email="", email2="",
                email3="", homepage="", address2="", phone2="",
                notes=""))
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(first_name="Fname", middle_name="Mname", last_name="Lname", nickname="Nickname", title="Test_title", company="Test_company", address="Test_address", tel_home="123456", tel_mobile="11223344", tel_work="11224433", tel_fax="11225566", email="test@mail.com", email2="test2@mail.com", email3="test3@mail.com", homepage="www.test.com", address2="second_address", phone2="123465798", notes="test_notes")
    contact.id = old_contacts[0].id
    app.contact.modify_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
