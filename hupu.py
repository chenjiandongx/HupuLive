
"""Hupu Live:
    Proudly presented by Hupu JRs.

Usage:
    hupu -l
    hupu -w <gameNumber>
    hupu -h | --help
    hupu -v | --version

Tips:
    Please hit Ctrl-C on the keyborad when you want to interrupt the game live.

Arguments:
    gameNumber     The key number contact to the specific game.

Options:
    -h --help        Show this help message and exit.
    -v --version     Show version.
    -l               Show game live list.
    -w               Select a game live to watch.

"""
import time
import re
from docopt import docopt
import requests
from bs4 import BeautifulSoup

class Hupu():

    __headers__ = {'X-Requested-With': 'XMLHttpRequest',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                                 '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

    def __init__(self, **kwargs):
        self._args = kwargs
        self._namelst = []
        self._hreflst = []
        self._headers = self.__headers__
        self.get_gamelist()

    def get_command(self):
        """ 处理命令行参数 """
        if self._args.get('-l'):
            if self._namelst:
                print("\n 比赛\t\t| 比赛场次\n", "-" * 25)
                for i, v in enumerate(self._namelst):
                    print(" {}\t| {}\n".format(v, i), "-" * 25)
            else:
                print(">>  暂无比赛直播")

        if self._args.get('-w'):
            try:
                self.live_game(self._hreflst[int(self._args.get('<gameNumber>'))])
            except Exception:
                print(">>  输入比赛场次有误")

    def get_gamelist(self):
        """ 获取直播场次列表 """
        url = "https://nba.hupu.com/games/playbyplay"
        try:
            response = requests.get(url, headers=self._headers, timeout=5).text
            game_href = BeautifulSoup(response, 'lxml').find_all('a', target="_self")

            for href in game_href:
                h = href['href']
                if "playbyplay" in h:

                    self._hreflst.append(h)
                    game = BeautifulSoup(requests.get(h).text, 'lxml').find('p', class_="bread-crumbs").text
                    self._namelst.append(str(game).strip().split()[2][:-4])     # 获取对阵双方
        except requests.exceptions.ConnectTimeout:
            print(">>  获取比赛场次失败,请检查您的网络连接情况")

    def live_game(self, url):
        """ 循环文字直播比赛 """
        currid = 2.0
        title = requests.get(url, headers=self._headers).text
        info = BeautifulSoup(title, 'lxml').find('tr', class_="title bg_a").find_all('td')
        print("\n\t{} \t {}\n".format(info[0].text, info[3].text))        # 获取比赛标题信息

        try:
            while True:
                r = requests.get(url, headers=self._headers, timeout=5).text
                table = BeautifulSoup(r, 'lxml').find('div', class_="table_list_live playbyplay_td table_overflow")

                # 比赛结束时序列是升序的，比赛中序列是降序的，匹配比赛是否结束然后选择排序方法
                if re.findall(r'team_num">(\S+)</div>', r):
                    trlst = reversed(table.find('table').find_all('tr'))
                else:
                    trlst = table.find('table').find_all('tr')
                for tr in trlst:
                    if currid <= float(tr['id']):
                        currid += 1
                        td = [t.text for t in table.find('tr', id=tr['id']).find_all('td')]

                        if len(td) == 4:
                            gtime, gteam, gevent, gscore = td
                            if len(gteam) < 5:      # 补全空格，使显示格式对齐，强迫症
                                gteam += int(5 - len(gteam)) * 2 * " "
                            print("\t{} \t {} \t {}\t{}\n".format(gtime, gscore, gteam[1:], gevent))
                        elif len(td) == 1:          # 显示如比赛暂停，第一节结束等非比分信息
                            print("", td[0], "\n")
                            if td[0] == "比赛结束":
                                return
                time.sleep(1)                       # 每隔一秒发起一次请求

        except requests.exceptions.ConnectTimeout:
            print(">>  网络连接失败，无法获得直播数据")
        except KeyboardInterrupt:
            print(">>  您已中断直播")


def cli():
    """ 入口方法 """
    args = docopt(__doc__, version='Hupu Live 1.1')
    Hupu(**args).get_command()


if __name__ == '__main__':
    cli()
