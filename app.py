import pyodbc
from flask import Flask, request, jsonify


app = Flask(__name__)


conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:scoresheet.database.windows.net,1433;Database=score_sheet_db;Uid=scoresheetAdmin;Pwd=ss@27365410;Encrypt=yes;TrustServerCertificate=no;")
cursor = conn.cursor()

@app.route('/')
def hello():
    return "Hello Azure"

@app.route('/ip', methods=['GET'])
def getIP():

    if(request.method == 'GET'):

        try:
            query = 'SELECT D.DeviceId, D.Address FROM Devices D'
            cursor.execute(query)
            res = cursor.fetchone()
            data = {
                'DeviceId': res.DeviceId,
                'Address': res.Address,
            }

            return jsonify(data), 200

        except  Exception as err:
            print(err)
            return jsonify(), 500


if __name__ == '__main__':
    app.run()