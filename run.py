import os
from flask import Flask, render_template


app = Flask(__name__,
            static_url_path='', 
            static_folder='/app',
            template_folder='/app')


@app.route('/')
def application():
    return render_template("index.html", ORG_NAME = os.getenv("ORG_NAME","") )

if __name__=="__main__":
    app.run(host='0.0.0.0', port=80)
