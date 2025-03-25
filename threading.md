


### When to Use threading
- You have I/O tasks but your libraries are blocking (like standard requests, or open() for files)
- You are working with legacy libraries that don’t support async

```python
# Using requests, which is blocking
def download(url):
    response = requests.get(url)

threads = [threading.Thread(target=download, args=(url,)) for url in urls]
```

