# -*- coding: utf-8 -*-
from contact import Contact
from application import Application
import pytest

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_new_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact(Contact(first_name="Fname", middle_name="Mname", last_name="Lname", nickname="Nickname", title="Test_title", company="Test_company", address="Test_address", tel_home="123456", tel_mobile="11223344", tel_work="11224433", tel_fax="11225566", email="test@mail.com", email2="test2@mail.com", email3="test3@mail.com", homepage="www.test.com", address2="second_address", phone2="123465798", notes="test_notes"))
    app.logout()

