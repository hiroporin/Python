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

# Initial Chromedriver
driver = web_control.set_driver()

# Open P2P site
driver.get('https://apex.oraclecorp.com/pls/apex/f?p=27260:1:1736970256711:::::')

# Input ID/PW and Login
WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.ID, 'sso_username')))
mail = driver.find_element_by_id('sso_username')
pass_wd = driver.find_element_by_id('ssopassword')# emailを入力
mail.send_keys('')
pass_wd.send_keys('')
pass_wd.submit()

# Open Cloud Engagement List
driver.get('https://apex.oraclecorp.com/pls/apex/f?p=24332:6:28029606852229::NO:RP,6,RIR::')
driver.find_element_by_partial_link_text('List').click()

#Load excel file
wb = xlrd.open_workbook('./FY19_Migration_List.xlsx')
sheet = wb.sheet_by_name('migration')

#Add P2P entry
row = 2
while(sheet.cell_value(row,1).upper() == 'JP'):
    if sheet.cell_value(row, 37) == 1.0:
        #Create P2P entry
        driver.find_element_by_id('B6924814101738542543').click()
        WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.ID, 'oj-inputsearch-input-P7_PARTNER_NAME_HIDDEN')))
        
        partner = driver.find_element_by_id('oj-inputsearch-input-P7_PARTNER_NAME_HIDDEN')
        poc_name = driver.find_element_by_id('P7_POC_NAME')
        poc_stage = driver.find_element_by_id('P7_POC_STAGE')
        poc_steps = driver.find_element_by_id('P7_NEXT_STEPS')
        
        partner.send_keys(sheet.cell_value(row, 2))
        poc_stage_element = Select(poc_stage)
        poc_stage_element.select_by_value('1. Qualifying')
        if sheet.cell_value(row, 30) == '':
            poc_steps.send_keys('TBD')
        else:
            poc_steps.send_keys(sheet.cell_value(row, 30))
            
        poc_name.send_keys(sheet.cell_value(row, 4))
        
        driver.find_element_by_id('B20620684921121152539').click()
        WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.ID, 'B6924814101738542543')))
    
    row+=1

# Close and quit
driver.close()
driver.quit()

