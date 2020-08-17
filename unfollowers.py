# @author: Deniz Sert
# @newest-version: August 2020
# @change-log: Added function docs

from selenium import webdriver
from time import sleep
from credentials import username, password

class InstaUnfollowers:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome('/Users/dsert/Desktop/Instafollow/chromedriver')
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        # self.driver.find_element_by_xpath("//a[contains(text(), 'Log In')").click() # clicks Log In button
        sleep(2)

        # handles username
        username_type = self.driver.find_element_by_xpath("//input[@name=\"username\"]")
        username_type.send_keys(username)

        # handles password
        password_type = self.driver.find_element_by_xpath("//input[@name=\"password\"]")
        password_type.send_keys(password)

        # submit
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(6)

        # handle setup 2 factor authentication prompt
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)

        # Notification buster
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)


    def get_unfollowers(self):
        '''Prints the list of users who have unfollowed you at some point'''
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username)).click()
        sleep(3)
        self.driver.find_element_by_xpath("//a[contains(@href, '/following')]").click() # open following list
        following = self.get_names()

        self.driver.find_element_by_xpath("//a[contains(@href, '/followers')]").click() # open followers list
        followers = self.get_names()

        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)




    def get_names(self):
        '''Parses through list of followers OR following, depending on what is accessed by the XPATH
        beforehand. Returns this list. '''
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")

        prev_height, height = 0, 1
        while prev_height != height: # reached the bottom of the followers list
            prev_height = height
            sleep(3)


            height = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)

        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click() # click out
        return names
if __name__ == '__main__':
    bot = InstaUnfollowers(username, password)

    bot.get_unfollowers()
    bot.driver.close()
