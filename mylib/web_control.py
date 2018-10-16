# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 13:15:51 2018

@author: h-ota
"""

import os
from selenium import webdriver

def set_driver():

    # chromedriver file check
    path  = os.getcwd()[:3] + r'Software\Tools\selenium\chromedriver\chromedriver.exe'
    #path  = os.getcwd()[:3] + r'Software\Tools\selenium\MicrosoftWebDriver\MicrosoftWebDriver.exe'
    
    # Initial Cchromedriver
    driver = webdriver.Chrome(path)
    #driver = webdriver.Edge(path)

    return driver

def DateChange(p_date):
    
    if p_date[5:7] == '01':
        engMonth = 'Jan'
    elif p_date[5:7] == '02':
        engMonth = 'Feb'
    elif p_date[5:7] == '03':
        engMonth = 'Mar'
    elif p_date[5:7] == '04':
        engMonth = 'Apr'
    elif p_date[5:7] == '05':
        engMonth = 'May'
    elif p_date[5:7] == '06':
        engMonth = 'Jun'
    elif p_date[5:7] == '07':
        engMonth = 'Jul'
    elif p_date[5:7] == '08':
        engMonth = 'Aug'
    elif p_date[5:7] == '09':
        engMonth = 'Sep'
    elif p_date[5:7] == '10':
        engMonth = 'Oct'
    elif p_date[5:7] == '11':
        engMonth = 'Nov'
    elif p_date[5:7] == '12':
        engMonth = 'Dec'
        
    r_date = p_date[8:10] + '-' + engMonth + '-' + p_date[0:4]                 
    
    return r_date
    
    
    
