INSERT_INTO_AUTH_TABLE = """INSERT INTO Authtable VALUES(?, ?, ?)"""

INSERT_INTO_ACCOUNT_TABLE = """INSERT INTO Account VALUES(?, ?, ?, ?, ?)"""

INSERT_TRANSACTION = """INSERT INTO TransactionTable VALUES (?, ?, ?, ?, ?)"""

DELETE_FROM_AUTH_TABLE = """DELETE FROM Authtable WHERE Unique_id = ?"""

DELETE_FROM_ACCOUNT_TABLE = """DELETE FROM Account WHERE Unique_id = ?"""

UPDATE_SECURITY_CODE_IN_AUTH = """UPDATE Authtable SET Security_code = ? WHERE Unique_id = ?"""

UPDATE_ADD_BALANCE = """UPDATE Account SET Balance = Balance + ? WHERE Unique_id = ?"""

UPDATE_REDUCE_BALANCE = """UPDATE Account SET Balance = Balance - ? WHERE Unique_id = ?"""

SEARCH_EXISTING_USER_IN_AUTH = """SELECT COUNT(*) FROM Authtable WHERE Unique_id = ?;"""

SEARCH_EXISTING_USER_IN_ACCOUNT = """SELECT COUNT(*) FROM Account WHERE Unique_id = ?;"""

SEARCH_EXISTING_TRANSACTION_ID = """SELECT COUNT(*) FROM Account WHERE Unique_id = ?;"""

SEARCH_USER_DETAILS_IN_AUTH ="""SELECT * FROM Authtable WHERE Unique_id = ? AND Security_code = ?"""

SEARCH_PASSWORD = """SELECT Security_code FROM Authtable WHERE Unique_id = ?"""

CHECK_ROLE = """SELECT * FROM Authtable WHERE Unique_id = ?"""

SEARCH_USER_DETAILS_IN_ACCOUNT = """SELECT * FROM Account WHERE Unique_id = ?"""

FETCH_BALANCE_IN_DETAILS = """SELECT Balance FROM Account WHERE Unique_id = ?"""

GET_RECENT_TRANSACTIONS = """SELECT Transaction_id, Account_Number, 
                            Transaction_type, Transaction_date_time, Amount 
                            FROM TransactionTable WHERE Account_Number = ? 
                            ORDER BY transaction_date_time DESC LIMIT 5"""
                            
                            