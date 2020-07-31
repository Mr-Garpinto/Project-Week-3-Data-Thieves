#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:30:17 2020

@author: goncalopinto

This code will contain all the functions used to "web scrape" data from youtube and youtube related
"""


from selenium import webdriver
from selenium.common import exceptions
import sys
import time



def scrape(url,driver):


    #driver = webdriver.Safari()
    #url = "https://www.youtube.com/watch?v=6zr0nfG3Xy4&t=5753s" #test url

    driver.get(url)
    driver.maximize_window()
    time.sleep(5)

    try:

        title = driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text
        comment_section = driver.find_element_by_xpath('//*[@id="comments"]')
    except exceptions.NoSuchElementException:

        error = "Error: Double check selector OR "
        error += "element may not yet be on the screen at the time of the find operation"
        print(error)


    driver.execute_script("arguments[0].scrollIntoView();", comment_section)
    time.sleep(10)


    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:

        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")


        time.sleep(10)


        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    
    username_elems = [0]
    comment_elems = [0]
    
    try:
        video_name = driver.find_elements_by_xpath("//yt-formatted-string[@class='style-scope ytd-video-primary-info-renderer']")



        view_count = driver.find_elements_by_xpath("//span[@class='view-count style-scope yt-view-count-renderer']")

        likes_count = driver.find_elements_by_xpath("//yt-formatted-string[@class='style-scope ytd-toggle-button-renderer style-text']")

        dislikes_count = driver.find_elements_by_xpath("//yt-formatted-string[@class='style-scope ytd-toggle-button-renderer style-text']")
        
        username_elems = driver.find_elements_by_xpath('//*[@id="author-text"]')
        comment_elems = driver.find_elements_by_xpath('//*[@id="content-text"]')
    
    except exceptions.NoSuchElementException:
        error = "Error: Double check selector OR "
        error += "element may not yet be on the screen at the time of the find operation"
        print(error)
    
    username_clean = []
    for user in username_elems:
        username_clean.append(user.text)
        
    comments_clean = []
    for comment in comment_elems:
        comments_clean.append(comment.text)
        
    num_views = view_count[0].text
    num_likes = likes_count[0].text
    num_dislikes = dislikes_count[1].text
    name = video_name[0].text
    date = video_name[1].text
        
        

        
    
    return username_clean, comments_clean, num_views, num_likes, num_dislikes, name, date

  

    driver.close()
    print(1)
    time.sleep(15)
    driver.quit()
    print(2)


