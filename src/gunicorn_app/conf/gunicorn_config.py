import os

bind = "%s:%s"%(os.environ.get('GUIP','0.0.0.0'),os.environ.get('PORT','8090'))
workers = 2
threads = 4


errorlog = '-'
loglevel = 'info'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
