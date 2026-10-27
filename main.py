from pyscript import document, display

country = {
    "ph": "Philippines",
    "au": "Australia",
    "jp": "Japan",
    "fr": "France",
    "sg": "Singapore",
}

country["us"] = "United States"


def check_country(e):
    country_code = document.getElementById("countries").value.lower().strip()
    document.getElementById("output1").innerText = country.get(country_code, "Country code not found")


def show_country(e):
    document.getElementById("output1").innerText = f"The number of countries are {len(country)}"
    display("Is it in the dictionary?", country, target="output1")