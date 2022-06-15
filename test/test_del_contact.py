from model.contact import Contact



def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(first_name="Test", middle_name="Test", last_name="Test_name", nickname="", title="",
                company="", address="", tel_home="", tel_mobile="",
                tel_work="", tel_fax="", email="", email2="",
                email3="", homepage="", address2="", phone2="",
                notes=""))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
