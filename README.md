# goodbye-python-repl
Repl switcher from python repl to Gauche (scheme) repl.

```
$>./gbpython
Python 3.8.2 (default, Jul  6 2020, 05:30:01)
[GCC 9.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 1 + 2
>>> b = [3,4,{"a":5,"b":6}]
>>> goodbye_repl()
gosh[r7rs.user]> a
3
gosh[r7rs.user]> b
(3 4 #<hash-table equal? 0xb6df5fc8>)
gosh[r7rs.user]> (cadr b)
4
gosh[r7rs.user]>
```
