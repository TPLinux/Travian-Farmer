# By: https://twitter.com/@i127001
# coding: utf8
import login
from bs4 import BeautifulSoup as BS  # noqa
from time import sleep  # noqa

class Raider(login.Login):
    """Raider Class"""

    def __init__(self):
        super(self.__class__, self).__init__()
        self.logged_in = self.login_to_server()

    def raider(self):
        file = 'farms_' + self.server + ".txt"
        first_lst = []
        lst = []
        # read farms
        f = open(file, 'r')
        # assigment farms in the first_lst to sort them
        lines_ = f.readlines()
        # farms count
        self.farm_numbers = len(lines_)
        # remove \n
        for i in lines_:
            i = i[:i.index('\n')]
            i = i.split("'|,|'")
            first_lst.append(i)
        for n in first_lst:
            lst.append([float(n[0]), n[1], n[2], n[3], n[4], n[5], n[6], n[7], n[8], n[9], n[10], n[11], n[12], n[13], n[14], n[15]])
        # sort farms order by distance
        lst.sort()
        # distance = lst[x][0]
        # Z-ID     = lst[x][1]
        # Vil Name = lst[x][2]
        # vil Pop  = lst[x][3]
        # t1       = lst[x][4]
        # t2       = lst[x][5]
        # t3       = lst[x][6]
        # t4       = lst[x][7]
        # t5       = lst[x][8]
        # t6       = lst[x][9]
        # t7       = lst[x][10]
        # t8       = lst[x][11]
        # t9       = lst[x][12]
        # t10      = lst[x][13]
        # x        = lst[x][14]
        # y        = lst[x][15]
        with self.sess as sess: # noqa
            for farm in lst:
                first_url = "http://" + self.server + "/build.php?id=39&tt=2&z=" + farm[1]
                attack_url = "http://" + self.server + "/build.php?id=39&tt=2"
                first_source = sess.get(first_url, headers=self.h, verify=False, timeout=self.timeout).content
                bs = BS(first_source, 'html.parser')
                # parameters info
                timestamp = bs.findAll('input',{"name": 'timestamp'})[0]['value']
                timestamp_checksum = bs.findAll('input',{"name": 'timestamp_checksum'})[0]['value']
                b = bs.findAll('input',{"name": 'b'})[0]['value']
                current_did = bs.findAll('input',{"name": 'currentDid'})[0]['value']
                # initializing post data
                first_post_data = {  # noqa
                    "timestamp": timestamp,
                    "timestamp_checksum":timestamp_checksum,
                    "b":b,
                    "currentDid":current_did,
                    "t1":farm[4],
                    "t2":farm[5],
                    "t3":farm[6],
                    "t4":farm[7],
                    "t5":farm[8],
                    "t6":farm[9],
                    "t7":farm[10],
                    "t8":farm[11],
                    "t9":farm[12],
                    "t10":farm[13],
                    "dname":"",
                    "x":farm[14],
                    "y":farm[15],
                    "c":"4",
                    "s1":"ok"
                    }
                # send first request
                sleep(2)
                try:
                    second_source = sess.post(attack_url, data=first_post_data, headers=self.h, verify=False, timeout=self.timeout)
                    bs = BS(second_source.content, 'html.parser')
                    # second post data
                    a = bs.findAll('input', {"type": "hidden", "name": "a"})[0]['value']
                    kid = bs.findAll('input', {"type": "hidden", "name": "kid"})[0]['value']
                    # second post data
                    second_post_data = {
                        "redeployHero":"",
                        "timestamp":timestamp,
                        "timestamp_checksum":timestamp_checksum,
                        "id":"39",
                        "a":a,
                        "c":"4",
                        "kid":kid,
                        "t1":farm[4],
                        "t2":farm[5],
                        "t3":farm[6],
                        "t4":farm[7],
                        "t5":farm[8],
                        "t6":farm[9],
                        "t7":farm[10],
                        "t8":farm[11],
                        "t9":farm[12],
                        "t10":farm[13],
                        "t11":"0",
                        "sendReally":"0",
                        "troopsSent":"1",
                        "currentDid":current_did,
                        "b":"2",
                        "dname":"",
                        "x":farm[14],
                        "y":farm[15],
                        "s1":"ok"}
                    sleep(2)
                    final_source = sess.post(attack_url, data=second_post_data, headers=self.h, verify=False, timeout=self.timeout)
                    if("troop_details outRaid" in final_source.content):
                        print("Attack sent To (%s | %s), Village: %s" % (farm[14], farm[15], farm[2]))
                        print("Link : http://%s" % (self.server + "/karte.php?d=" + farm[1]))
                        print("Distance : %d" % farm[0])
                        print('------')
                except:
                    print('------')
                    print("Problem with Send Attack To (%s | %s), Village: %s" % (farm[14], farm[15], farm[2]))
                    print('------')
                    pass
            print('\n\n-------------')
            print("Raiding Finished")
            print('-------------\n\n')

r = Raider()
if(r.logged_in):
    print("------")
    print("WoW, Logged IN!!")
    print("------")
    print("Raiding ...")
    r.raider()
else:
    print("------")
    print("Unable To Login")
    print("------")
