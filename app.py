# from flask import Flask, request, render_template
# import psycopg2

# app = Flask(__name__)

# # Database connection
# def get_db_connection():
#     conn = psycopg2.connect(
#         host="localhost",
#         database="crop",
#         user="postgres",
#         password="Aayush@123"
#     )
#     return conn

# # Route to serve the HTML form
# @app.route('/form')
# def form():
#     return render_template('crop_form.html')  
# # The HTML file should be inside the 'templates' folder
# @app.route('/index')
# def index():
#     return render_template('index.html') 
# @app.route('/crops')
# def crops():
#     return render_template('crops.html') 
# @app.route('/contact')
# def contact():
#     return render_template('contact.html') 
# # Route to handle form submission
# @app.route('/submit_crop', methods=['POST'])
# def submit_crop():
#     crop_name = request.form['crop_name']
#     quantity = request.form['quantity']
#     price = request.form['price']
#     farmer_name = request.form['farmer_name']

#     conn = get_db_connection()
#     cursor = conn.cursor()

#     # Insert crop data into the PostgreSQL database
#     cursor.execute(
#         "INSERT INTO crops (crop_name, quantity, price, farmer_name) VALUES (%s, %s, %s, %s)",
#         (crop_name, quantity, price, farmer_name)
#     )

#     conn.commit()
#     cursor.close()
#     conn.close()

#     return "Crop info submitted successfully!"

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="crop",
        user="postgres",
        password="Aayush@123"
    )
    return conn

# Route to serve the HTML form
@app.route('/form')
def form():
    return render_template('crop_form.html')
@app.route('/index')
def index():
    return render_template('index.html') 
@app.route('/crops')
def crops():
    return render_template('crops.html') 

# Route to handle form submission
@app.route('/submit_crop', methods=['POST'])
def submit_crop():
    crop_name = request.form['crop_name']
    quantity = request.form['quantity']
    price = request.form['price']
    farmer_name = request.form['farmer_name']

    conn = get_db_connection()
    cursor = conn.cursor()

    # Insert crop data into the PostgreSQL database
    cursor.execute(
        "INSERT INTO crops (crop_name, quantity, price, farmer_name) VALUES (%s, %s, %s, %s)",
        (crop_name, quantity, price, farmer_name)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return "Crop info submitted successfully! <br><a href='/view_crops'>View all crops</a>"

# Route to display all submitted crop data
@app.route('/view_crops')
def view_crops():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch all crop data from the database
    cursor.execute('SELECT crop_name, quantity, price, farmer_name FROM crops')
    crops = cursor.fetchall()

    cursor.close()
    conn.close()
    print(crops)
    if not crops:
        return "No crops have been submitted yet."

    return render_template('view_crops.html', crops=crops)

if __name__ == "__main__":
    app.run(debug=True)