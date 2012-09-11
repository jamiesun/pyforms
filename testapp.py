#!/usr/bin/env python
#coding:utf-8

from __future__ import unicode_literals  
from flask import Flask
from flask import request
import pyforms as form
app = Flask(__name__)


is_email = form.regexp('[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$',"无效的email格式")
is_chars = form.regexp("^[A-Za-z]+$","必须是英文字符串")
is_alphanum = lambda x:form.regexp("^[A-Za-z0-9]{%s}$"%x,"必须是长度为%s的数字字母组合"%x)
is_alphanum2 = lambda x,y:form.regexp("^[A-Za-z0-9]{%s,%s}$"%(x,y),"必须是长度为%s到%s的数字字母组合"%(x,y))
is_number = form.regexp("^[0-9]*$","必须是数字")
is_cn = form.regexp("^[\u4e00-\u9fa5],{0,}$","必须是汉字")
is_url = form.regexp('[a-zA-z]+://[^\s]*',"无效的url")
is_phone = form.regexp('^(\(\d{3,4}\)|\d{3,4}-)?\d{7,8}$',"无效的电话号码")
is_idcard = form.regexp('^\d{15}$|^\d{18}$|^\d{17}[Xx]$',"无效的身份证号码")
is_ip = form.regexp("\d+\.\d+\.\d+\.\d+","无效ip")
is_rmb = form.regexp('^(([1-9]\d*)|0)(\.\d{2})?$',"无效的人民币金额")
len_of = lambda x,y:form.regexp(".{%s,%s}$"%(x,y),"长度必须为%s到%s"%(x,y))

form1 = form.Form(
    form.Textbox("name",is_alphanum2(6,32),description=""),
    form.Password("passwd",is_alphanum2(6,32),description=""),
    form.Textarea("desc",len_of(1,128),description="",rows="5",),
    form.Button("submit", type="submit",html="<b>提交</b>"),
)

def render_form(frm):
    return "<form action='/' method='POST'>%s</form>"%frm.render()

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    iform = form1()
    if request.method == 'GET':
        return render_form(iform)
    elif request.method == 'POST':
        if not iform.validates(source=request.form): 
            return render_form(iform)
        else:
            return "ok"  

if __name__ == '__main__':
    app.run()