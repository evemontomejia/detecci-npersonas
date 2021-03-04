#codificacion del servidor
from flask import Flask, json, request, jsonify
from GUI_MySQL_class import MySQL

mysql = MySQL()
app = Flask(__name__)

@app.route("/")
def server_info():
    
    rvs=mysql.ConsultData()
    content = {} #estructura global objeto
    employee = [] #lista
    for rv  in rvs: #for para repetir (bucle) #rv es el elemtento de la consulta de la bd
        content = {'id':rv[0], 'alarma': [1]}
        employee.append(content)
        content ={}
    get_thing = {"get_alarma":employee}
       
    return jsonify(get_thing)

         

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True,
            threaded=True, use_reloader=False)

