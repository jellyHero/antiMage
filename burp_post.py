#!/usr/bin/python
# author:Shelly
# time:2018-03-28

def getRequestInfo(messageIsRequest,messageInfo,helpers):
    result = {}
    if messageIsRequest:
        httpService = messageInfo.getHttpService()
        host = httpService.getHost() #<type 'unicode'>
        port = httpService.getPort() #<type 'int'>
        protocol = httpService.getProtocol()#<type 'unicode'>
        request = messageInfo.getRequest()#<type 'java.util.ArrayList'>
        analyzeRequest = helpers.analyzeRequest(httpService,request)
        headers = analyzeRequest.getHeaders()
        body = request[analyzeRequest.getBodyOffset():]
        body_str = body.tostring()#<type 'str'>
        url = analyzeRequest.getUrl() #<type 'java.net.URL'>
        result = {'url':url,'host':host,'port':port,'protocol':protocol,'headers':headers,'body':body_str}
        return result
    else:
        print 'not request'
        pass


def getResponseInfo(messageIsRequest,messageInfo,helpers):
    result = {}
    if not messageIsRequest:
        response = messageInfo.getResponse()
        analyzedResponse = helpers.analyzeResponse(response)
        headers = analyzedResponse.getHeaders()
        body = response[analyzedResponse.getBodyOffset():]
        body_str = body.tostring()
        result = {'headers':headers,'body':body_str}
        return result
    else :
        print 'not response'
        pass


def changeRequest(messageInfo,helpers,new_headers,new_body):
    messageInfo.setRequest(helpers.buildHttpMessage(new_headers, new_body))

def changeResponse(messageInfo,helpers,new_headers,new_body):
    messageInfo.setResponse(helpers.buildHttpMessage(new_headers, new_body))

def sendDataToApi(messageIsRequest,messageInfo,helpers):
    if messageIsRequest:
        httpService = messageInfo.getHttpService()
        host = httpService.getHost() #<type 'unicode'>
        port = httpService.getPort() #<type 'int'>
        protocol = httpService.getProtocol()#<type 'unicode'>
        request = messageInfo.getRequest()#<type 'java.util.ArrayList'>
        analyzeRequest = helpers.analyzeRequest(httpService,request)
        headers = analyzeRequest.getHeaders()
        body = request[analyzeRequest.getBodyOffset():]
        body_str = body.tostring()#<type 'str'>
        url = analyzeRequest.getUrl() #<type 'java.net.URL'>

        # format headers from ARRAY to DICT
        post_headers = {}
        for i in range(0,len(headers)-1):
            j = headers[i]
            if i == 0 :
                post_headers['line1'] = str(j)
            else:
                j_split_array = j.split(':')
                j_split_array_len = len(j_split_array)
                if j_split_array_len == 2 :
                    post_headers[str(j_split_array[0])] = str(j_split_array[1])
                else:
                    head_value = ''
                    for k in range(1,j_split_array_len-1):
                        head_value = head_value + str(j_split_array[k])
                    post_headers[str(j_split_array[0])] = head_value

        postToAPI_data = {'url':str(url),'host':str(host),'port':str(port),'protocol':str(protocol),'headers':post_headers,'body':body_str}

        #if requests not in blacklist,send to api
        def getReqType(post_headers):
            url_path = post_headers['line1'].split(' ')[1]
            if '.' in url_path :
                return url_path.split('.')[1]
            else :
                return ' '
        reqType_blackList = ['htm','html','js','png','jpg']
        if getReqType(post_headers) not in reqType_blackList:
            postToAPI('http://127.0.0.1:1858/postDataApi','print','utf-8',postToAPI_data)

sendDataToApi(messageIsRequest,messageInfo,helpers)

'''
if messageIsRequest:
    request = getRequestInfo(messageIsRequest,messageInfo,helpers)
    new_requestHeaders = request['headers']
    new_requestBody = request['body']
    changeRequest(messageInfo,helpers,new_requestHeaders,new_requestBody)


if not messageIsRequest:
    response = getResponseInfo(messageIsRequest,messageInfo,helpers)
    new_responseHeaders = response['headers']
    new_responseBody = 'hello ! burp script!'
    changeResponse(messageInfo,helpers,new_responseHeaders,new_responseBody) 
'''