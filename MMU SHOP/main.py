from flask import Flask,  redirect, url_for, render_template, request

app = Flask(__name__)

mmu_student = False

@app.route('/mmustudent/<name>')
def mmustudent(name):  
    return render_template("homepage.html",name=name,mmustudent=mmustudent)


@app.route("/notmmustudent/<name>")
def notmmustudent(name):
    return render_template("homepage.html",name=name)

@app.route("/2-handshop/<name>")
def secondhandshop(name):
    return render_template("2-handshop.html",name=name,mmustudent=mmustudent)

@app.route("/not2-handshop/<name>")
def notsecondhandshop(name):
    return render_template("2-handshop.html" ,name=name)

@app.route("/menspage.html/<name>")
def menspage(name):
    return render_template("menspage.html",name=name,mmustudent=mmustudent)

@app.route("/notmenspage,html/<name>")
def notmenspage(name):
    return render_template("menspage.html",name=name)

@app.route("/mmustuff/<name>")
def mmustuff(name):
    return render_template("mmustuff.html",name=name,mmustudent=mmustudent)

@app.route("/notmmustuff/<name>")
def notmmustuff(name):
    return render_template("mmustuff.html",name=name)





@app.route('/uploadproduct/<name>')
def uploadproduct(name): 
    return render_template("sellerform.html",name=name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    global mmu_student
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if "@student.mmu.edu.my" in email:
            mmu_student = True
            username = email.split('@')[0]
            return redirect(url_for('mmustudent', name=username))
        else:
            mmu_student = False
            username = email.split('@')[0]
            return redirect(url_for('notmmustudent',name=username))
    else:
        return render_template("loginpage.html")
    
def logout():
    response = make_response(redirect(url_for('login')))
    response.set_cookie('mmustudent','',expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True, port=5000)