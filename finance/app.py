import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    portfolio = db.execute("SELECT symbol, SUM(shares) AS total_shares FROM purchases WHERE username = ? GROUP BY symbol HAVING total_shares > 0", session["user_id"])

    # Initialize variables
    grand_total = 0
    rows = []

    # Iterate through the user's portfolio
    for item in portfolio:
        symbol = item["symbol"]
        total_shares = item["total_shares"]

        stock = lookup(symbol)

        if stock:
            price = stock["price"]
            total_value = total_shares * price
            grand_total += total_value

            rows.append({"symbol": symbol, "shares": total_shares, "price": price, "total_value": total_value})

    # Retrieve user's current cash balance
    user_balance = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]

    username = session.get('user_name', 'Guest')

    # usd(usflasker_balance)
    # Calculate grand total
    grand_total += user_balance

    # usd(grand_total)
    # Render template
    return render_template("index.html", user_balance=user_balance, rows=rows, grand_total=grand_total, username=username)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""




    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        stock = lookup(symbol)

        try:
            shares = int(shares)
        except ValueError:
            return apology("Shares must be a valid integer", 400)

        if not symbol:
            return apology("Missing symbol")
        elif shares <= 0:
            return apology("Input is not a positive integer of shares",400)
        if not stock:
            return apology("Stock not found", 400)

    # calc the total cost of the user's share purchase
        share_cost = stock["price"] * shares

        # Query database to get user's cash balance
        user_balance = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]

        if user_balance < share_cost:
            return apology("Insufficient funds", 403)

        remaining_balance = user_balance - share_cost
        db.execute("UPDATE users SET cash = ? WHERE id = ?", remaining_balance, session["user_id"])

        # Insert the purchase into the transactions table
       # Check if the symbol already exists in the purchases table
        existing_purchase = db.execute("SELECT * FROM purchases WHERE username = ? AND symbol = ?", session["user_id"], symbol)

        if existing_purchase:
            # If the symbol exists, update the shares
            user_shares = int(existing_purchase[0]["shares"])
            remaining_shares = user_shares + shares
            db.execute("UPDATE purchases SET shares = ? WHERE username = ? AND symbol = ?", remaining_shares, session["user_id"], symbol)
        else:
            # If the symbol doesn't exist, insert a new entry
            db.execute("INSERT INTO purchases (username, symbol, shares, total) VALUES (?, ?, ?, ?)",
                    session["user_id"], symbol, shares, stock["price"])

        # history
        dt=datetime.now()
        transaction_type="buy"
        db.execute("INSERT INTO transactions (user, symbol, number,type, price,date) VALUES (?, ?, ?, ?, ?, ?)", session["user_id"], symbol, shares, transaction_type, float(stock["price"]), dt)

        
        # Flash success message
        flash("Stock purchase successful!", "success")
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("select * from transactions where user = ? ",session["user_id"])
    tt = []
    if transactions:
        for transaction in transactions:
            if transaction["type"] == "sell":
                transaction["number"] = str("-")+str(transaction["number"])
            tt.append(transaction)
    return render_template("history.html",transactions=tt)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["user_name"] = rows[0]["username"]



        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol=request.form.get("symbol")

        stock = lookup(symbol)

        if stock:
            return render_template("quoted.html", stock=stock)
        else:
            return apology("Symbol not found", 400)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
        # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")


        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)
        elif password !=confirmation:
            return apology("passwords do not match", 400)

        exists = db.execute("SELECT * FROM users WHERE username = ?", name)

    # Check if username already exists
        if exists:
            return apology("username already exists", 400)

        # hashing password using werkzeug.security
        hashed_password = generate_password_hash(password)

        # Query database for username
        db.execute("insert into users (username,hash) VALUES (?, ?)", name, hashed_password)

        # Flash success message
        flash("Register successful!", "success")
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get('symbol')
        shares = request.form.get('shares')

        # TODO: Validate input and sell the shares
        if not request.form.get('symbol'):
            return apology("Not a valid symbol", 400)
        elif not request.form.get("shares"):
            return apology("Not a valid amount", 400)

        # elif not shares or not shares.replace(".", "").isdigit()  or float(shares) <= 0:
        #     return apology("Number of share must must a positive number", 400)

        user_stocks = db.execute("select distinct symbol,SUM(shares) as total from purchases where username = ? GROUP BY symbol HAVING total > 0",session["user_id"])

        # Check if the user has enough shares to sell
        user_shares = user_stocks[0]["total"]
        if int(float(shares)) > user_shares:
            return apology("You do not have enough shares to sell", 400)

        #check stock price of share
        stock_info = lookup(symbol)

        if not stock_info:
            return apology("You do not own this stock", 400)

        profit = stock_info["price"] * int(float(shares))

        user_balance = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
        user_balance += profit
        db.execute("UPDATE users SET cash = ? WHERE id = ?", user_balance, session["user_id"])

        # update user portfolio
        remaining_shares = int(user_shares) - int(float(shares))
        db.execute("UPDATE purchases SET shares = ? WHERE username = ? AND symbol = ? ", remaining_shares, session["user_id"], symbol)

        # history
        dt=datetime.now()
        transaction_type="sell"
        db.execute("INSERT INTO transactions (user, symbol, number,type, price,date) VALUES (?, ?, ?, ?, ?, ?)", session["user_id"], symbol, shares, transaction_type, float(stock_info["price"]), dt)

        # Flash success message
        flash("Stock sold successfully!", "success")
        # Redirect the user to the home page after selling
        return redirect('/')
    else:
        # Render the form for selling stocks
        user_stocks = db.execute("select symbol from purchases where username = ?",session["user_id"])
        user_stocks = [row["symbol"] for row in user_stocks]
        return render_template('sell.html', user_stocks=user_stocks)

@app.route("/profile", methods=["GET","POST"])
@login_required
def profile():
    """Change user password"""
    if request.method == "POST":
        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")
        confirm = request.form.get("confirm")

        # ensure every required field has been passed
        if not old_password:
            return apology("Please provide your old password", 403)
        elif not new_password:
            return apology("Please provide new password", 403)
        elif not confirm:
            return apology("Please confirm new password", 403)

        #  Query database for username
        rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"] )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], old_password
        ):
            return apology("Invalid password", 403)

        # change password
        if new_password == confirm:
            hashed_password = generate_password_hash(new_password)
            db.execute("UPDATE users SET hash = ? WHERE id = ?",hashed_password,session["user_id"])
            return apology("Password changed")
        else:
            return apology("Passwords do not match", 403)
    else:
        return render_template("profile.html")







