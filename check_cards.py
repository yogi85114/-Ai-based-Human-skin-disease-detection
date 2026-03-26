import requests
import re
import time

r = requests.get(f'http://127.0.0.1:5000?t={time.time()}')
html = r.text

# Count disease-card divs
names = re.findall(r'disease-card-name">(.*?)</h3>', html)
print(f"Rendered {len(names)} disease cards:")
for i, name in enumerate(names, 1):
    print(f"  {i}. {name}")

# Check for hidden divs - maybe some cards render but are somehow filtered
all_cards = html.count('class="disease-card"')
print(f"\nTotal 'disease-card' class divs: {all_cards}")
