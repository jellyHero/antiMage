1、简介
	通过burpsuit插件（scripter），抓取burpsuit符合规则的请求，将其发送到api接口（http服务），并调用api接口上的扫描模块进行扫描。

2、使用方法

	2、1 修改scripter插件
		将修改后burpscripter.py放到原位置，主要是在插件里新添了函数postToAPI

	2、2 添加基于burp的数据采集
		将burp_post.py的代码复制到scripter插件的输入框

		主要实现以下2个功能：
		i 统一接受数据格式：
		{'action':'print','charset':'utf-8','postData':postData_dict}
		其中：
		postData_dict:
		{'url':url,'host':host,'port':port,'protocol':protocol,'headers':headers_dict,'body':body_str}
		action:标志收到数据后，做何种处理
		如只进行sql注入扫描，还是进行全部扫描
		charset：编码方式，默认设为utf-8，此外还有iso、gbk
		postData_dict：传递的http请求数据
		url：网址
		host：主机
		port：端口
		protocol：协议
		headers：http头，请设置为字典类型
		body：数据内容，请设置为字符串类型

		ii 筛选符合格式的请求：
		目前采用黑名单筛选：后缀不在黑名单的，发送到api接口
		reqType_blackList = ['htm','html','js','png','jpg']

	2、3 开启api服务
		python3 main.py

3、开发进度

	2019/01/14
	完成基于burp的数据采集初版
	完成main.py初版：目前直接对接收到数据进行打印，未做其他处理
	下一步计划：添加data模块，采用sqlite3对接收的数据进行排序、存储