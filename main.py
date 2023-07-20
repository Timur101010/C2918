import requests
# import pandas as pd

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'

res = requests.get(url)
res_dict = res.json()

repos = res_dict ["items"]
len(repos)

import requests 
import pandas as pd
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'
res = requests.get (url)
res_dict = res. json ( )
repos = res_dict[ 'items']
len (repos)
30

del res_dict['items']
res_dict
{'incomplete_results': True,'total count': 8046758}

repo_df = pd.DataFrame(repos)

repo_df = repo_df[['name', 'full_name', 'html_url', 'created_at', 'stargazers_count', 'watchers', 'forks', 'open_issues']]
repo_df['created_at'] = pd.to_datetime(repo_df['created_at'])
repo_df['created_year'] = repo_df['created_at'].dt.year
repo_df['years_on_github'] = 2022 - repo_df['created_at'].dt.year

repo_df = pd. DataFrame (repos)
repo_df = repo_df[['name', 'full _name', 'html _url', 'created at', 'stargazers_ count', 'watchers', 'forks', 'open_issues']]
repo_df['created_at'] = pd.to_datetime(repo_df['created_at'])
repo_df ['created _year'] = repo_df['created_at'].dt.year
repo_df['years _on_github'] = 2022 - repo_df['created_at'].dt.year
repo_df



# import requests
# import pandas as pd
#
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'
#
# res = requests.get(url)
# res_dict = res.json()
#
# repos = res_dict["items"]
# len(repos)
#
# repo_df = pd.DataFrame(repos)
#
# repo_df = repo_df[['name', 'full_name', 'html_url', 'created_at', 'stargazers_count', 'watchers', 'forks', 'open_issues']]
# repo_df['created_at'] = pd.to_datetime(repo_df['created_at'])
# repo_df['created_year'] = repo_df['created_at'].dt.year
# repo_df['years_on_github'] = 2022 - repo_df['created_at'].dt.year
#
# repo_df















