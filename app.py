from flask import Flask
#from modules.comparison_xml.resources import comparison_xml
#or you have to place the comparison_xml.py inside the folders: modules/comparison_xml/resources
import comparison_xml

app = Flask(__name__)
app.register_blueprint(comparison_xml, url_prefix="/xml")

@app.route('/')
def api():
    return {'data':'Api Running'}


app.run(debug=True)
