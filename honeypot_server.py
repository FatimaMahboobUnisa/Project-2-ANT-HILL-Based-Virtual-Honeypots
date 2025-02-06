from flask import Flask, request
import logging

app = Flask(__name__)
logging.basicConfig(filename='honeypot.log', level=logging.INFO)

@app.route('/')
def honeypot():
    attacker_ip = request.remote_addr
    logging.warning(f"Potential attacker detected: IP {attacker_ip}")
    return "Welcome to the dummy server!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
