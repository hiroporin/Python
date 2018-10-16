# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 09:37:31 2018

@author: Oracle HOTA
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 13:49:11 2018

@author: HOTA
"""

# Initial mylib
import os
import sys; sys.path.append(os.getcwd()[:3] + r'Appli\Python\mylib')
import web_control
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Initial Chromedriver
driver = web_control.set_driver()

# Open Logfile
path = './log.txt'
f = open(path, mode='a')

# Open Cloud Account Select
try:
    driver.get('https://cloud.oracle.com/ja_JP/sign-in')
    account_name = driver.find_element_by_id('cloudAccountName')
    account_name.send_keys('necgprime')
    driver.find_element_by_class_name('signin-button').click()
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, 'idcs-signin-basic-signin-form-username')))
    f.write(datetime.now().strftime("%Y/%m/%d %H:%M:%S") + "Succeed: Oracle Cloud Account Page\n")
except:
    f.write(datetime.now().strftime("%Y/%m/%d %H:%M:%S") + "Failed : Oracle Cloud Account Page : Can't open Oracle Cloud Account Page\n")
    sys.exit()
    

# Open Cloud Login
try:
    mail = driver.find_element_by_id('idcs-signin-basic-signin-form-username')
    pass_wd = driver.find_element_by_id('idcs-signin-basic-signin-form-password')
    mail.send_keys('hiroshi.ota@oracle.com')
    pass_wd.send_keys('9IcdamsZF___')
    driver.find_element_by_id('idcs-signin-basic-signin-form-submit').click()
    f.write(datetime.now().strftime("%Y/%m/%d %H:%M:%S") + "Succeed: Oracle Cloud Login Page\n")
except:
    f.write(datetime.now().strftime("%Y/%m/%d %H:%M:%S") + "Failed : Oracle Cloud Login Page : Can't login\n")
    sys.exit()

# Close and quit
f.close()
#driver.close()
#driver.quit()
