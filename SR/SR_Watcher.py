# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 09:37:31 2018

@author: HOTA
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 13:49:11 2018

@author: HOTA
"""

# Initial mylib
import os
#import sys; sys.path.append(os.getcwd()[:3] + r'Appli\Python\mylib')
import sys; sys.path.append('Python/mylib')
import web_control
import xlrd

# Initial Cchromedriver
driver = web_control.set_driver()

# Initial Parameter
row = 2
winno = 0

#Load excel file
wb = xlrd.open_workbook('./SR_List.xlsx')
sheet = wb.sheet_by_name('NEC AI Platform')

# Login SR site
driver.get('https://mosemp.us.oracle.com/mosspui/src/sr/viewer/index.html#/' + sheet.cell_value(row,1))

# Input ID/PW and Login
mail = driver.find_element_by_id('sso_username')
pass_wd = driver.find_element_by_id('ssopassword')# emailを入力
mail.send_keys('hiroshi.ota@oracle.com')
pass_wd.send_keys('Qt4myoFE')
pass_wd.submit()

# Open SRs
while(sheet.cell_value(row,1).upper() != 'END'):
    if winno==0:
        driver.get('https://mosemp.us.oracle.com/mosspui/src/sr/viewer/index.html#/' + sheet.cell_value(row,1))
    else:
        driver.execute_script("window.open()")
        driver.switch_to.window(driver.window_handles[winno])
        driver.get('https://mosemp.us.oracle.com/mosspui/src/sr/viewer/index.html#/' + sheet.cell_value(row,1))

    winno+=1
    row+=1
           
# Close and quit
"""
driver.close()
driver.quit()
"""

