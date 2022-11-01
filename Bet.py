import sqlite3


class Bet:
    def __init__(self, id, amountBet, state):
        self.id = id
        self.amountBet = amountBet
        self.state = state

    def getId(self):
        return self.id

    def getState(self):
        return self.state

    def getAmountBet(self):
        return self.amountBet

    def setState(self, state):
        self.state = state

    def setAmountBet(self, amountBet):
        self.amountBet = amountBet

    def betToDB(self, userid, outcomeid):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO bets(outcome, user, amountBet, state) VALUES (?, ?, ?, ?)",
                  (userid, outcomeid, self.amount, self.state))
        conn.commit()
        conn.close()

    def DBtoBet(id):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM bets WHERE id = ?", (id,))
        bet = c.fetchone()
        conn.commit()
        conn.close()
        return Bet(bet[0], bet[3], bet[4])
