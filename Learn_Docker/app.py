from flask import Flask, request 

app = Flask(__name__)
# my name is rahul 

# www.google.com/mail
@app.route("/" , methods = ["GET"])  # www.google.com
def welcome():
    return " This is Home Page "

@app.route("/even_odd", methods=["GET"]) # www.google.com/main
def even_odd():
    num = request.args.get("num")
    num = int(num)
    if num % 2 == 0 :
        return f"{num} is Even"
    else :
        return f"{num} is Odd"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)

# laptop 1 - 20,000 Digital Ports 