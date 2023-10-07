from flask import Flask
import dao

app = Flask(__name__)



@app.route('/', methods = ['GET'] )
def get_restaurants():
    return jsonify({"Hello": "World"})

if __name__ == "__main__":
    app.run(debug= True)