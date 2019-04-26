"""
Main module of the server file
"""

import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the yaml file to configure the endpoints
app.add_api("master.yaml")

# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = ("It's working!")
    return msg


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
