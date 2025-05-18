
from flask import Flask app Flask (__name_____)
@app.route('/')
def hello():
return "Hello from Docker!"
if __name_ == "____main___":
app.run(host='0.0.0.0', port=5000)