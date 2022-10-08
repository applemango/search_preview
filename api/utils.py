def parse_url(url: str) -> str:
    u = url[:url.index("//")+2:] + url[url.index("//")+2:].split("/")[0]
    return u