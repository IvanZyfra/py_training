


def test_phones_on_home_page(app):
   contact_from_home_page = app.contact.get_contacts_list()[0]
   contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
   assert contact_from_home_page.tel_home == contact_from_edit_page.tel_home
   assert contact_from_home_page.tel_mobile == contact_from_edit_page.tel_mobile
   assert contact_from_home_page.tel_work == contact_from_edit_page.tel_work
   assert contact_from_home_page.tel_fax == contact_from_edit_page.tel_fax