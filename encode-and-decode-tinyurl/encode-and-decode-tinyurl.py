class Codec:
    def __init__(self):
        self.lookup=[]

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        enc = len(self.lookup)
        self.lookup.append(longUrl)
        return "https://tinyurl.com/" + str(enc)
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        dec = int(shortUrl.split("/")[-1])
        return self.lookup[dec]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))