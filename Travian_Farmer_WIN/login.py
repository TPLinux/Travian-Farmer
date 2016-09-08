# By: https://twitter.com/@i127001
# coding: utf8
import sys
import os
import requests as rq
from bs4 import BeautifulSoup as BS

# config file dir to load login info
conf_path = os.getcwd() + '\conf'
# add this dir to sys path
sys.path.append(conf_path)

import conf_file as cf  # noqa


class Login(object):
    """Login class"""

    def __init__(self):
        self.alliance_exception = cf.alliance_exception.encode('utf8')
        self.players_exception = cf.players_exception.encode('utf8')
        self.max_player_pop = cf.max_player_pop
        self.max_village_pop = cf.max_village_pop
        self.server = cf.server
        self.t1 = cf.t1
        self.t2 = cf.t2
        self.t3 = cf.t3
        self.t4 = cf.t4
        self.t5 = cf.t5
        self.t6 = cf.t6
        self.t7 = cf.t7
        self.t8 = cf.t8
        self.t9 = cf.t9
        self.t10 = cf.t10
        self.t11 = "0"
        # login post info
        self.url = "http://" + cf.server + "/dorf1.php"
        self.username = cf.username
        self.password = cf.password
        # requsts Session
        self.sess = rq.session()
        # request header
        self.h = {
            "Host":cf.server,
            "User-Agent":"Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate",
            "Referer":"http://ts70.travian.com/",
            "Connection":"keep-alive",
        }
        # login form data
        self.login_data = {
            "name":cf.username,
            "password":cf.password,
            "lowRes":"1",
            "s1":"Login",
            "w":"840:460",
            "login":""
        }
        # time out of request
        self.timeout = 300

    # login method
    def login_to_server(self):
        with self.sess as sess:
            try:
                resp = sess.post(self.url, data=self.login_data, headers=self.h, verify=False, timeout=self.timeout)
                resp = resp.content
                bs = BS(resp, 'html.parser')
                pla_name = bs.findAll("div",{"class": "playerName"})[0].findAll("a", {"href": "spieler.php"})[0].string
                if(pla_name == cf.username):
                    return True
                else:
                    return False
            except:
                return False
