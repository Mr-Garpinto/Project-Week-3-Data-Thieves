#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 15:43:17 2020

@author: goncalopinto
"""


from selenium import webdriver
from selenium.common import exceptions
import sys
import time

import json

from youtube import*


urls = ["https://www.youtube.com/watch?v=6zr0nfG3Xy4&t=100s"]


dataframe_list = []

cold_storage = []
driver = webdriver.Safari()
for url in urls:
    youtube_dict = {"UserCount": "", "CommentCount": "", "NumViews": "", "NumLikes": "", "NumDis" :"", "VidName":"", "LDate" : "" }
    youtube_cold = {"UserName":[], "Comments":[]}
    
    #username_clean, comments_clean, num_views, num_likes, num_dislikes, name, date
    
    user_names, comments, num_views, num_likes, num_dislikes, name, date = scrape(url, driver)
    
    youtube_dict["UserCount"] = len(user_names)
    youtube_dict["CommentCount"] = len(comments)
    youtube_dict["NumViews"] = num_views
    youtube_dict["NumLikes"] = num_likes
    youtube_dict["NumDis"] = num_dislikes
    youtube_dict["VidName"] = name
    youtube_dict["LDate"] = date
    
    
    
    

    youtube_cold["UserName"] = user_names
    youtube_cold["Comments"] = comments
    
    dataframe_list.append(youtube_dict)
    cold_storage.append(youtube_cold)


with open("testedata.json","w") as file:
    json.dump(dataframe_list,file)
    
with open("testedatacold.json","w") as file:
    json.dump(cold_storage,file)


driver.close()
time.sleep(15)
driver.quit()

print(dataframe_list)



    
