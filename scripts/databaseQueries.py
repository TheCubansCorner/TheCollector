#! python3, sqlight3
#! databaseQueries -- Class of various database queries

import os, sys, sqlite3

from configparser import ConfigParser

class DatabaseQueries:
    def __init__(self) -> None:                                                     # -- Initiates the module.
        super().__init__()
        with sqlite3.connect("test.db") as self.database:
            self.curse: sqlite3.Cursor = self.database.cursor()
            self.createTables()

    def createTables(self) -> None:                                                 # -- Initiates Database Tables if they don't exist.
        # -- Users
        self.curse.execute("""
            CREATE TABLE IF NOT EXISTS users(   
            userID INTEGER PRIMARY KEY NOT NULL,
            username CHAR(50) NOT NULL,
            password CHAR(50) NOT NULL
            )""")
        
        # -- User Informaiton
        self.curse.execute("""
            CREATE TABLE IF NOT EXISTS userInformation(
            userID INTEGER,
            firstName CHAR(20) NOT NULL,
            lastName CHAR(20) NOT NULL,
            dob CHAR(8) NOT NULL,
            email CHAR(50) NOT NULL,
            profilePicture CHAR(100) NOT NULL
            )""")

        # -- Collection Lists
        # -- TODO list 
        # -- CSV file names       

    def fetchAllUsers(self) -> list:                                                # -- Returns a list of all the users
        userList: list = self.curse.execute("Select * FROM users").fetchall()
        return userList

    def fetchUserID(self, username: str, password: str) -> list:                    # -- Finds the ID for a user/password combo
        self.curse.execute(f"SELECT userID FROM users WHERE userName = ? and password = ?", (username, password))
        return self.curse.fetchall()
    
    def userExists(self, username: str, password: str) -> bool:                     # -- Checks if the user exists in the database
        userId = self.fetchUserID(username, password)

        if len(userId) > 0:
            return True
        else:
            return False

    def createUser(self, user: tuple) -> bool:                                      # -- Saves the users account to the database.
        if not self.userExists(user[0], user[1]):
            self.curse.execute("""
                INSERT INTO users (username, password) VALUES (?, ?)               
                """, tuple(user[:2]))
            
            self.database.commit()

            userID = int(self.fetchUserID(user[0], user[1])[0][0])
            userInformation = ((userID,) + tuple(user[2:]))
            self.curse.execute("""
                INSERT INTO userInformation (userID, firstName, lastName, dob, email, profilePicture)
                VALUES (?, ?, ?, ?, ?, ?)
                """, userInformation)
            
            self.database.commit()
            
            return True
        else:
            return False

    def fetchUser(self, userID: int) -> tuple:                                      # -- Fetches a users informaiton based on a user ID and returns a tuple
        self.curse.execute("SELECT * FROM users WHERE userID = ?", str(userID))
        userInformationOne = self.curse.fetchall()[0]
        self.curse.execute("SELECT * FROM userInformation WHERE userID = ?", str(userID))
        userInformationTwo = self.curse.fetchall()[0]
        
        return (userInformationOne + userInformationTwo[1:])

    def usernameExists(self, username: str) -> bool:                                # -- Returns a boolean value of whether the username exists
        user = self.database.execute("SELECT * FROM users WHERE username = ?", (username,))

        if len(user.fetchall()) > 0:
            return True
        else:
            return False

    def emailExists(self, email: str) -> bool:                                      # -- Checks if the email exists in the database
        confirmation: list = self.curse.execute("SELECT * FROM userInformation WHERE email = ?", (email,)).fetchall()

        if len(confirmation) > 0:
            return False
        
        return True

    def checkLogin(self, username: str, password: str) -> bool:
        user = self.database.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchall()
        self.errorMessage: str = ""

        if len(user) < 1:
            self.errorMessage = "There are no users with this username"   
            return False

        if user[0][2] == password:
            return True
        else:
            self.errorMessage = "Your password does not match the username"

        return False

if __name__ == "__main__":
    database: DatabaseQueries = DatabaseQueries()

    x = database.checkLogin("usernasdasdsaame", "password")
    