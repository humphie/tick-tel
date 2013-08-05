from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class PollsTest(LiveServerTestCase):
    fixtures = ['admin_user.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()
    
    def test_the_admin(self):

        self.browser.get(self.live_server_url + '/admin/')

        #'Django administration' heading
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        #  username and passwords and hits return
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('tick')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('tick')
        password_field.send_keys(Keys.RETURN)

        # the Site Administration page
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)
        
        #get the Sms link
        sms_link = self.browser.find_element_by_link_text('Smss').click()
        
        #get Add sms
        add_sms_link = self.browser.find_element_by_link_text('Add sms').click()
        
        
        #add a userz credentails
        #enter thr username
        username = self.browser.find_element_by_name('name')
        username.send_keys('tick')
        
        #enter the contact
        contact = self.browser.find_element_by_name('contact')
        contact.send_keys('256703000289')
        
        #enter the country
        country = self.browser.find_element_by_name('country')
        country.send_keys('uganda')
        
        #enter the remaining msgz
        remaining_messages = self.browser.find_element_by_name('sms_count')
        remaining_messages.send_keys('5000')
        
        #check if the response code is 200
        click_save_button = self.browser.find_element_by_css_selector("input[value='Save']").click()
        
        #examine the out put
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('The sms "tick" was added successfully', body.text)
        
        #click the home link
        home_link = self.browser.find_element_by_link_text('Home').click()
        
        #check for 'Site Administration' in the body
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)
        
        #click the phone link
        phonebook_link = self.browser.find_element_by_link_text('Phones').click()
        self.browser.implicitly_wait(5)
        
        #click the add phone link
        add_phone_link = self.browser.find_element_by_link_text('Add phone').click()
        
        #fill in the form
        username = self.browser.find_element_by_name('username')
        username.send_keys('tick')
        
        #input name
        name = self.browser.find_element_by_name('name')
        name.send_keys('hum')
        
        #input the group
        group = self.browser.find_element_by_name('group')
        group.send_keys('family')
        
        #enter the number
        number = self.browser.find_element_by_name('contact')
        number.send_keys('25670330289')
        
        #click the save button
        click_save_button = self.browser.find_element_by_css_selector("input[value='Save']").click() 
        
        #get the response
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('The phone "tick" was added successfully', body.text)
        
        #add acalendar to the mix
        #click the home link
        home_link = self.browser.find_element_by_link_text('Home').click()
        
        #check for 'Site Administration' in the body
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)
        
        #click the calendar link
        event_link = self.browser.find_element_by_link_text('Events').click()
        
        #click the Add event link
        add_event_link = self.browser.find_element_by_link_text('Add event').click()
        
        #insert fields
        #event owner
        event_owner = self.browser.find_element_by_name('owner')
        event_owner.send_keys('tick')
        
        #event title
        event_owner = self.browser.find_element_by_name('event_title')
        event_owner.send_keys('board meeting')
        
        #event date
        event_date = self.browser.find_element_by_name('date')
        event_date.send_keys('2013-06-28')
        
        #event description
        event_description = self.browser.find_element_by_name('description')
        event_description.send_keys('Reminder of the Tick board meeting @ 3pm in the main conference room')
        
        
        #event riority
        event_priority = self.browser.find_element_by_name('priority')
        event_priority.send_keys('high')
        
        #event type
        event_type = self.browser.find_element_by_name('event_type')
        event_type.send_keys('private')        
        
        #click the save button
        click_save_button = self.browser.find_element_by_css_selector("input[value='Save']").click() 
        
        #get the response
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('The event "Event object" was added successfully', body.text)        
        
        #click the logout link
        logout_click = self.browser.find_element_by_link_text('Log out').click()
        
        #analyze the response page and close the browser
        logged_out_page = self.browser.find_element_by_tag_name('body')
        self.assertIn('Logged out', logged_out_page.text)
        
    

    
    def test_the_home_page(self):

        #get the home page
        self.browser.get(self.live_server_url + '/')
        
        #check the home page for '2013 Tick Int'
        home_page = self.browser.find_element_by_tag_name('body')
        self.assertIn('2013 Tick Int', home_page.text)
        
        #get to the login form
        login_page_link = self.browser.find_element_by_link_text('Tick More').click()
        self.browser.implicitly_wait(5)
        
        login_page_link = self.browser.find_element_by_link_text('Sign In').click()
        
        #enter the username
        username = self.browser.find_element_by_name('username')
        username.send_keys('tick')
        
        #enter the password
        password = self.browser.find_element_by_name('password')
        password.send_keys('sasaki')
        
        #click the login button
        click_login = self.browser.find_element_by_css_selector('Sign In').click()
        
        #check the logged in page for the username
        logged_in_page = self.browser.find_element_by_tag_name('body')
        self.assertIn('Sign out', logged_in_page.text)
       
        
        
        
        
       
        
        
