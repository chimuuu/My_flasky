# -*-coding:utf-8-*-


from flask import Flask,render_template
from flask.ext.mail import Mail, Message
import os

app = Flask(__name__)
#下面是SMTP服务器配置
app.config['MAIL_SERVER'] = 'smtp.163.com' #电子邮件服务器的主机名或IP地址
app.config['MAIL_PORT'] = '25' #电子邮件服务器的端口
app.config['MAIL_USE_TLS'] = True #启用传输层安全
app.config['MAIL_USERNAME'] = 'w409048772@163.com' #邮件账户用户名
app.config['MAIL_PASSWORD'] = '409048772aaa' #邮件账户的密码

mail = Mail(app)

@app.route('/')
def index():
    msg = Message('主题',sender=os.environ.get('MAIL_USERNAME'),recipients=['1403814829@qq.com'])
    msg.body = '这是一封来自 flask的邮件，正在学习，拿来试试手'
    msg.html = '<b>这是一封来自 flask的邮件，正在学习，拿你来试试手</b> '
    mail.send(msg)

    return '<h1>邮件发送成功</h1>'


if __name__ == '__main__':
	# print MAIL_USERNAME,MAIL_PASSWORD
	app.run(debug=True)
