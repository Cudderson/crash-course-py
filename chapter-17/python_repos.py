import requests

# Using Github's API to request info about python repos
# Generate visualization with Plotly, 'ranking' popularity of python repos


# Make an API call and store results
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# Define headers of API call. Github is on version 3 of their API, so we define headers that ask to use this version.
headers = {'Accept': 'application/vnd.github.v3+json'}

# Use requests to make call to API
# 'get()' returns a response object that we store in 'r'
r = requests.get(url, headers=headers)

# response object has attribute 'status code'. Status code = 200 is a successful response
print(f"Status code = {r.status_code}")

# Store API response in a variable
# API returns info in json format. We use '.json()' method to convert info to python dictionary
response_dict = r.json()

# Process results:
print(response_dict.keys())

# Access dictionary key 'total_count'
print(f"Total Python Repositories: {response_dict['total_count']}")

# Explore information about the repositories
repo_dicts = response_dict['items']
# Value associated with 'items' is a list containing dictionaries, each containing info about individual python repos

# 'len(repo_dicts)' represents the number of repos the API call returned
print(f"Repositories returned: {len(repo_dicts)}")


for repo_dict in repo_dicts:
    print("\nSelected information about each repository:")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")

# Print number of keys in individual dictionary for repo, to see how much info we can access
print(f"\nKeys: {len(repo_dicts[0].keys())}")

# print name of each key to console
for key in sorted(repo_dict.keys()):
    print(key)
