def generate_random_str(length: int) -> str:
    import random
    a,r = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",""
    for i in range(length):r += random.choice(a)
    return r

def parse_url(url: str) -> str:
    u = url[:url.index("//")+2:] + url[url.index("//")+2:].split("/")[0]
    return u