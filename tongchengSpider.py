import requests
from bs4 import BeautifulSoup
from lxml import html
import warnings
from time import sleep
import numpy as np
from scrapy import Selector
import pandas as pd
from datetime import datetime
import multiprocessing
import re
import json


def get_links(nums):
    links = []
    headers = {
        "cookies":"COMSEInfo=RefId=14355888&SEFrom=google&SEKeyWords=&RefUrl=; 17uCNRefId=RefId=14211860&SEFrom=google&SEKeyWords=; TicketSEInfo=RefId=14211860&SEFrom=google&SEKeyWords=; CNSEInfo=RefId=14211860&tcbdkeyid=&SEFrom=google&SEKeyWords=&RefUrl=https%3A%2F%2Fwww.google.com%2F; __tctmu=144323752.0.0; longKey=1578059534808521; __tctrack=0; qdid=35294|1|14211860|be6ca5,35294|1|14211860|be6ca5; Hm_lvt_c6a93e2a75a5b1ef9fb5d4553a2226e5=1578059535,1578069771; Hm_lvt_d3dcbf14b43296ccba0611c7d61e927a=1578059535,1578069771; __tctma=144323752.1578059534808521.1578059534481.1578067556777.1578069771033.3; __tctmz=144323752.1578069771033.3.2.utmccn=(referral)|utmcsr=google.com|utmcct=|utmcmd=referral; Hm_lpvt_c6a93e2a75a5b1ef9fb5d4553a2226e5=1578070826; route=dbd8b6b8ef73d1d38f7a84a4020fe96c; Hm_lpvt_d3dcbf14b43296ccba0611c7d61e927a=1578070826; __tctmc=144323752.6028853; __tctmd=144323752.203042327; __tctmb=144323752.2171353891148171.1578069771033.1578070826615.2",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"
    }

    links = []
    for i in range(1, nums):
        print("当前正处于第{}页".format(i))
        url = "https://www.ly.com/travels/home/GetJingHuaYouJiListToIndex?pindex={}&psize=10&iid=0.31439625475259003".format(i)
        try:
            res = requests.get(url, headers = headers)
            res_json = json.loads(res.text)
            for data in res_json["Obj"]["YouJiList"]:
                # print(data["travelNoteId"])
                links.append("https://www.ly.com/travels/" + str(data["travelNoteId"]) + ".html")

            sleep(np.random.randint(1, 5))

        except:
            print("网页无法获取")

    with open("同程旅游.txt", "w") as f:
        for link in links:
            f.writelines("%s\n" % link)


# def get_content():


if __name__ == "__main__":
    get_links(99)
    print("Done")