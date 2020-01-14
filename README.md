# 北大口腔剩余号源爬取程序

## QuickStart

##### 1. 安装虚拟环境并激活  

> supports Python 3.5+
  
##### 2. 安装py module  
 
```shell
pip install -r requirements.txt   
``` 
   
##### 3.  配置爬取规则

```shell
vim (project_path)/etc/rule_settings.py
```  

##### 4. 运行

```shell
nohup python main.py &
```

## Configuration  

> in etc/rule_settings.py
  
sorts        「号种」       
department   「门诊部」  
title        「医师职级」      
doctor       「医师名」  
time         「上/下午」  
week         「星期」  
title_reverse 「反选医师职级」  
doctor_reverse 「反选医生」    

「号种」字段必须填写，想全匹配可在列表里填一个空字符串    
如有多个选择项依次在列表里填多个字符串        
其余字段保留空列表即可  
    
**列表里如果有空串则会匹配全类型，如果有其他数据结构会raise exception**

> in etc/config.py  

BDKQ_HOST **域名(type:str)**    
TICKETS_LEFT_API **剩余票号api(type:str)**  
  
MAIL_HOST **MTA地址(type:str)**  
MAIL_PORT **MTA服务端口(type:int)**  
MAIL_SENDER_USERNAME **发送方邮箱(type:str)**  
MAIL_SENDER_AUTH_KEY **发送方第三方授权码(type:str)**  
MAIL_RECEIVER_USERNAME **收件方邮箱(type:str)**  
  
LOG_LEVEL_DEFAULT **日志默认等级(type:str)**  
  
TLS_VERIFY **API访问TLS验证(type:bool)**  
TLS_WARNING **TLS校验错误提醒(type:bool)**
  
API_TIMEOUT **API访问超时时间(type:tuple)**  
  
SLEEPING_TIME_WHEN_SUCCESS **成功匹配到票号后程序休眠时间(type:float)**  
NORMAL_SLEEPING_TIME **没有匹配到票号后下次访问时间间隔(type:float)**  

EXIT_WHEN_WHEN_SUCCESS  **成功匹配到票号后程序直接退出程序(type:bool)**  

EXIT_WHEN_PARSE_EXCEPTION **程序内部出现异常直接退出程序(type:bool)**  
EXIT_WHEN_REQUEST_EXCEPTION **网络请求出现异常直接退出程序(type:bool)**  



## Extensions

### E-mail Extensions  
因为没接入邮件服务器，本程序的邮件提醒功能需要使用者自备两个邮箱账号。  

一个邮箱账号是发件方(需开启客户端授权码功能)，由程序作为MUA发送给MTA(配置文件里默认设置为smtp.126.com)

另一个账号是收件方，收件人请使用自备的MUA查看邮件提醒。