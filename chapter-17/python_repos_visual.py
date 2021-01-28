import requests

from plotly.graph_objs import Bar
from plotly import offline

# We won't import 'Layout' class here. We will use dictionary approach to define layout

# Using Github's API to request info about python repos
# Generate visualization with Plotly, 'ranking' popularity of python repos


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# Define headers of API call. Github is on version 3 of their API, so we define headers that ask to use this version.
headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url, headers=headers)

print(f"Status code = {r.status_code}")

# Proccess Results
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars = [], []

# Value associated with 'items' is a list containing dictionaries, each containing info about individual python repos

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Make Visualization
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
}]

# Instead of importing 'Layout' class, we use dictionary approach to define the data we will use (title,x-axis,y-axis)
my_layout = {
    'title': 'Most-Starred Python Repos on Github',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos_visual.html')
