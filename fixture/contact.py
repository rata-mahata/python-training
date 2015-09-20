__author__ = 'Olga'
from model.contact import Contact
class ContactHelper :


    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")) :
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        # initiate creating new contact
        wd.find_element_by_link_text("add new").click()
        # filling form
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        self.contact_cache=None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_field("firstname", contact.name)
        self.change_contact_field("lastname", contact.surname)
        self.change_contact_field("title", contact.title)
        self.change_contact_field("mobile", contact.phone)
        self.change_contact_field("email", contact.email)

    def change_contact_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_last_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_home_page()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_home_page()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        wd.get("http://localhost/addressbook/")
        self.contact_cache=None

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        wd.get("http://localhost/addressbook/")
        self.contact_cache=None


    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache=None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                surname = cells[1].text
                name = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                self.contact_cache.append(Contact(surname=surname, name=name,id=id))
        return list(self.contact_cache)






