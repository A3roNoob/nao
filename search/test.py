# -*- coding: utf-8 -*-

from Search import *

reload(sys)
sys.setdefaultencoding('utf8')

def main():
    s = Search()
    r = s.google_search('avion', num=1)
    s.toJsonFile(r)
    

if __name__ == '__main__':
    main()