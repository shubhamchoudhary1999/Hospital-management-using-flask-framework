from flask import *
import pymysql

db=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="hospital"
    )
cursor=db.cursor()

app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/AddPatient")
def AddPatient():
    cursor.execute("select * from nacl")
    data=cursor.fetchall()
    return render_template("addpatient.html",userdata=data)

@app.route("/create",methods=["POST"])      

def create():
    pid=request.form.get('pid')
    room_no=request.form.get('room_no')
    first_name=request.form.get('first_name')
    last_name=request.form.get('last_name')
    sex=request.form.get('sex')
    date_of_birth=request.form.get('date_of_birth')
    address=request.form.get('address')
    age=request.form.get('age')
    blood_group=request.form.get('blood_group')
    city=request.form.get('city')
    date_register=request.form.get('date_register')
    insq="insert into nacl(pid,room_no,first_name,last_name,sex,date_of_birth,address,age,blood_group,city,date_register)values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(pid,room_no,first_name,last_name,sex,date_of_birth,address,age,blood_group,city,date_register)
    try:
        cursor.execute(insq)
        db.commit()
        return redirect(url_for("AddPatient"))
    except:
        db.rollback()
        return "error in query"
    
@app.route("/delete")
def delete():
    pid=request.args.get('pid')
    delq="delete from nacl where pid={}".format(pid)
    try:
        cursor.execute(delq)
        db.commit()
        return redirect(url_for("AddPatient"))
    except:
        db.rollback()
        return("error in query")
   
@app.route("/edit")
def edit():
    pid=request.args.get('pid')
    selq="select * from nacl where pid={}".format(pid)
    cursor.execute(selq)
    data=cursor.fetchone() 
    return render_template("editdetail.html",row=data)


@app.route("/update",methods=["POST"])
def update():
    pid=request.form.get('pid')
    room_no=request.form.get('room_no')
    first_name=request.form.get('first_name')
    last_name=request.form.get('last_name')
    sex=request.form.get('sex')
    date_of_birth=request.form.get('date_of_birth')
    address=request.form.get('address')
    age=request.form.get('age')
    blood_group=request.form.get('blood_group')
    city=request.form.get('city')
    date_register=request.form.get('date_register')
    insq="update nacl set room_no='{}',first_name='{}',last_name='{}',sex='{}',date_of_birth='{}',address='{}',age='{}',blood_group='{}',city='{}',date_register='{}' where pid={}".format(room_no,first_name,last_name,sex,date_of_birth,address,age,blood_group,city,date_register,pid)
    try:
        cursor.execute(insq)
        db.commit()
        return redirect(url_for("AddPatient"))
    except:
        db.rollback()
        return "error in query"
@app.route("/SearchPatient")
def SearchPatient():
    return render_template("searchpatient.html")


@app.route("/getdata",methods=["POST"])
def getdata():
    pid=request.form.get('pid')
    selq="select * from nacl where pid={}".format(pid)
    cursor.execute(selq)
    data=cursor.fetchone()
    return render_template("searchpatient.html",row=data)

if __name__=="__main__":
    app.run(debug=True)
