import requests

# Search for a term
def search_wikipedia(term):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "opensearch",
        "search": term,
        "limit": 5,
        "format": "json"
    }
    response = requests.get(url, params=params)
    return response.json()

# Get the summary of a page
def get_page_summary(title):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "titles": title,
        "format": "json"
    }
    response = requests.get(url, params=params)
    data = response.json()
    pages = data['query']['pages']
    page = next(iter(pages.values()))  # Get the first page
    return page.get('extract')

# Example usage
search_results = search_wikipedia("Bola Tinubu")
print(search_results)

# summary = get_page_summary("Bola Tinubu")
# print(summary)
