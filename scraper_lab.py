import requests
from requests.auth import HTTPBasicAuth
import os
import config

def get_repo_files(owner, repo, path='', token=None, desired_extensions=None):
    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    auth = HTTPBasicAuth('username', token) if token else None
    response = requests.get(url, headers=headers, auth=auth)
    response.raise_for_status()
    contents = response.json()
    files = []
    for item in contents:
        if item['type'] == 'file':
            if desired_extensions is None or item['path'].endswith(tuple(desired_extensions)):
                files.append(item['path'])
        elif item['type'] == 'dir':
            files.extend(get_repo_files(owner, repo, item['path'], token, desired_extensions))
    return files

repo_url = 'https://github.com/AccessRetrieved/2_hand_motions'
parts = repo_url.rstrip('/').split('/')
owner = parts[-2]
repo = parts[-1]

coding_language_extensions = [
    ("Python", ".py"),
    ("Java", ".java"),
    ("JavaScript", ".js"),
    ("C", ".c"),
    ("C++", ".cpp"),
    ("C#", ".cs"),
    ("Ruby", ".rb"),
    ("PHP", ".php"),
    ("Go", ".go"),
    ("Swift", ".swift"),
    ("Kotlin", ".kt"),
    ("Rust", ".rs"),
    ("HTML", ".html"),
    ("CSS", ".css"),
    ("TypeScript", ".ts"),
    ("Shell Script", ".sh"),
    ("Perl", ".pl"),
    ("R", ".R"),
    ("Scala", ".scala"),
    ("Lua", ".lua"),
    ("Dart", ".dart"),
    ("Objective-C", ".m"),
    ("Elixir", ".ex"),
    ("Haskell", ".hs"),
    ("MATLAB", ".m"),
    ("Groovy", ".groovy"),
    ("Visual Basic", ".vb"),
    ("Assembly", ".asm"),
]


desired_extensions = [
    '.py', '.java', '.js', '.c', '.cpp', '.cs', '.rb', '.php', '.go', '.swift',
    '.kt', '.rs', '.html', '.css', '.ts', '.sh', '.pl', '.R', '.scala', '.lua',
    '.dart', '.m', '.ex', '.hs', '.m', '.groovy', '.vb', '.asm'
]

token = config.CODEGPT_PERSONAL_ACCESS_TOKEN

all_files = get_repo_files(owner, repo, token=token, desired_extensions=desired_extensions)
for file in all_files:
    print(file)