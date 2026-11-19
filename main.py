from pyscript import document


instruments = {
    "thermometer": {
        "name": "Thermometer",
        "measures": "Air Temperature",
        "unit": "Degrees Celsius (°C)",
        "purpose": "Measures how hot or cold the air is.",
    },
    "barometer": {
        "name": "Barometer",
        "measures": "Atmospheric Pressure",
        "unit": "Hectopascals (hPa)",
        "purpose": "Measures air pressure to help monitor weather changes.",
    },
    "anemometer": {
        "name": "Anemometer",
        "measures": "Wind Speed",
        "unit": "Kilometers per hour (km/h)",
        "purpose": "Measures how fast the wind is blowing.",
    },
    "hygrometer": {
        "name": "Hygrometer",
        "measures": "Relative Humidity",
        "unit": "Percent (%)",
        "purpose": "Measures the amount of moisture in the air.",
    },
    "rain gauge": {
        "name": "Rain Gauge",
        "measures": "Rainfall",
        "unit": "Millimeters (mm)",
        "purpose": "Measures the amount of rainfall in an area.",
    },
    "wind vane": {
        "name": "Wind Vane",
        "measures": "Wind Direction",
        "unit": "Cardinal Directions",
        "purpose": "Identifies the direction from which the wind is blowing.",
    },
    "weather balloon": {
        "name": "Weather Balloon",
        "measures": "Atmospheric Conditions",
        "unit": "Varies",
        "purpose": "Collects atmospheric data at different altitudes.",
    },
    "pyranometer": {
        "name": "Pyranometer",
        "measures": "Solar Radiation",
        "unit": "Watts per square meter (W/m²)",
        "purpose": "Measures incoming solar radiation.",
    },
}

not_found = {
    "name": "Instrument Not Found",
    "measures": "N/A",
    "unit": "N/A",
    "purpose": "This instrument is not included in the dataset. Please try one of the eight listed instruments.",
}


def search_instrument(_event):
    user_input = document.querySelector("#instrument_name").value.strip().lower()
    output = document.querySelector("#output1")

    if not user_input:
        output.textContent = "Please enter a weather instrument name."
        return

    info = instruments.get(user_input, not_found)
    output.innerHTML = (
        "<h2>Instrument Information</h2>"
        f"<p><b>Weather Instrument:</b> {info['name']}</p>"
        f"<p><b>Measures:</b> {info['measures']}</p>"
        f"<p><b>Unit of Measurement:</b> {info['unit']}</p>"
        f"<p><b>Purpose:</b> {info['purpose']}</p>"
    )
    