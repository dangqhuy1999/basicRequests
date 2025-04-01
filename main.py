import requests
import json

headers = {
    'x-api-key': ''
}

response = requests.get(URL, headers=headers)

print("Status Code:", response.status_code)
print("Status Code:", response.text)
# Chuyển response text thành JSON nếu có thể
try:
    response_json = response.json()  # Chuyển response thành dictionary
    formatted_json = json.dumps(response_json, indent=4, ensure_ascii=False)
    print("Response JSON:\n", formatted_json)
except json.JSONDecodeError:
    print("Response Text:", response.text)  # Nếu không phải JSON, in text bình thường
