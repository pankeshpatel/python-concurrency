### When to Use multiprocessing

- You have CPU-bound tasks
- You want to utilize multiple CPU cores

```python
# Process large images on multiple cores
from multiprocessing import Pool

with Pool(4) as pool:
    results = pool.map(process_image, image_files)
```