import requests
from requests.auth import HTTPBasicAuth
import config
import os

class GithubScraper:
    def __init__(self, repo_url):
        self.repo_url = repo_url
        
        parts = repo_url.rstrip('/').split('/')
        self.owner = parts[-2]
        self.repo = parts[-1]
        
        self.coding_language = [
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
        
        self.extensions = [
            '.py', '.java', '.js', '.c', '.cpp', '.cs', '.rb', '.php', '.go', '.swift',
            '.kt', '.rs', '.html', '.css', '.ts', '.sh', '.pl', '.R', '.lua',
            '.dart', '.vb', '.asm'
        ]
        
        self.token = config.CODEGPT_PERSONAL_ACCESS_TOKEN
    
    def get_files(self, path=''):
        url = f'https://api.github.com/repos/{self.owner}/{self.repo}/contents/{path}'
        headers = {'Accept': 'application/vnd.github.v3+json'}
        auth = HTTPBasicAuth('username', self.token) if self.token else None
        response = requests.get(url, headers=headers, auth=auth)
        response.raise_for_status()
        contents = response.json()
        files = []
        
        for item in contents:
            if item['type'] == 'file':
                if self.extensions is None or item['path'].endswith(tuple(self.extensions)):
                    files.append(item['path'])
                    print('[!] retrieving', item['path'])
            elif item['type'] == 'dir':
                files.extend(self.get_files(item['path']))
                
        return files
    
    def download_files(self, save_dir):
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        
        files = self.get_files()
        base_url = f'https://api.github.com/repos/{self.owner}/{self.repo}/contents/'
        
        headers = {'Accept': 'application/vnd.github.v3.raw'}
        auth = HTTPBasicAuth('username', self.token) if self.token else None
        
        for file_path in files:
            file_url = base_url + file_path
            response = requests.get(file_url, headers=headers, auth=auth)
            response.raise_for_status()
            
            filename = os.path.basename(file_path)
            txt_filename = f'{os.path.splitext(filename)[0]}{os.path.splitext(filename)[1]}.txt'
            save_path = os.path.join(save_dir, txt_filename)
            
            print(f'[!] downloading {filename}')
            
            with open(save_path, 'w', encoding='utf-8') as write_file:
                write_file.write(response.text)