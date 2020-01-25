# import requests
# import urllib
# import posixpath
# from urllib.parse import urlparse
# from datetime import datetime
# import pickle


class LibrariesIOConnector:
    def __init__(self, key):
        ### this import has to be here, because it will INSTANTLY search for LIBRARIES_API_KEY
        ### instead of beeing actualy coded properly
        ### there is no proper api for this stupid wrapper and so we do this here
        ### to check for access to the library
        from pybraries.search import Search
        search = Search()
        info = search.platforms()
        if not info:
            raise ConnectionError("Could not connect to LibrariesIO")

    # def getOwnerandProject(self, platform, name):
    #     url_path = posixpath.join('api', platform, name)
    #     url = urllib.parse.urljoin(self.base_url, url_path)
    #     r = requests.get(url, params=self.apiKey)
    #     if r.status_code is not 200 or r.json().get('repository_url') is None:
    #         print(platform + " " + name)
    #         print("Request not possible")
    #         print(r.status_code)
    #         return None
    #     else:
    #         try:
    #             repository_url = urlparse(r.json().get('repository_url'))
    #             owner = repository_url.path.split('/')[1]
    #             project_name = repository_url.path.split('/')[2]
    #             return {"owner": owner, "project_name": project_name}
    #         except:
    #             print("Repository URL is not valid")
    #             print(platform + " " + name)
    #             return None
    #
    # def getDependencyData(self, owner, name):
    #     name = name.replace(".git", "")
    #     url_path = posixpath.join('api', 'github', owner, name, 'dependencies')
    #     url = urllib.parse.urljoin(self.base_url, url_path)
    #     r = requests.get(url, params=self.apiKey)
    #     if r.status_code is not 200:
    #         print(owner + " " + name)
    #         print("Request not possible")
    #         print(r.status_code)
    #         return None
    #     else:
    #         return {"dependencies": r.json().get('dependencies'), "github_id": r.json().get('github_id')}
