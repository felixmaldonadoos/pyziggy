import requests
from bs4 import BeautifulSoup

# send a GET request to the website
url = 'https://ziglang.org/download/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
links = soup.find_all('a')

# Function to check for additional text after the valid extension
def get_file_signature(url:str=None, valid_extensions:list=[".tar.xz",".tar.gz",".tar.bz2",".zip"])->str:
    if not url or not valid_extensions:
        print("url or valid_extensions is None")
        return None
    
    for ext in valid_extensions:
        if ext in url:
            base_url, *sig_list = url.split(ext)
            if sig_list and len(sig_list) == 1 and sig_list[0] != '': # make sure theres only 1 signature
                return ''.join(sig_list)
            else:
                return None
    return None

def remove_signature_from_url(url_signature_pair:tuple=None)->tuple:
    if not url_signature_pair: return None
    url, signature = url_signature_pair
    if signature:
        return (url.replace(signature, ''), signature.strip('.'))
    return url_signature_pair

def get_file_url(url:str=None, valid_extensions:list=[".tar.xz",".tar.gz",".tar.bz2",".zip"])->list:
    if url is None:
        return None
    return url if any(ext in url for ext in valid_extensions) else None

def clean_url_signature(url:str=None, signature:str=None)->tuple:
    return (url,signature)

def get_url_valid_signature(url_signature_pair:list=None)->tuple:
    if not url_signature_pair: return None
    return url_signature_pair if url_signature_pair[1] else None

class GetLinks:
    def __init__(self,url:str=None):
        self.url = url
        self.valid_extension_list = [".tar.xz",".tar.gz",".tar.bz2",".zip"]
        self.links = None
    
    def set_links(self, links:str=None):
        if not links: return None
        self.links = links
        return self
    
    def prepare(self):
        # send a GET request to the website
        if not self.url: raise ValueError("url is None")
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.links = soup.find_all('a')
    
    def set_valid_extension_list(self, valid_extension_list:list=None):
        if not valid_extension_list: return None
        self.valid_extension_list = valid_extension_list
        return self
    
    # Function to check for additional text after the valid extension
    def get_file_signature(self, url:str=None)->str:
        if not url or not self.valid_extension_list:
            print("url or valid_extensions is None")
            return None
        if not self.valid_extension_list: raise ValueError("valid_extension_list is None\n use self.set_valid_extension_list()")
        
        for ext in self.valid_extensions:
            if ext in url:
                base_url, *sig_list = url.split(ext)
                if sig_list and len(sig_list) == 1 and sig_list[0] != '': # make sure theres only 1 signature
                    return ''.join(sig_list)
                else:
                    return None
        return None

    def remove_signature_from_url(self, url_signature_pair:tuple=None)->tuple:
        if not url_signature_pair: return None
        url, signature = url_signature_pair
        if signature:
            return (url.replace(signature, ''), signature.strip('.'))
        return url_signature_pair

    def get_file_url(self, url:str=None)->list:
        if url is None:
            return None
        return url if any(ext in url for ext in self.valid_extensions) else None

    def clean_url_signature(self, url:str=None, signature:str=None)->tuple:
        return (url,signature)

    def get_url_valid_signature(self, url_signature_pair:list=None)->tuple:
        if not url_signature_pair: return None
        return url_signature_pair if url_signature_pair[1] else None
    
# process 
urls = list(map(lambda link: link.get('href') , links))
urls_files = list(filter(lambda link: get_file_url(link) , urls))
urls_sigs = list(map(lambda link: get_file_signature(link), urls_files))
urls_joined = list(zip(urls_files, urls_sigs))
urls_clean = list(map(lambda x: remove_signature_from_url(x), urls_joined))
urls_with_signature = list(filter(lambda x: clean_url_signature(x), urls_clean))
urls_valid_signatures = list(filter(lambda x: get_url_valid_signature(x), urls_with_signature))

# todo: get values that match os and architecture

for url in urls_valid_signatures: 
    print(url)
