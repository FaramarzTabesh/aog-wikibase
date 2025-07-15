import requests

wiki_api_url = "https://aogdata.wikibase.cloud/w/api.php"
params = {
    "action": "query",
    "meta": "siteinfo",
    "siprop": "languages",
    "format": "json"
}

response = requests.get(wiki_api_url, params=params)
data = response.json()

for lang in data["query"]["languages"]:
    print(f"Code: {lang['code']}, Name: {lang['*']}")