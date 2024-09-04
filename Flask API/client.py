import requests
res = requests.post('http://localhost:5000/sim', json={"title":"cdc currently report ninety-nine thousand and thirty-one death general discrepancy death count different source small explicable death toll stand roughly one hundred thousand people today", "content": "cdc currently report ninety-nine thousand and thirty-one death general discrepancy death count different source small explicable death toll stand roughly one hundred thousand people today"})
if res.ok:
    print(res.json())