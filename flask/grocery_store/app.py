from flask import Flask, render_template, request, redirect, url_for, flash
from database import DatabaseManager

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for flash messages

# Initialize database manager
db_manager = DatabaseManager({
    'user': 'root',
    'password': 'Hrhk@9090',
    'host': 'localhost',
    'database': 'grocery_store'
})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find_bill', methods=['POST'])
def find_bill():
    bill_number = request.form['bill_number']
    customer_name = request.form['customer_name']
    result = db_manager.find_bill(bill_number, customer_name)

    if result:
        return render_template('bill.html', bill=result)
    else:
        flash('Bill not found!', 'error')
        return redirect(url_for('index'))

@app.route('/save_bill', methods=['POST'])
def save_bill():
    # Logic to save the bill
    return redirect(url_for('index'))

@app.route('/share_bill', methods=['POST'])
def share_bill():
    # Logic to share the bill via email
    return redirect(url_for('index'))

if __name__ == '_main_':
    app.run(debug=True)