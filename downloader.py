import subprocess
import os

class Downloader:
    def download_url(self, url, directory=None):
        print(f"Downloading {url}...")
        if directory is None:
            directory = os.getcwd()  # Set to CWD if no directory is specified
        
        result = subprocess.run(["wget", "-P", directory, url])
        
        if result.returncode == 0:
            return True
        else:
            return False
        
    def test(self):
        return self.download_url("https://ziglang.org/download/0.8.0/zig-linux-x86_64-0.8.0.tar.xz")
        
# if __name__=='__main__':
#     d = Downloader()
#     print(d.test())