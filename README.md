# Monitoring top 5 traders binance <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Binance_Logo.svg/2048px-Binance_Logo.svg.png"  width="20" height="20" />



### Language and module:


* Python <img src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/python/python-original.svg" width="15" height="15"/>
* Requests <img src="https://pypi.org/static/images/logo-small.2a411bc6.svg" width="15" height="15"/>


### Install requests:


```python
pip install requests
```

### Cod:
```python
from time import sleep
from conf import rank_profile

url = 'https://www.binance.com/bapi/futures/v3/public/future/leaderboard/getLeaderboardRank'

def main():
    while True:
        rank_profile()
        sleep(3600)

if __name__ == '__main__':
    main()
```

---

<div id="badges">

  <a href="https://t.me/jenya64">
    <img src="https://img.icons8.com/?size=512&id=63306&format=png"width="40" height="40"/>
  </a>

</div>
