# import requests

# url = "http://127.0.0.1:8000/user-query"
# payload = {"query": "What are the symptoms of diabetes?"}
# headers = {"Content-Type": "application/json"}

# response = requests.post(url, json=payload, headers=headers)

# print(response.json())
# test.py
import requests

def test_query(query):
    url = "http://127.0.0.1:8000/user-query"
    payload = {"query": query}
    response = requests.post(url, json=payload)
    return response.json()

if __name__ == "__main__":
    # Test cases
    general_query = "What are the benefits of regular exercise?"
    healthcare_query = "What should I eat to improve my immune system?"
    programming_query = "Can you write a Python code to sort a list?"
    
    print("General Query:", test_query(general_query))
    print("Healthcare Query:", test_query(healthcare_query))
    print("Programming Query:", test_query(programming_query))
