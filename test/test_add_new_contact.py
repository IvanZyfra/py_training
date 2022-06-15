# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_add_new_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(first_name="Fname", middle_name="Mname", last_name="Lname", nickname="Nickname", title="Test_title", company="Test_company", address="Test_address", tel_home="123456", tel_mobile="11223344", tel_work="11224433", tel_fax="11225566", email="test@mail.com", email2="test2@mail.com", email3="test3@mail.com", homepage="www.test.com", address2="second_address", phone2="123465798", notes="test_notes")
    app.contact.add_new_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_new_empty_contact(app):
#     app.contact.add_new_contact(Contact(first_name="", middle_name="", last_name="", nickname="", title="", company="", address="", tel_home="", tel_mobile="", tel_work="", tel_fax="", email="", email2="", email3="", homepage="", address2="", phone2="", notes=""))
