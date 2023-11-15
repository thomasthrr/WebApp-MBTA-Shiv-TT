from flask import Flask, render_template, request
from mbta_helper import get_lat_long, get_nearest_station, get_temp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mbta_station', methods=['POST'])
def mbta_station():
    if request.method == 'POST':
        place_name = request.form['placeName']
        latitude, longitude = get_lat_long(place_name)
        station_name, wheelchair_accessible = get_nearest_station(latitude, longitude)
        temperature = get_temp(place_name)

        return render_template('mbta_station.html',
                               station_name=station_name,
                               wheelchair_accessible=wheelchair_accessible,
                               temperature=temperature)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)