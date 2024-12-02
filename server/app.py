from flask import Flask, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/node_geojson')
def get_node_geojson():
    # 读取 GeoJSON 文件
    return send_file('./SiouxFallsCoordinates.geojson', mimetype='application/geo+json')

@app.route('/link_geojson')
def get_link_geojson():
    # 读取 GeoJSON 文件
    return send_file('./links_with_exec_data1.geojson', mimetype='application/geo+json')

if __name__ == '__main__':
    app.run(debug=True)
