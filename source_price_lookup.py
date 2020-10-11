# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 22:47:22 2020

@author: singh
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

preferred_vendor=""
from_price=""
to_price=""
#Initializing the Selenium WebDriver
def initialize_driver(browser="chrome"):
    driver = webdriver.Chrome()
    return driver

#Displaying Welcome Message
def welcome_message():
    print("===================== Welcome to Bell ========================")
    print("Please answer the following search questions to filter results!")

#Displaying search questions and waiting for user inputs
def prompt_filter_questions():
    global preferred_vendor
    global from_price
    global to_price
    #The search criteria will be based on the preferred vendor and desired 24 month monthly price range at $0 down.
    preferred_vendor=input("Please provide your: Prefered Vendor?")
    from_price=float(input("Please provide the lower limit for 24 month monthly price ($0 down): "))
    to_price=float(input("Please provide the upper limit for 24 month monthly price ($0 down): "))

#Displaying the BELL Homepage.
def get_page(driver,page):
    driver.get(page)

#Filtering the phone models available for the preferred vendor
def vendor_models(driver):
    vendor_main_web = driver.find_element_by_id("filter_nav_"+preferred_vendor)
    # Sending a signal that Return key has been pressed.To Navigate to page of the desired vendor
    vendor_main_web.send_keys(Keys.RETURN)
    el1=driver.find_element_by_id("dl-list-"+preferred_vendor)
    
    #Retrieve the list of phone models available for the preferred vendor
    phone_models_list=el1.find_elements_by_class_name('dl-tile-content')
    return phone_models_list

#Filtering the phone models extracted from the preferred vendor to only the ones that lie
    #within the range of preferred 24 month monthly price range at $0 down.
def price_range_models(driver,phone_models_list):
    for i in range(0,len(phone_models_list)-1):
        model_name=phone_models_list[i].find_element_by_class_name('dl-tile-name')
        el1=phone_models_list[i].find_element_by_class_name('dl-tile-price-wrap')
        el2=el1.find_element_by_class_name('dl-tile-price-month')
        monthly_price=el2.find_element_by_class_name('dl-tile-price')
        #print(model_name.text)
        #print(monthly_price.text)
        if((float(monthly_price.text[1:len(monthly_price.text)-4]))>from_price and float(monthly_price.text[1:len(monthly_price.text)-4])<to_price):
            print(model_name.text)
    
if __name__ == "__main__":
        driver = initialize_driver(browser="chrome")
        welcome_message()
        get_page(driver,"https://www.bell.ca/Mobility/Smartphones_and_mobile_internet_devices");
        prompt_filter_questions();
        phone_models_list=vendor_models(driver);
        price_range_models(driver,phone_models_list)