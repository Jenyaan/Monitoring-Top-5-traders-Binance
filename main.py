from time import sleep
from conf import rank_profile

url = 'https://www.binance.com/bapi/futures/v3/public/future/leaderboard/getLeaderboardRank'

def main():
    while True:
        rank_profile()
        sleep(3600)

if __name__ == '__main__':
    main()


