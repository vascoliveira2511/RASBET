import sqlite3


class Bet:
    def __init__(self, id, state):
        self.id = id
        self.state = state

    def getId(self):
        return self.id

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def betToDB(self, userid, outcomeid):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO bets(outcome, user, state) VALUES (?, ?, ?)",
                  (userid, outcomeid, self.state))
        conn.commit()
        conn.close()

    def DBtoBet(self, id):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM bets WHERE id = ?", (id,))
        data = c.fetchone()
        self.id = data[0]
        self.state = data[3]
        conn.close()
