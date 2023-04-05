# -*- coding: utf-8 -*-
# @Time: 2023年03月02日17时05分
# @File: 图片.py
import requests
import re

try:
    url = input('输入链接地址: ')
    obj = re.compile(r"http.*/", re.S)
    url = obj.finditer(url)

    for i in url:
        pid = i.group()
        print(i.group())
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        'cookie': '__ac_nonce=064009406003db16b655a; __ac_signature=_02B4Z6wo00f01OB8KJgAAIDDKMDhh5TecCzgXCwAAFwle6; ttwid=1%7CCTBQOahTiOJ0ZMjznnb92DErTXIkPk1PcZwkmkEJjvQ%7C1677759494%7Cf3431f1918913bdc618ed28082b9bf864c8cb34bc96f9ef9df5e4793bf17670d; douyin.com; home_can_add_dy_2_desktop=%220%22; strategyABtestKey=%221677759476.529%22; passport_csrf_token=b9fe6f05abc17e50df2ae7ca40625f84; passport_csrf_token_default=b9fe6f05abc17e50df2ae7ca40625f84; s_v_web_id=verify_ler2o9t5_ByuEiHoS_Y4So_4Z5o_9ovX_KPxdrm0FW4B4; csrf_session_id=f0ede1751d0a21c9f2059b097620860c; ttcid=9f3577324d8646b18c5482c581e3a2b738; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWNsaWVudC1jc3IiOiItLS0tLUJFR0lOIENFUlRJRklDQVRFIFJFUVVFU1QtLS0tLVxyXG5NSUlCRGpDQnRRSUJBREFuTVFzd0NRWURWUVFHRXdKRFRqRVlNQllHQTFVRUF3d1BZbVJmZEdsamEyVjBYMmQxXHJcbllYSmtNRmt3RXdZSEtvWkl6ajBDQVFZSUtvWkl6ajBEQVFjRFFnQUVGZlVtSXhzMUNQOTEwbnRRUGkxN3B6RUpcclxuZENvcm5BZnpCV01QTWhrOFV4RVNNMkphcUljREYxTW1ydHVUNWhpMUY1RFVBNGo4RXF0cW55S1FhbFBXd0tBc1xyXG5NQ29HQ1NxR1NJYjNEUUVKRGpFZE1Cc3dHUVlEVlIwUkJCSXdFSUlPZDNkM0xtUnZkWGxwYmk1amIyMHdDZ1lJXHJcbktvWkl6ajBFQXdJRFNBQXdSUUloQU9GWXg4RGVMaUcwMWVEVHdlNUtvR2dVc3NiYWQ3ajhkV1VBcE9WL1Y5RzZcclxuQWlCS256WTAwSmFmWmhvUnpadndzejBCUUJ4MVhIYTFHc2U4OVBVdStQaVRCdz09XHJcbi0tLS0tRU5EIENFUlRJRklDQVRFIFJFUVVFU1QtLS0tLVxyXG4ifQ==; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20230302%22; msToken=QAk0_NtZEestmvcqWug8skFf2tcZV3RxUk1PV4nu2zUWJ1tqWh5h0JG5p911FtK1vHTWW-erY6vjCkfqNboz2qPdeZ_5b5QBYFVNv0I4UVu-FbD88q76_9BRd8caGg==; msToken=5kESc8ybkAeXkNt_idCfS2K4WNprEF_AwThfu0QudgisFVFcgUIpQCIWoCZ8NYO1scUJ4KRS6VXc81n4yLDcxMkE6Ak0sPXs3eIKWuTwdk9zPvyYdncrsv4RZoJNcHA=; tt_scid=I9HGHAgkPbQ58WqFmU9LAlp.N9vgfGnk6RY0V2So9VBu0Ntt6LGO4bHSyXHU8mK96c06'
    }

    resp = requests.get(url=pid, headers=headers, allow_redirects=False)

    print(resp.text)
    pid = re.finditer(r"video/(?P<IID>.*?)/", resp.text)

    for i in pid:
        ID = i.group('IID')
        print(i.group('IID'))

    resp1 = 'https://www.douyin.com/note/' + ID

    print(resp1)

    res = requests.get(resp1, headers=headers, allow_redirects=False)


    a = re.findall('<div class=".*?"><img class=".*?" src="(.*?)"/></div>', res.text, re.S)

    for index,i in enumerate(a):
        b = re.sub('amp;', "", i)
        print(b,index)
        with open(f'image//{index}' + '.jpg', 'wb') as f:
            jpg = requests.get(url=b, headers=headers).content
            f.write(jpg)
except:
    print('解析异常')
