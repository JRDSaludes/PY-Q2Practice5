from pyscript import document

def check_country(e):
    country = {
        "ph": "Philippines",
        "au": "Australia",
        "jp": "Japan",
        "fr": "France",
        "sg": "Singapore",
    }

    country_code = document.getElementById("countries").value.lower().strip()

    document.getElementById("output1").innerText = country.get(country_code, "Country code not found")

    #add a country
    country["us"] = "United States"

    document.getElementById("output2").innerText = country.get("us", "Country code not found")