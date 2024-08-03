import requests
from bs4 import BeautifulSoup
import re

class GetLinks:
    def __init__(self,url:str=None):
        self.url = url
        self.valid_extension_list = [".tar.xz",".tar.gz",".tar.bz2",".zip"]
        self.link = None
        self.links_fetched = None
        self.urls_downloadable = None
        
    def set_link(self, link:str=None, override:bool=False):
        if not link: return None
        
        if self.link and not override: 
            print(f"link already set and override is {override}, keeping original link")
        else:
            print(f"Setting link: {link}")
            self.link = link
        return self
    
    def _prepare_(self):
        # send a GET request to the website
        if not self.url: raise ValueError("url is None")
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.links_fetched = soup.find_all('a')
        return self
    
    def set_valid_extension_list(self, valid_extension_list:list=None):
        if not valid_extension_list: return None
        self.valid_extension_list = valid_extension_list
        return self
    
    def _get_file_signature_(self, url:str=None)->str:
        if not url or not self.valid_extension_list:
            print("url or valid_extensions is None")
            return None
        if not self.valid_extension_list: raise ValueError("valid_extension_list is None\n use self.set_valid_extension_list()")
        
        for ext in self.valid_extension_list:
            if ext in url:
                _, *sig_list = url.split(ext)
                if sig_list and len(sig_list) == 1 and sig_list[0] != '': # make sure theres only 1 signature
                    return ''.join(sig_list)
                else:
                    return None
        return None

    def _remove_signature_from_url_(self, url_signature_pair:tuple=None)->tuple:
        if not url_signature_pair: return None
        url, signature = url_signature_pair
        if signature:
            return (url.replace(signature, ''), signature.strip('.'))
        return url_signature_pair

    def _get_file_url_(self, url:str=None)->list:
        if url is None: return None
        return url if any(ext in url for ext in self.valid_extension_list) else None

    def _clean_url_signature_(self, url:str=None, signature:str=None)->tuple:
        return (url,signature)

    def _get_url_valid_signature_(self, url_signature_pair:list=None)->tuple:
        if not url_signature_pair: return None
        return url_signature_pair if url_signature_pair[1] else None
    
    def get_urls_from_source(self,links:list=None)->list:
        return list(map(lambda link: link.get('href') , links))
    
    def get_file_urls(self,links:list=None)->list:
        return list(filter(lambda link: self._get_file_url_(link) , links))
    
    def get_url_signatures(self,links:list=None)->list:
        return list(map(lambda link: self._get_file_signature_(link), links))
    
    def get_url_joined(self, url_files:str=None, signatures:str=None):
        return list(zip(url_files, signatures))
    
    def get_urls_clean(self,urls_joined:list=None):
        return list(map(lambda x: self._remove_signature_from_url_(x), urls_joined))
    
    def get_urls_with_valid_signature(self,urls_clean:list=None):
        return list(filter(lambda x: self._get_url_valid_signature_(x), urls_clean))
    
    def join_strings(self,strings:list=None)->str:
        return ''.join(strings)
    
    def print(self, header:str=None,body_list:list=None):
        
        if not body_list: return None
        if header: print(header)
        if len(body_list)==0: print("No items in list")
        for b in body_list: 
            print(b)
    
    def run(self):
        # process 
        if self.links_fetched is None:
            self._prepare_()
        
        urls = self.get_urls_from_source(self.links_fetched)
        urls2 = list(map(lambda link: link.get('href') , self.links_fetched))
        assert(urls == urls2)
        
        urls_files = self.get_file_urls(urls)
        urls_files2 = list(filter(lambda link: self._get_file_url_(link) , urls))
        # self.print(urls_files)
        assert(urls_files == urls_files2)
        
        urls_sigs = self.get_url_signatures(urls_files)
        urls_sigs2 = list(map(lambda link: self._get_file_signature_(link), urls_files))
        assert(urls_sigs==urls_sigs2)
        
        urls_joined = self.get_url_joined(urls_files, urls_sigs)
        urls_joined2 = list(zip(urls_files, urls_sigs))
        assert(urls_joined == urls_joined2)
        # self.print(urls_joined)
        
        urls_clean = self.get_urls_clean(urls_joined)
        urls_clean2 = list(map(lambda x: self._remove_signature_from_url_(x), urls_joined))
        self.urls_downloadable = urls_clean
        assert(urls_clean==urls_clean2)
        # self.print(urls_clean)

        urls_valid_signatures = self.get_urls_with_valid_signature(urls_clean)
        urls_valid_signatures2 = list(filter(lambda x: self._get_url_valid_signature_(x), urls_clean))
        assert(urls_valid_signatures==urls_valid_signatures2)
        return self
    
    def _test_get_download_url(self):
        os = 'linux'
        arch = 'x86_64'
        url = self.get_download_url(url_list=None,os=os, architecture = arch, has_signature=True)
        assert(url is not None)
        self.print(url)
    
    def get_url_containing_string(self, url_list:list=None, string:str=None)->list:
        return list(filter(lambda x: string in x, url_list))
    
    def _split_url_info_(self, url:str=None)->list:
        if not url: return None
        return url.split('/')
    
    def _get_url_version_(self, url:str=None)->str:
        if not url: return None
        pattern_version = re.compile(r'^[0-9.]+$')
        parts = self._split_url_info_(url)
        if parts:
            for p in parts:
                a = p if p and pattern_version.match(p) else None 
                if a: return a
        return None
    
    def get_url_versions(self, url_list:list=None)->list:
        if not url_list: return None
        return list(map(lambda x: self._get_url_version_(x), url_list))

    def get_download_url(self,
                         url_list:list=None, 
                         os:str=None, 
                         architecture:str=None, 
                         has_signature:bool=True,
                         latest_version:bool=True)->list:
        
        print(f'Status: Looking for download url for {os} and {architecture}: ')
        urls_valid = []
        
        if not url_list:
            url_list = self.urls_downloadable
            print("Warning: url_list is None, using cached list")
        
        assert(url_list is not None) # dbg
        
        if has_signature: 
            url_list = self.get_urls_with_valid_signature(url_list)
        
        # self.print(url_list)
        assert(url_list is not None) # dbg
        if not url_list: raise ValueError("url_list is None")    

        for u in url_list:
            if u[0] and os in u[0] and architecture in u[0]:
               urls_valid.append(u)
        
        if urls_valid and len(urls_valid)>0:  
            print(f'Found ({len(urls_valid)}) downloadable files')
            if latest_version:
                print('NEED TO FIX THIS: breaks if we include the latest branch (unstable)')
            return urls_valid
        else: 
            self.print(header='\nNo downloadable files found', body_list=[])
            return None
    