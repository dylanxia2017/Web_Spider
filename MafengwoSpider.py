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
import unicodedata



infomations = []

def get_Mafengwo(nums):
    print("开始咯..")
    for num in range(1, nums):
        print("正处于第{}页".format(num))
        url = 'https://pagelet.mafengwo.cn/note/pagelet/recommendNoteApi?callback=jQuery1810499468080928426_1578149125286&params={"type":7,"objid":0,"page":' +str(num) + ',"ajax":1,"retina":0}'
        # print(url)
        headers = {
            "cookie":"PHPSESSID=n827scln6h6cell74v1m65d0e0; mfw_uuid=5e0e25c1-cc9b-83ef-dff9-31ecfd7acf5b; uva=s%3A92%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1577985474%3Bs%3A10%3A%22last_refer%22%3Bs%3A24%3A%22https%3A%2F%2Fwww.mafengwo.cn%2F%22%3Bs%3A5%3A%22rhost%22%3BN%3B%7D%22%3B; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1577985474%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=5e0e25c1-cc9b-83ef-dff9-31ecfd7acf5b; __omc_chl=; _r=google; _rp=a%3A2%3A%7Bs%3A1%3A%22p%22%3Bs%3A15%3A%22www.google.com%2F%22%3Bs%3A1%3A%22t%22%3Bi%3A1578059573%3B%7D; oad_n=a%3A5%3A%7Bs%3A5%3A%22refer%22%3Bs%3A22%3A%22https%3A%2F%2Fwww.google.com%22%3Bs%3A2%3A%22hp%22%3Bs%3A14%3A%22www.google.com%22%3Bs%3A3%3A%22oid%22%3Bi%3A1075%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222020-01-03+21%3A52%3A53%22%3B%7D; __mfwothchid=referrer%7Cwww.google.com; __omc_r=www.google.com; __mfwc=referrer%7Cwww.google.com; Hm_lvt_8288b2ed37e5bc9b4c9f7008798d2de0=1577985475,1578059574; __mfwb=a94b33edccb6.1.direct; __mfwa=1577985474268.38277.5.1578111815348.1578140532032; __mfwlv=1578140532; __mfwvn=4; __mfwlt=1578140532; Hm_lpvt_8288b2ed37e5bc9b4c9f7008798d2de0=1578140532",
            "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"
        }
        res = requests.get(url, headers = headers).text

        info = {}
        for data in res.split(" "):
            if data != "" and data.startswith("href") and data[7] != "j" and "i" in data:
                link = data
                print(link)
                new_link = "https://www.mafengwo.cn" + str(link.replace("href=", "").replace("\\", ""))[1:-1]
            elif data.startswith("data-type"):
                data = data.replace("\/","").replace('u\'','\'').encode("utf-8")
                loc = data.decode("unicode-escape")
                pattern = re.compile("[\u4e00-\u9fa5]")
                location = "".join(pattern.findall(loc))
                print(location)

                if location != "":
                    if location not in info:
                        info[location] = new_link
                    else:
                        info[location + "2"] = new_link

        infomations.append(info)

        print(info)
        sleep(np.random.randint(1, 5))

    with open("马蜂窝信息.txt", "w") as f:
        for infoma in infomations:
            f.writelines("%s\n" % infoma)


if __name__ == "__main__":
    get_Mafengwo(6451)



