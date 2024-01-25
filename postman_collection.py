import requests
collection = {}

def make_postman_request(request):
    url = request['url']['raw']
    method = request['method']
    headers = {header['key']: header['value'] for header in request['header']}
    
    # Extracting query parameters from the URL
    query_params = {param.split('=')[0]: param.split('=')[1] for param in url.split('?')[1].split('&')}
    
    response = requests.request(method, url, headers=headers, params=query_params, verify=False)
    return response

# Make requests
for item in collection['item']:
    request = item['request']
    response = make_postman_request(request)
    
    print(f"Request Name: {item['name']}")
    print(f"Response Code: {response.status_code}")
    print(f"Response Text: {response.text}\n")
