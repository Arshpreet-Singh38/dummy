# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 20:15:08 2020

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
    price_range_models_list=[]
    for i in range(0,len(phone_models_list)-1):
        el1=phone_models_list[i].find_element_by_class_name('dl-tile-price-wrap')
        el2=el1.find_element_by_class_name('dl-tile-price-month')
        monthly_price=el2.find_element_by_class_name('dl-tile-price')
        if((float(monthly_price.text[1:len(monthly_price.text)-4]))>from_price and float(monthly_price.text[1:len(monthly_price.text)-4])<to_price):
            price_range_models_list.append(phone_models_list[i])
    return price_range_models_list

#Extracting the details of the phone models that lie within the preferred 24 month 
    #monthly price range at $0 down including model name,full model price,model monthly price and available colors.
def models_details(price_range_models_list):
    models_details_dict={}
    for i in range(0,len(price_range_models_list)):
        list1=[]
        model_name=price_range_models_list[i].find_element_by_class_name('dl-tile-name')
        model_full_price=price_range_models_list[i].find_element_by_class_name('dl-tile-full-price')
        el1=price_range_models_list[i].find_element_by_class_name('dl-tile-price-month')
        model_monthly_price=el1.find_element_by_class_name('dl-tile-price')
        list1.append(model_full_price.text)
        list1.append(model_monthly_price.text)
        
        el2=price_range_models_list[i].find_element_by_class_name('dl-tile-colors')
        el3=el2.find_elements_by_tag_name('li')
        for j in range(0,len(el3)):
            available_color=el3[j].get_attribute('data-color-palette')
            list1.append(available_color)
        models_details_dict[model_name.text]=list1
    return models_details_dict

#Displaying the model details including model name,full model price, 24-month w/ $0 down price and available colors.
def display_model_details(models_details_dict):
    print("*"*20+"\n"+"\t"+preferred_vendor.upper()+"\n"+"*"*20)
    for i in models_details_dict:
        print("Model Name: "+i)
        details=models_details_dict[i];
        print(details[0]+"\n"+"24-month w/ $0 down price: "+details[1])
        print("Available colors: ",end="")
        for j in range(2,len(details)):
            print(details[j],end=" ")
        print("\n"+"-"*35)
    
if __name__ == "__main__":
        driver = initialize_driver(browser="chrome")
        welcome_message()
        get_page(driver,"https://www.bell.ca/Mobility/Smartphones_and_mobile_internet_devices");
        prompt_filter_questions();
        phone_models_list=vendor_models(driver);
        price_range_models_list=price_range_models(driver,phone_models_list)
        models_details_dict=models_details(price_range_models_list)
        display_model_details(models_details_dict)