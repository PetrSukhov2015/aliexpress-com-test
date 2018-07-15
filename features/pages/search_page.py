import time

from testtools.assertions import assert_that




class SearchPage(object):

    def __init__(self, driver):
        self.driver = driver

    def open(self, link):
        self.driver.get(link)

    def close_pop_up(self):
        self.driver.find_element_by_xpath('/html/body/div[7]/div/div/a').click()

    def wait (self,sec):
        time.sleep(int(sec))
    def fill (self, s_request):
        self.driver.find_element_by_xpath('//*[@id="search-key"]').send_keys(s_request)
    def search(self):
        self.driver.find_element_by_xpath('//*[@id="form-searchbar"]/div[1]/input').click()
    def check_result(self,num):
        res = self.driver.find_element_by_xpath('//*[@id="we-wholesale-search-list"]/div[6]/div/div/div[2]/p/strong').text
        res_num= self.to_int(res)
        assert_that(res_num>num)

    def to_int(self,the_string):
        if ',' in the_string:
            h = the_string.split(',')[0]
            return h*1000 + int(the_string.split(',')[1])
        else:
            return int(the_string)
        return 0

            #assertTrue ( res > 0)
        #self.driver.screen


        # WebDriverWait(context.browser, 120).until(
        #    EC.element_to_be_clickable((By.XPATH, '//button'))
        # )
        # context.browser.

        # assert context.browser.find_element_by_xpath('//*[contains(text(), "%s")]' % text)



