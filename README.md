# Trash Can Emptying Microservice

This microservice takes the path of a trash can file, empties that file, and puts a 0 at the top to represent that its empty. Just send a request with the file path, and it’ll handle the task for you.

# Use

Sending a Request
You’ll make a POST request to /empty-trashcan, with a JSON payload that includes:

trashcanPath (string): The local file path of the trashcan file.

# Requesting Data from the Microservice

To programmatically request data from the Trashcan Emptying Microservice, you need to make an HTTP POST request to the /empty-trashcan endpoint with a JSON payload containing the file path (trashcanPath).

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

# Example Response Handling

This Python code sends a POST request to the Trashcan Emptying Microservice with the trashcan file path, then handles the response by printing a success message if the operation is successful, or an error message if there’s an issue, such as the file not existing or the first line not being 1.

    import requests
    import json
    
    #the URL of the microservice (adjust if necessary)
    url = "http://localhost:8080/empty-trashcan"
    
    #the data to send in the POST request
    data = {
        "trashcanPath": "/path/to/your/trashcan.txt"  # Replace with the actual file path
    }
    
    #send the POST request
    response = requests.post(url, json=data)
    
    #handle the response
    if response.status_code == 200:  # Check if the response is successful
        #parse the JSON response
        response_data = response.json()
    
        #check if the response contains a message (success)
        if "message" in response_data:
            print(f"Success: {response_data['message']}")
        #if there's an error message
        elif "error" in response_data:
            print(f"Error: {response_data['error']}")
    else:
        #if the server responds with a non-200 status code
        print(f"Request failed with status code {response.status_code}")
        print("Response content:", response.text)


# Example JSON Responses
Here’s what the responses from the server will look like:

If everything works (trashcan emptied):

    "message": "Trashcan emptied successfully. First line changed to '0'."

If the trashcan file path is incorrect:

    "error": "File '/path/to/your/trashcan.txt' does not exist. Please check the path and try again."

If the file format is incorrect (e.g., the first line isn’t '1'):

    "error": "The first line of the file is not '1' or the file is empty."

# Notes
File Path: trashcanPath points to a valid file on your system and that the first line of the file is 1 before sending the request.
Server Address: If the server addressisn't working adjust accordingly in the request URL.

![Sequence diagram](https://github.com/user-attachments/assets/b618820a-feb6-4b2d-9306-9c4d1b1bb89a)
