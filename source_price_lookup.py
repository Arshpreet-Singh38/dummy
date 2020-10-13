# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 21:06:28 2020

@author: singh
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

preferred_vendor_list=[]
from_monthly_price=""
to_monthly_price=""
from_full_device_price=""
to_full_device_price=""

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
    global preferred_vendor_list
    global from_monthly_price
    global to_monthly_price
    global from_full_device_price
    global to_full_device_price
    
    #The search criteria will be based on the preferred vendors and either desired 24 month monthly price range at $0 down
        #or the desired device full price range.In case no preferred vendors provided program will trace
            #all the available vendors.
    print("Please provide the list of Preferred Vendors ('-1' to Skip or '-1' after listing preferred vendors)?")
    while True:
        preferred_vendor=input()
        if(preferred_vendor!="-1"):
            preferred_vendor_list.append(preferred_vendor)
        else:
            break;
    if(len(preferred_vendor_list)==0):
            preferred_vendor_list=['samsung','apple','lg','google','huawei','TCL','motorola']
    while True:
        try:        
            #Search criteria will be based on either 24 month monthly price range or Full Device Price range only.
            from_monthly_price=float(input("Please provide the lower limit for 24 month monthly price $0 down ('-1' to Skip): "))
            if(from_monthly_price==-1):
                from_full_device_price=float(input("Please provide the lower limit for Full Device Price ('-1' to Skip): "))
                to_full_device_price=float(input("Please provide the upper limit for Full Device Price ('-1' to Skip): "))
                break
            else:
                to_monthly_price=float(input("Please provide the upper limit for 24 month monthly price $0 down ('-1' to Skip): "))
                break
        except ValueError:
            print("Incorrect input for the price range!")
        
#Displaying the BELL Homepage.
def get_page(driver,page):
    driver.get(page)

#Filtering the phone models available for the preferred vendor
def vendor_models(driver,preferred_vendor):
    vendor_main_web = driver.find_element_by_id("filter_nav_"+preferred_vendor.lower())
    # Sending a signal that Return key has been pressed.To Navigate to page of the desired vendor
    vendor_main_web.send_keys(Keys.RETURN)
    el1=driver.find_element_by_id("dl-list-"+preferred_vendor.lower())
    
    #Retrieve the list of phone models available for the preferred vendor
    phone_models_list=el1.find_elements_by_class_name('dl-tile-content')
    return phone_models_list

#Filtering the phone models extracted from the preferred vendors to only the ones that lie
    #within the range of preferred 24 month monthly price range at $0 down 
        #or within the range of preferred full device price.
def price_range_models(driver,phone_models_list):
    price_range_models_list=[]
    for i in range(0,len(phone_models_list)):
        if(from_monthly_price!=-1 and to_monthly_price!=-1):
            try:
                el1=phone_models_list[i].find_element_by_class_name('dl-tile-price-month')
                monthly_price=el1.find_element_by_class_name('dl-tile-price')
                if((float(monthly_price.text[1:len(monthly_price.text)-4]))>=from_monthly_price and float(monthly_price.text[1:len(monthly_price.text)-4])<=to_monthly_price):
                    price_range_models_list.append(phone_models_list[i])
            except NoSuchElementException:
                continue
        else:
            try:
                full_price=phone_models_list[i].find_element_by_class_name('dl-tile-full-price')
                model_full_price=full_price.text[20:]
                if(len(model_full_price)>6):
                    model_full_price=model_full_price[0]+model_full_price[2:] 
                if(float(model_full_price)>=from_full_device_price and float(model_full_price)<=to_full_device_price):
                    price_range_models_list.append(phone_models_list[i])
            except NoSuchElementException:
                continue
    return price_range_models_list

#Extracting the details of the phone models that lie within the preferred 24 month 
    #monthly price range at $0 down or within the range of preferred full device price
        #including model name,full model price,model monthly price and available colors.
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
def display_model_details(models_details_dict,preferred_vendor):
    print("*"*40+"\n"+"\t"+preferred_vendor.upper()+"\n"+"*"*40)
    for i in models_details_dict:
        print("Model Name: "+i)
        details=models_details_dict[i];
        print(details[0]+"\n"+"24-month w/ $0 down price: "+details[1])
        print("Available colors: ",end="")
        for j in range(2,len(details)):
            print(details[j],end=" ")
        print("\n"+"-"*40)

#Exit driver
def shutdown_driver(driver):
    driver.quit()
    
if __name__ == "__main__":
        driver = initialize_driver(browser="chrome")
        welcome_message()
        get_page(driver,"https://www.bell.ca/Mobility/Smartphones_and_mobile_internet_devices")
        prompt_filter_questions()
        for vendor in preferred_vendor_list:
            phone_models_list=vendor_models(driver,vendor)
            price_range_models_list=price_range_models(driver,phone_models_list)
            models_details_dict=models_details(price_range_models_list)
            display_model_details(models_details_dict,vendor)
            print("\n")
        shutdown_driver(driver)