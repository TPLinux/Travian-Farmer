# By: https://twitter.com/@i127001
# coding: utf8
import login
from bs4 import BeautifulSoup as BS
from time import sleep

class Searcher(login.Login):
    """Searcher Class"""
    def __init__(self):
        super(self.__class__, self).__init__()
        self.logged_in = self.login_to_server()

    def search_farms(self, p_from_page, p_pages_count,cap_x,cap_y):
        # start search from page
        from_page = p_from_page
        static_from = p_from_page
        # pages count
        pages_count = p_pages_count
        # starting search
        print("Searching ...")
        with self.sess as sess:  # noqa
            while(from_page <= pages_count + static_from - 1):
                # initializing page url
                page_url = "http://" + self.server + "/statistiken.php?id=2&idSub=0&page=" + str(from_page)  # noqa
                row = 0
                sleep(2)
                while(row <= 20):
                    # get current villages page
                    page_source = sess.get(page_url, headers=self.h, verify=False, timeout=self.timeout)
                    bs = BS(page_source.content, 'html.parser')
                    # initializing village info
                    village_table = bs.findAll('table', {"id": "villages", "class": "row_table_data"})[0]
                    vill_row = village_table.findAll("tr")[row]
                    # info
                    village_rank = vill_row.findAll("td", {"class": "ra "})[0].string.encode('utf8')  # noqa
                    village_name = vill_row.findAll("td", {"class": "vil "})[0].findAll("a")[0].string.encode('utf8')  # noqa
                    village_link = vill_row.findAll("td", {"class": "vil "})[0].findAll("a")[0]['href']
                    village_z = village_link[12:].encode('utf8')  # noqa
                    village_link = "http://" + self.server + "/" + village_link  # noqa
                    pla_name = vill_row.findAll("td", {"class": "pla "})[0].findAll("a")[0].string.encode('utf8')  # noqa
                    pla_link = vill_row.findAll("td", {"class": "pla "})[0].findAll("a")[0]['href']
                    pla_link = "http://" + self.server + "/" + pla_link  # noqa
                    village_pop = int(vill_row.findAll("td", {"class": "hab "})[0].string.encode('utf8'))  # noqa
                    x_y = vill_row.findAll("td", {"class": "coords "})[0].findAll("a")[0]['href']
                    x1 = int(x_y[x_y.index('x=') + 2:x_y.index('&')])
                    y1 = int(x_y[x_y.index('y=') + 2:])
                    # findig distance using co-ordinates
                    x = x1 - cap_x
                    y = y1 - cap_y
                    x = pow(x,2)
                    y = pow(y,2)
                    # distance as integer
                    distance = float(pow((x + y),0.5))  # noqa
                    # enter player profile
                    pla_profile = sess.get(pla_link, headers=self.h, verify=False, timeout=self.timeout).content
                    bs = BS(pla_profile, 'html.parser')
                    # intializing
                    pla_table = bs.findAll('table', {"id": "details"})[0]
                    # player_info
                    try:
                        # if player have alliance
                        pla_alliance = pla_table.findAll('tr')[2].findAll('td')[0].findAll('a')[0].string.encode('utf8')
                    except:
                        # if player haven't alliance
                        pla_alliance = pla_table.findAll('tr')[2].findAll('td')[0].string.encode('utf8')
                    pla_pop = int(pla_table.findAll('tr')[4].findAll('td')[0].string.encode('utf8'))
                    # check search exceptions
                    if(pla_pop <= self.max_player_pop and village_pop <= self.max_village_pop and (pla_alliance not in self.alliance_exception) and (pla_name not in self.players_exception)):
                        f = open('farms_' + self.server + '.txt', 'a')
                        f.write("%.1f'|,|'%s'|,|'%s'|,|'%d'|,|'%s'|,|'%s'|,|'%s'|,|'%s'|,|'%s'|,|'%s'|,|'%s'|,|'%s'|,|'%s'|,|'%s'|,|'%d'|,|'%d\n" % (distance, village_z, village_name, village_pop, self.t1, self.t2, self.t3, self.t4, self.t5, self.t6, self.t7, self.t8, self.t9, self.t10, x1, y1))
                        print("---Farm Added---")
                        print("Village Rank : %s" % village_rank)
                        print("Village Name : %s" % village_name)
                        print("Village Pop : %s" % village_pop)
                        print("Village Link : %s" % village_link)
                        print("Player Name : %s" % pla_name)
                        print("Player Pop : %s" % pla_pop)
                        print("Player Link : %s" % pla_link)
                        print("Alliance : %s" % pla_alliance)
                        print("Distance : %.1f" % distance)
                        print('--------------')
                        f.close()
                    sleep(2)
                    # increase row number
                    row = row + 1
                # increase page url
                from_page = from_page + 1
            print('\n\n-------------')
            print("Searching Finished")
            print('-------------\n\n')

s = Searcher()
if(s.logged_in is True):
    print("------")
    print("WoW, Logged IN!!")
    print("------")
    print("Search Setting:\n")
    print("Max Player Pop: %d" % s.max_player_pop)
    print("Max Village Pop: %d" % s.max_village_pop)
    print("Filter Players: %s" % s.players_exception)
    print("Filter Alliances: %s" % s.alliance_exception)
    print("\nTroops For Farms:")
    print("t1  : %s" % s.t1)
    print("t2  : %s" % s.t2)
    print("t3  : %s" % s.t3)
    print("t4  : %s" % s.t4)
    print("t5  : %s" % s.t5)
    print("t6  : %s" % s.t6)
    print("t7  : %s" % s.t7)
    print("t8  : %s" % s.t8)
    print("t9  : %s" % s.t9)
    print("t10 : %s" % s.t10)
    print("---------")
    print("You Can Change This Settings From: conf/conf_file.py ")
    print("---------")
    start_from_page = int(raw_input("Start Search From Page: "))
    pages_count = int(raw_input("Pages Count: "))
    print("\nCalculating Distanse From:")
    x = int(raw_input("X: "))
    y = int(raw_input("Y: "))
    s.search_farms(start_from_page,pages_count,x,y)
else:
    print("------")
    print("Unable To Login")
    print("------")
