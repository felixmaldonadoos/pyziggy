import subprocess
import os
import platform

class Downloader:
    def __init__(self) -> None:
        self.os_type = platform.system()
        print("OS type:", self.os_type)
        pass
    
    def _download_with_curl_(self,url:str=None, directory:str=None)->bool:
        print("Using curl...")

        # curl requires full filename if you want to save it to a specific directory
        filename = os.path.basename(url)
        if not self._verify_directory_(directory):
            print(f'Failed to create directory (curl)...{directory}')
            return False
        
        filepath = os.path.join(directory, filename)
     
        result = subprocess.run(["curl", "-L", "-o", filepath, url])
        
        if result.returncode == 0:
            print(f"Downloaded successfully to {directory}")
            return True
        else:
            print("Download failed")
            return False        
       
    def _download_with_winget_(self, url:str=None, directory:str=None):
        print("Using winget...")
        if not directory:
            directory = os.getcwd()  # Set to CWD if no directory is specified
        
        result = subprocess.run(["wget", "-P", directory, url])
        
        if result.returncode == 0:
            return True
        else:
            return False
        
    def _verify_directory_(self, directory:str=None)->bool:
        if not os.path.exists(directory):
            print(f'Creating directory {directory}...')
            os.mkdir(directory)
        return os.path.exists(directory)
        
    def download_url(self, url, directory=None)->bool:
        if not url: return False

        if not self._verify_directory_(directory): 
            print(f'Failed to validate directory...{directory}')
            return False
        print(f'Downloading "{url}" to "{directory}"...')
        if self.os_type == "Windows":
            return self._download_with_winget_(url, directory)
        elif self.os_type == "Linux":
            return self._download_with_curl_(url, directory)
        else:
            print("Unsupported OS :(")
            return False
    
    def test(self, directory=None):
        return self.download_url("https://ziglang.org/download/0.8.0/zig-linux-x86_64-0.8.0.tar.xz",directory)
    
if __name__=='__main__':
    d = Downloader()
    print(d.test(directory=os.path.join(os.getcwd())))