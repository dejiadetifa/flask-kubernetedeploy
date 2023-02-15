from flask import Flask, render_template
import socket

# an instance of the Flask

app = Flask(__name__)

# get system ip and hostname
def fetch_info():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return str(hostname), str(ip)

    
@app.route("/")
@app.route("/home")
def home_page():
    return render_template("index.html")


@app.route("/info")
def get_info():
    hostname, ip = fetch_info()
    return render_template("index.html", hostname=hostname, ipaddress=ip)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)