from flask import Flask, render_template , request
import sqlite3

file = sqlite3.connect("Student.db",check_same_thread=False)

table = file.execute("select * from sqlite_master where type = 'table' and name = 'student' ").fetchall()

if table != []:
    print("Table exists")
else:
    file.execute('''create table student(
                     id integer primary key autoincrement,
                     name text,
                     branch text,
                     admno integer,
                     roll integer,
                     dob text,
                     sem integer,
                     pass text );''')
    print("Table created")

app = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        getName = request.form["name"]
        getBranch = request.form["branch"]
        getAdmno = request.form["admno"]
        getRoll = request.form["roll"]
        getDob = request.form["dob"]
        getSem = request.form["sem"]
        getPassword = request.form["pass"]
        getCpassword = request.form["cpass"]
        print(getName)
        print(getBranch)
        print(getAdmno)
        print(getRoll)
        print(getDob)
        print(getSem)
        print(getPassword)
        print(getCpassword)

        try:
            file.execute("insert into student(name,branch,admno,roll,dob,sem,pass) \
            values('"+getName+"','"+getBranch+"',"+getAdmno+","+getRoll+",'"+getDob+"','"+getSem+"','"+getPassword+"')")
            file.commit()
            file.close()
            print("Data inserted sucessfully")
        except Exception as error:
            print(error)

    return render_template("register.html")

@app.route('/search')
def search():
    return render_template("search.html")

@app.route('/delete')
def delete():
    return render_template("delete.html")

if __name__ == "__main__":
    app.run()