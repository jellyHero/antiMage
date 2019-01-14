import urllib
import urllib2
import json

def postToAPI(api_url,action,charset,postData):
    reqdata = {'action':action,'charset':charset,'postData':postData}
    headers = {'Content-Type': 'application/json'}
    req = urllib2.Request(url = api_url,headers=headers,data =json.dumps(reqdata))
    res_data = urllib2.urlopen(req)

postToAPI('http://127.0.0.1:1858/postDataApi','print','utf-8',{'headers': {'Accept': ' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Connection': ' close', 'User-Agent': ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 'Host': ' www.t00ls.net', 'Cache-Control': ' max-age=0', 'Upgrade-Insecure-Requests': ' 1', 'Accept-Language': ' zh-CN,zh;q=0.9', 'line1': 'GET /index.php HTTP/1.1'}, 'body': '', 'url':u'https://www.t00ls.net:443/index.php', 'protocol': u'https', 'port': 443, 'host': u'www.t00ls.net'})