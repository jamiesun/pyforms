pyforms
=======

python web app forms tools

Code is extracted  from web.py

example of flask 
=================

    #!/usr/bin/env python
    #coding:utf-8

    from flask import Flask
    from flask import request
    import pyforms as form
    app = Flask(__name__)


    is_email = form.regexp('[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$',"Invalid email format")
    is_chars = form.regexp("^[A-Za-z]+$","Must be in English string")
    is_alphanum = lambda x:form.regexp("^[A-Za-z0-9]{%s}$"%x,"Alphanumeric combinations must be length %s"%x)
    is_alphanum2 = lambda x,y:form.regexp("^[A-Za-z0-9]{%s,%s}$"%(x,y),"Must be a length of %s to %s alphanumeric combinations"%(x,y))
    is_number = form.regexp("^[0-9]*$","Must be numeric")
    is_cn = form.regexp("^[\u4e00-\u9fa5],{0,}$","Must be Chinese characters")
    is_url = form.regexp('[a-zA-z]+://[^\s]*',"Invalid url")
    is_phone = form.regexp('^(\(\d{3,4}\)|\d{3,4}-)?\d{7,8}$',"Invalid phone numbers")
    is_idcard = form.regexp('^\d{15}$|^\d{18}$|^\d{17}[Xx]$',"Invalid ID card number")
    is_ip = form.regexp("\d+\.\d+\.\d+\.\d+","无效ip")
    is_rmb = form.regexp('^(([1-9]\d*)|0)(\.\d{2})?$',"Invalid amount of RMB")
    len_of = lambda x,y:form.regexp(".{%s,%s}$"%(x,y),"Length must be %s to %s"%(x,y))

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