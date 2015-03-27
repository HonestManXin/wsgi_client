from f_client import FCGIApp

sock_file = "/home/s/apps/xenwebsensor/xenwebsensor/run/xenadmin-fastcgi.sock"
app = FCGIApp(sock_file)
env = {
       'SCRIPT_FILENAME': "/",
       'QUERY_STRING': '',
       'REQUEST_METHOD': 'GET',
       'SCRIPT_NAME': "/",
       'REQUEST_URI': "/home/",
       'GATEWAY_INTERFACE': 'CGI/1.1',
       'SERVER_SOFTWARE': 'ztc',
       'REDIRECT_STATUS': '200',
       'CONTENT_TYPE': '',
       'CONTENT_LENGTH': '0',
       #'DOCUMENT_URI': url,
       #'DOCUMENT_ROOT': '/',
       #'DOCUMENT_ROOT': '/var/www/',
       'SERVER_PROTOCOL' : 'HTTP/1.1',
       'REMOTE_ADDR': '127.0.0.1',
       'REMOTE_PORT': '8899',
       'SERVER_ADDR': "127.0.0.1",
       'SERVER_PORT': "80",
       'SERVER_NAME': "localhost"
}
ret = app(env, None)
print ret
