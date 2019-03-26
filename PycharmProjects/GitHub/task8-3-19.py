
# ##Start Excercise_________________________________________
# Exercise 1: Ran code in terminal
# import random

#  random.randint(5, 10)
# 10
#  random.randint(5, 10)
# 9
#  t =[21,22,32]
#  random.choice(t)
# 21
#  t=[1,3,6]
#  random.choice(t)
# 1
#  t=[32,20,33]
#  random.choice(t)
# 33

# ##Start Excercise_________________________________________
# Exercise 2: Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get.
# repeat_lyrics()
# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print('I sleep all night and I work all day.')

# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()

# Answer: the following errors_______________________
# Traceback (most recent call last):
#   File "main.py", line 16, in <module>
#     repeat_lyrics()
# NameError: name 'repeat_lyrics' is not defined

# ##Start Excercise_________________________________________
# Exercise 3:

# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print('I sleep all night and I work all day.')

# repeat_lyrics()

# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()
# Answer: the following errors_______________________
# Traceback (most recent call last):
#   File "main.py", line 18, in <module>
#     ___________
# NameError: name '___________' is not defined

# ##Start Excercise_________________________________________
# Exercise 4: What is the purpose of the "def" keyword in Python?
# Answer is d) both true -It indicates the start of a function & It indicates that the following indented section of code is to be stored for later

# ##Start Excercise_________________________________________
# Exercise 5:
# Answer is d)

# ##Start Excercise_________________________________________
# Exercise 6:
##Code Start-my version 1______
# def computepay(hours,rate):
#   if hours > 0 and rate > 0:
#     if hours > 40:
#       pay = (40 * rate) + ((hours - 40) * 1.5 * rate)
#     else:
#       pay = (hours * rate)
#     return pay
#   else:
#     print('please check hours or rates')
## End Code______

##Code Start- my version 1.4______
# def computepay(hours,rate):
#   try:
#     hours = float(hours)
#     rate = float(rate)
#     if hours > 0 and rate > 0:
#       if hours >= 40:
#         pay = (40 * rate) + ((hours - 40) *1.5*rate)
#         return pay
#       else:
#         pay = (hours * rate)
#         return pay
#   except:
#     print('please check hours or rates')

# print(computepay(41,10))
# print(computepay(41,0))
# print(computepay(41,1))
# print(computepay(41,"hello"))
## End Code______

# ##Start Excercise_________________________________________
# Exercise 7:
##Code Start______

def computegrade(score):
  try:
    score = float(score)
    if score >= 0.9 and score <=1.0:
      return "A"
    elif score >= 0.8 and score <0.9:
      return "B"
    elif score >= 0.7 and score <0.8:
      return "C"
    elif score >= 0.6 and score <0.7:
      return "D"
    elif score < 0.5 and score >=0 :
      return "F"
    else:
      return "Bad Score"
  except:
    return "Bad Score"

prompt = "Please enter score between 0.0 and 1.0\n"
enter_score = (input(prompt))
print(computegrade(enter_score))
## End Code______
from flask import Flask, jsonify, request, url_for, redirect, session, render_template, g
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Thisisasecret!'

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'strata'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

flaskmysql = MySQL()
flaskmysql.init_app(app)

def connect_db(flaskmysql):
    con = flaskmysql.connect()
    return con

def get_db(flaskmysql):
    if not hasattr(g, 'mysql_db'):
        g.mysql_db = connect_db(flaskmysql)
    return g.mysql_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'mysql_db'):
        g.mysql_db.close()

@app.route('/')
def index():

    return "<h1>Strata Issues</h1><button onclick=""window.location.href='create'"">Raise Issue</button>"


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    else:
        issue_description = request.form['issue_description']
        con = get_db(flaskmysql)
        cur = con.cursor()
        cur.execute('insert into issues (issue_description) values (%s)', (issue_description))
        con.commit()
        return redirect(url_for('read'))

@app.route('/read', methods=['POST', 'GET'])
def read():
    con = get_db(flaskmysql)
    cur = con.cursor()
    cur.execute('select * from issues')
    results = cur.fetchall()
    #Start - Conversion from Tuples to Dictionary (Copied from Stack Overflow =))
    def Convert(tup, di):
        di = dict(tup)
        return di
    dictionary = {}
    results_dict = Convert(results, dictionary)
    print('results_dict : ', results_dict)
    return render_template('read.html', results_dict=results_dict)

@app.route('/update', methods=['GET', 'POST'])
def update():
    con = get_db(flaskmysql)
    cur = con.cursor()
    cur.execute('update issues \
                    set issue_description = %s \
                  where issue_number = %s', ('dummyname',1))
    con.commit()
    return redirect(url_for('read'))

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    con = get_db(flaskmysql)
    cur = con.cursor()
    cur.execute('delete from issues \
                  where issue_number = %s', (2))#need delete to become like update and have delete by itself it from line 2.
    con.commit()
    return redirect(url_for('read'))

if __name__ == '__main__':
    app.run()
