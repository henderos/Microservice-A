# Trash Can Emptying Microservice

This microservice takes the path of a trash can file, empties that file, and puts a 0 at the top to represent that its empty. Just send a request with the file path, and it’ll handle the task for you.

# Use

Sending a Request
You’ll make a POST request to /empty-trashcan, with a JSON payload that includes:

trashcanPath (string): The local file path of the trashcan file.

# Example POST Request (Python Code)

Here’s an example of how you’d send a request from your program. It posts the trashcanPath in JSON format to get back a success or error response.

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

# Getting the Response

If successful, the server will respond with a success message indicating the trashcan was emptied and the first line was changed to 0.
If something went wrong (like the file doesn’t exist or there’s an issue with its format), you’ll receive a helpful error message.

# Example Response Handling (Python)

    import requests
    import json
    
    def send_trashcan_request(trashcan_path):
        url = "http://localhost:8080/empty-trashcan"  # Replace with your server's URL if needed
    
        # Prepare the payload
        payload = {
            "trashcanPath": trashcan_path
        }
    
        try:
            # Send POST request
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            
            # Parse the response JSON
            data = response.json()
            if "message" in data:
                print("Success:", data["message"])
            elif "error" in data:
                print("Error:", data["error"])
        except requests.exceptions.RequestException as e:
            print("An error occurred:", e)
    
    if __name__ == "__main__":
        # Specify the path to your trashcan file
        trashcan_file_path = "/path/to/your/trashcan.txt"  # Update with the actual file path
    
        # Call the function
        send_trashcan_request(trashcan_file_path)
        
# Example JSON Responses
Here’s what the responses from the server will look like:

If everything works (trashcan emptied):

    "message": "Trashcan emptied successfully. First line changed to '0'."

If the trashcan file path is incorrect:

    "error": "File '/path/to/your/trashcan.txt' does not exist. Please check the path and try again."

If the file format is incorrect (e.g., the first line isn’t '1'):

    "error": "The first line of the file is not '1' or the file is empty."

# Notes
File Path: Ensure that the trashcanPath points to a valid file on your system and that the first line of the file is 1 before sending the request.
Server Address: If the server address isn’t http://localhost:8080, adjust accordingly in the request URL.
