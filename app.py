from flask import Flask, render_template, request, session
from random import randrange

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route("/")
def index():
    if "money" not in session:
        session["money"] = 10000
    return render_template("index.html", money=session["money"])

@app.route("/game", methods=["GET", "POST"])
def game():
    if "money" not in session:
        session["money"] = 10000
    if request.method == "POST":
        bet = int(request.form["bet"])
        number = int(request.form["number"])
        winning_number = randrange(50)+1

        if bet < 0 & 1<= number <=50:
            winning_number = number
        
        if number == winning_number:
            session["money"] += bet
            message = "Congratulations, you won! Your new balance is: $" + str(session["money"]) + "(+" + str(bet) + ")"
        else:
            session["money"] -= bet
            message = "Sorry, you lost. Your new balance is: $" + str(session["money"])
        return render_template("game.html", message=message, money=session["money"])
    else:
        return render_template("game.html", money=session["money"])

@app.route("/store")
def store():
    if "money" not in session:
        session["money"] = 10000
    return render_template("store.html", money=session["money"])

@app.route("/buy_flag", methods=["POST"])
def buy_flag():
    if "money" not in session:
        session["money"] = 10000
    if session["money"] < 100000000:
        message = "Sorry, you don't have enough money to buy the flag."
    else:
        session["money"] -= 100000000
        flag = "KCTF{w0w_y0u_4r3_und3rst4nd1ng_m1nus_V4lu3!}"
        message = "Congratulations, you bought the flag!" + str(flag) + "\nYour new balance is: $" + str(session["money"])
    return render_template("store.html", message=message, money=session["money"])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8078)
