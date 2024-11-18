import requests
import json

def send_trashcan_request(trashcan_path):
    url = "http://localhost:8080/empty-trashcan"  #replace with your server's URL

    #prepare the payload
    payload = {
        "trashcanPath": trashcan_path
    }

    try:
        #send POST request
        response = requests.post(url, json=payload)
        response.raise_for_status()  #HTTPError for bad responses (4xx and 5xx)
        
        #parse response JSON
        data = response.json()
        if "message" in data:
            print("Success:", data["message"])
        elif "error" in data:
            print("Error:", data["error"])
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    trashcan_file_path = "trash_test.txt"  #update with the actual file path

    #call the function
    send_trashcan_request(trashcan_file_path)
