import mysql.connector as connection
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

# Connection with Mysql database
conn = connection.connect(
    host='localhost',
    user='root',
    password='Dreams@2024',
    database='login_info',
    use_pure=True
)
cur = conn.cursor()

# Route for Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Route for rental Login
@app.route('/login')
def login():
    return render_template('register.html')

# Route for Registration for rental
@app.route('/registration', methods=['POST'])
def form():
    name = request.form.get('name')
    email = request.form.get('email')
    password = str(request.form.get('pass'))
    cur.execute("use login_info")
    query = " INSERT INTO credentials values(%s, %s, %s)"
    val = [(name, email, password)]
    cur.executemany(query, val)
    conn.commit()
    return render_template("signin.html")


# link for returnig page after signing in 
@app.route('/sign_in', methods=['POST'])
def sign_in():
    # email = request.form.get('email')
    # password = str(request.form.get('pass'))

    # cur.execute("SELECT email, password FROM credentials WHERE email = email", (email,))
    # user = cur.fetchone()
    # if user is not None and user[1] == password:
    #     return "Login succesfull"
    # else:
    #     return render_template('register.html', error="Invalid email or password")

    return render_template('rental.html')


# Link if rental is already logged in
@app.route('/member')
def member():
    return render_template('signin.html')

# Link for register
@app.route('/register')
def registration():
    return render_template('register.html')

# Route for submission form for Rental person
@app.route('/rental',methods=['POST'])
def rent_client():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    farm_name = request.form.get('farm_name')
    address = request.form.get('address')
    city = request.form.get('city')
    state = request.form.get('state')
    zip = request.form.get('zip')
    Acres = request.form.get('Acres')
    Rent = request.form.get('Rent')
    description = request.form.get('description')
    cur.execute("use login_info")
    query = " INSERT INTO rental_info values(%s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)"
    val = [(name, email, phone, farm_name,address, city, state, zip,Acres,Rent, description)]
    cur.executemany(query, val)
    conn.commit()
    return "Your requst is submitted succesfully, farmer will call you..."

# Route for farmer login
@app.route('/farmer_login2')
def farmer_registration():
    return render_template('farmer_login.html')

# Route for farmer Registration
@app.route('/farmer_registration',methods=['POST'])
def farmer_data():
    name = request.form.get('name')
    mobile = request.form.get('mobile')
    location = request.form.get('location')
    Address = request.form.get('Address')
    experience = request.form.get('experience')
    cur.execute("use login_info")
    query2 = " INSERT INTO farmer_login values(%s, %s, %s, %s,%s)"
    val = [(name, mobile, location, Address, experience)]
    cur.executemany(query2, val)
    conn.commit()
    return "Your registration is succesfull "

# Route for buying machinaries
@app.route('/machinary')
def machinaries():
    return render_template('buy_machinary.html')

# Redirecting from home page
@app.route('/first_login')
def first_login():
    return render_template('farmer_login.html')

# Redirecting from home page
@app.route('/rent')
def rent():
    return render_template('signin.html')

if __name__ == '__main__':
    app.run(debug=True)