import requests


# define the key to retrieve
key = "x"

# send a GET request to the FastAPI endpoint
x_response = requests.get(f"http://localhost:8000/x/{key}")
x_dict = x_response.json()
x = x_dict["val"]

# create source data
data = [
    {"name": "source1", "plastic": 0, "glass": 0, "biowaste": 0},
    {"name": "source2", "plastic": 0, "glass": 0, "biowaste": 0}
]

# update source1 data according to "x"
data[0]["plastic"] = x // 10
data[0]["glass"] = x // 50
data[0]["biowaste"] = x // 50

# update source2 data according to "x"
data[1]["plastic"] = x // 50
data[1]["glass"] = x // 20
data[1]["biowaste"] = x // 50

# send a POST request to the FastAPI endpoint
response = requests.post("http://localhost:8000/source/", json=data)

# print the response from the server
print(response.json())
