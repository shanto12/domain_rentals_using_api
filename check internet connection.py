import requests
import re


hardcoded_address='Tumbalong+Boulevard,+Haymarket+NSW+2000'
hardcoded_address="6 Loftus Street, Sydney NSW 2000"
r=requests.get(f"https://www.whistleout.com.au/Broadband/Search?data=-1&speed=200&tab=fixed&address={hardcoded_address}")
r_text=r.text

pattern = r'Ultrafast" data-count="(?P<count>\d*)"'

matches = re.findall(pattern, r_text)

ultrafast_count = list({x for x in matches})[0]

print(ultrafast_count)
print(matches)