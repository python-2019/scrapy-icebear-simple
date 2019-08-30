import json

import requests

if __name__ == '__main__':
    url = "https://icebear.me/job"
    method = "POST"
    headers = {
        "Content-Type": "application/json",
        ":authority": "icebear.me",
        ":method": "POST",
        ":path": "/job",
        ":scheme": "https",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-length": "28",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": "_ga=GA1.2.706103452.1567131638; _gid=GA1.2.1209515709.1567131638; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216ce0531e27695-0eee45636b0755-34594974-2073600-16ce0531e2930a%22%2C%22%24device_id%22%3A%2216ce0531e27695-0eee45636b0755-34594974-2073600-16ce0531e2930a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _hjid=f00a2064-982f-4ce2-9c9f-6e0deba0b2d4; session_login_token=1; PHPSESSID=m91t46vi6qvukk6sere1g4fgj8; session_login_token_login_info=bfAUQ3TXwfxUAJwnpD4pwkOwwT-CZI4aWfmM-b184CfKzCjF2nzbyCcxtvPbxXEF6iMTT6c3r5k16o5AnwqCsfKqoDhNdoUbnpKS8rWmXeGiFxxJtedC5flU60xPao4FMjqs-m-8jsUxZO0c6VVPOjd-apW5cFjbLiM3-fjpJUqJ4RaxhfNFQx1NpOtKX1PyVn2kumLe73Al3bLfvkd4kChVAeiJbDp6aaifkSymV26ydIMS9h6xGZmDUBYs8Bb4uHh8wgdAYFB0MtnHTCIPNHgWhKtXRVIgDmpqQ3iSjC7tZ7RguZ6Fiqik-dMi-uP31aL7VRPpqsEudm4GmhOmp9fz6S5s6MAXNvjZstNHMBmZZotNwCFUtDW15Yx0ZAxoZDrsyGcJxAbXhaTwMbDckaxLFCSBLjHyYSI9Z5upAIvk0RpkuSeyz4a9Lzks0klsO2s8EHy1xS0",
        "origin": "https://icebear.me",
        "pragma": "no-cache",
        "referer": "https://icebear.me/job.html",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3738.400",
        "x-requested-with": "XMLHttpRequest"
    }
    request = requests.request(method, url, headers=headers)
    print(request.text)
