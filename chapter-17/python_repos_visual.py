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
# list 'labels' will hold data about project description and owner
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
# Value associated with 'items' is a list containing dictionaries, each containing info about individual python repos

# Modifying x-axis labels to be clickable by pulling URL and using it while generating labels
# We can make a clickable link by using HTML within text elements
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    # use HTML anchor tag format to generate link:
    repo_link = f"<a href='{repo_url}'>{repo_name}<a/>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    # still in loop, creating label for each repo
    # Plotly allows us to use HTML within text elements, '<br/ >' is a line-break
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# Make Visualization
# We can include styling directions in 'data' and 'my_layout' as key/value pairs
# 'marker' represents 'bar' characteristics here

data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6
}]

# Instead of importing 'Layout' class, we use dictionary approach to define the data we will use (title,x-axis,y-axis)
# First 'titlefont' refers to chart title, 'titlefont' can also be defined for x and y axis titles:
my_layout = {
    'title': 'Most-Starred Python Repos on Github',
    'titlefont': {'size': 26},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 12},
        'tickfont': {'size': 10},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 12},
        'tickfont': {'size': 10},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos_visual.html')
