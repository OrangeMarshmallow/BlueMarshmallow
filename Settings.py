class DataBase(object):
    admins = [117764726, 449391308]
    moders = []
    privilege = admins + moders
    white = privilege
    black = []

    def update(self, db_admins=None, db_moders=None, db_privilege=None, db_white=None, db_black=None):
        if not db_admins is None:
            self.admins = db_admins
        if not db_moders is None:
            self.moders = db_moders
        if not db_privilege is None:
            self.privilege = db_privilege
        if not db_white is None:
            self.white = db_white
        if not db_black is None:
            self.black = db_black
        self.privilege = list(set(self.privilege))
        self.white = list(set(self.white))
        self.black = list(set(self.black))
        self.admins = list(set(self.admins))
        self.moders = list(set(self.moders))


class BotSettings(object):
    login = '79372776567'
    password = '35lodavni'

    prefixes = ['/', '!']
    czarID = 117764726
    mainID = 449391308
    ok = False
    while not ok:
        try:
            tmp_admins = eval(open('DB\\admins.txt', 'r').read())
            tmp_moders = eval(open('DB\\moders.txt', 'r').read())
            tmp_privilege = eval(open('DB\\privilege.txt', 'r').read())
            tmp_white = eval(open('DB\\white.txt', 'r').read())
            tmp_black = eval(open('DB\\black.txt', 'r').read())
            DataBase().update(db_admins=tmp_admins,
                              db_moders=tmp_moders,
                              db_privilege=tmp_privilege,
                              db_white=tmp_white,
                              db_black=tmp_black)
            ok = True
        except (ValueError, SyntaxError):
            tmp_admins = [449391308, 117764726]
            tmp_moders = [284605667]
            tmp_privilege = []
            tmp_white = []
            tmp_black = [422177159, 448676027]
            f = open('DB\\admins.txt', 'w')
            f.write(str(tmp_admins))
            f.close()
            f = open('DB\\moders.txt', 'w')
            f.write(str(tmp_moders))
            f.close()
            f = open('DB\\privilege.txt', 'w')
            f.write(str(tmp_privilege))
            f.close()
            f = open('DB\\white.txt', 'w')
            f.write(str(tmp_white))
            f.close()
            f = open('DB\\black.txt', 'w')
            f.write(str(tmp_black))
            f.close()

    title = 'Bot'
    photo = "eyJvaWQiOjIwMDAwMDAwMDMsInBob3RvIjp7InBob3RvIjoiNmEzYmRjMGQ1ZTp6Iiwic2l6ZXMiOltbInMiLD" \
            "g0NjMyMzg0MiwiZDI0OTYiLCJBTS12U2pFRHBIbyIsNzUsNjBdLFsibSIsODQ2MzIzODQyLCJkMjQ5NyIsIjF3" \
            "LUd2ODJLNXA4IiwxMzAsMTA0XSxbIngiLDg0NjMyMzg0MiwiZDI0OTgiLCJaaVFVeGQzWGJxQSIsNjA0LDQ4M1" \
            "0sWyJ5Iiw4NDYzMjM4NDIsImQyNDk5IiwiVnRwUkZSWUp1MWciLDgwNyw2NDZdLFsieiIsODQ2MzIzODQyLCJk" \
            "MjQ5YSIsInNFSktnNkJCX2x3IiwxMjgwLDEwMjRdLFsibyIsODQ2MzIzODQyLCJkMjQ5YiIsIlNoYXBMaVNqLX" \
            "Y0IiwxMzAsMTA0XSxbInAiLDg0NjMyMzg0MiwiZDI0OWMiLCJMeFl6RTlNLWJDQSIsMjAwLDE2MF0sWyJxIiw4" \
            "NDYzMjM4NDIsImQyNDlkIiwiWGJyNm52a0ladjQiLDMyMCwyNTZdLFsiciIsODQ2MzIzODQyLCJkMjQ5ZSIsIn" \
            "I1TlF1Sko1b0pJIiw1MTAsNDA4XV0sImxhdGl0dWRlIjowLCJsb25naXR1ZGUiOjAsImtpZCI6Ijc3ZGIxYTY0" \
            "OWI0MjVkMzdkMTAyYjQ1ZjE5ODEyODAwIn0sInNxdWFyZSI6MSwiZGF0YSI6WyJ7XCJwaG90b1wiOlwiYjllZm" \
            "UyMTk2YnhcIixcInNpemVzXCI6W1tcIm1heFwiLDg0NjMyMzg0MixcImQyNDlmXCIsXCJIYXl0WXpFTkI3Y1wi" \
            "LDEyODAsMTAyNF0sW1wib1wiLDg0NjMyMzg0MixcImQyNGEwXCIsXCJDX2Y4NUxRdlJ3MFwiLDEwMjQsMTAyNF" \
            "0sW1wiYlwiLDg0NjMyMzg0MixcImQyNGExXCIsXCJIc2dxd2l1X0JuNFwiLDQwMCw0MDBdLFtcImFcIiw4NDYz" \
            "MjM4NDIsXCJkMjRhMlwiLFwidHFYWW9aYnZQRzhcIiwyMDAsMjAwXSxbXCJkXCIsODQ2MzIzODQyLFwiZDI0YT" \
            "NcIixcIjdoSEhBNFRESlJNXCIsMTAwLDEwMF0sW1wiZVwiLDg0NjMyMzg0MixcImQyNGE0XCIsXCJpdnh1b1hk" \
            "Tmt4a1wiLDUwLDUwXSxbXCJjXCIsODQ2MzIzODQyLFwiZDI0YTJcIixcInRxWFlvWmJ2UEc4XCIsMjAwLDIwMF" \
            "1dfSIsIjEyOCwwLDEwMjQsMTAyNCwwLDAsMTAyNCJdLCJid2FjdCI6Im93bmVyX3Bob3RvIiwic2VydmVyIjo4" \
            "NDYzMjMsIm1pZCI6NDQ5MzkxMzA4LCJfc2lnIjoiYTU3YWYxMzIzYmU5ZjY1OGY0MTQ0NGVmZmRiZTk4ZmIifQ"

    chatID = 3
    chatCheck = 1
    chatPeer = 2000000000 + chatID
    sleep_time = 0.25
    ranges = 1

    lastID = 0
    globalID = 0
    listen = True

    name = '🐲≌CzarBot'
    version = '2.1'

    run = False
    plugins = []
    words = []
    vk_start = False

    main_start = False

    getting = False
    bot_online = True

    calc_result = None

    tasks = []
    aw = False

    start_now = False
    history_started = False

    symbol_id = 0
    pin_id = eval(open('DB\\pin.txt', 'r').read())

    debugging = eval(open('DB\\debug.txt', 'r').read())
    debug_mode = debugging['debug']

    logging = eval(open('DB\\logging.txt', 'r').read())
    log_text = logging['Text']
    log_console = logging['Console']
    log_all = logging['All']
