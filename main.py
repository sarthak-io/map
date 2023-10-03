from flask import Flask, request, jsonify
import folium 
import os

app = Flask(__name__)

@app.route('/map', methods=['GET'])
def get_map():
    
    city_name = request.args.get('city_name', 'Delhi')
    latitude = float(request.args.get('latitude', '28.6139'))
    longitude = float(request.args.get('longitude', '77.2090'))


    map = folium.Map(location=[latitude, longitude], zoom_start=10)

    # Add a marker for the city
    folium.Marker([latitude, longitude], tooltip=city_name).add_to(map)

 
    templates_folder = os.path.join(os.path.dirname(__file__), 'templates')


    map.save(os.path.join(templates_folder, 'map.html'))


    return jsonify({'message': 'Map created successfully'})

if __name__ == '__main__':
    app.run(debug=True)
