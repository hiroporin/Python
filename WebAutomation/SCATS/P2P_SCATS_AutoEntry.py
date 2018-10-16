# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 13:49:11 2018

@author: HOTA
"""

# Initial mylib
import os
import sys; sys.path.append(os.getcwd()[:3] + r'Appli\Python\mylib')
import web_control
import xlrd
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime as dt

# Initial Cchromedriver
driver = web_control.set_driver()

# Open P2P site
driver.get('https://apex.oraclecorp.com/pls/apex/f?p=27260:1:1736970256711:::::')

# Input ID/PW and Login
mail = driver.find_element_by_id('sso_username')
pass_wd = driver.find_element_by_id('ssopassword')# emailを入力
mail.send_keys('hiroshi.ota@oracle.com')
pass_wd.send_keys('Qt4myoFE')
pass_wd.submit()

# Open Cloud Engagement List
driver.get('https://apex.oraclecorp.com/pls/apex/f?p=P360_ACTIVITIES:::::::')

#Load excel file
wb = xlrd.open_workbook('./SC_Activity.xlsx')
sheet = wb.sheet_by_name('Activity')

#Add P2P entry
row = 2
while(sheet.cell_value(row,1).upper() != 'END'):
    #Create Activity
    driver.find_element_by_class_name('ui-widget-content').click()
    
    #Find element
    activity= driver.find_element_by_id('P29_ACTIVITY_ID')
    act_date = web_control.DateChange(dt.strptime('2018/08/28','%Y/%m/%d').strftime('%Y/%m/%d'))
    
    poc_name = driver.find_element_by_id('P7_POC_NAME')
    poc_stage = driver.find_element_by_id('P7_POC_STAGE')
    poc_steps = driver.find_element_by_id('P7_NEXT_STEPS')
    
    #Set Value
    activity_element = Select(activity)
    if a=='':        
        activity_element.select_by_value('129188634126706740470948518512533725501')


    partner.send_keys(sheet.cell_value(row, 2))
    poc_stage_element = Select(poc_stage)
    poc_stage_element.select_by_value('1. Qualifying')
    if sheet.cell_value(row, 30) == '':
        poc_steps.send_keys('TBD')
    else:
        poc_steps.send_keys(sheet.cell_value(row, 30))
        
    poc_name.send_keys(sheet.cell_value(row, 4))
    
    #Save
    driver.find_element_by_id('B20620684921121152539').click()
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, 'ui-widget-content')))
    
    row+=1

# Close and quit
driver.close()
driver.quit()

