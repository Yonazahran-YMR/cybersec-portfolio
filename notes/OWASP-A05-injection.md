# OWASP A05: Injection

Untrusted input gets interpreted as a command instead of just data. SQL injection is the classic case, user input gets concatenated directly into a query string instead of being treated as a parameter.

| Type | What it looks like |
|---|---|
| SQL injection | `' OR '1'='1` in a login field, bypasses auth entirely |
| Command injection | User input gets passed to a shell command |
| LDAP injection | Same idea, targets directory queries instead of SQL |
| Cross-Site Scripting (XSS) | Technically its own historical category, but injection of script into pages the browser then executes |

Core cause every time: untrusted input plus no separation between code and data.

Fix: parameterized queries (prepared statements), never string concatenation for building queries. Input validation is a second layer on top, not a replacement for it.

## Scenario I worked through

Java code building a query like this:

```java
String query = "SELECT * FROM logs WHERE source_ip = '" + userInput + "'";
```

This is vulnerable, the user input gets glued directly into the SQL string. The fix is JDBC's PreparedStatement, which separates the query structure from the data. The input gets bound as a parameter value instead of getting concatenated in, so even something like `' OR '1'='1` just gets treated as a literal string to search for, not as SQL syntax.

## Recap from the crypto review before this session

SSN that needs to be displayed back to the user later gets encrypted, not hashed. Not because encryption is "harder to crack," that's actually the hashing pitch. It's encryption specifically because the original value needs to come back. Hashing is one-way, there'd be no way to show the real SSN again if it were hashed.

The actual test for whether a field needs protection isn't "is it a log," it's whether the data is sensitive, and if so, what protection fits (encryption if the value needs retrieving later, hashing if it only ever needs verifying).

## Next up

A06 Insecure Design.
