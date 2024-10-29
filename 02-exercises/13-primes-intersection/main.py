"""
I nedenstående ser du 2 ting:
- 1) et 'import' statement af 'random' modulet
- 2) et 'set' bestående af alle primtal indtil 50.

Din opgave er at lave et nyt 'set' bestående af 10 tilfældigt genereret tal mellem 1 og 50
og så tjekke, hvorvidt nogen af disse 10 tal er primtal.

* HINT *
Når man skal generere et tilfældigt tal, kan man bruge 'random.randint(a, b)' funktionen,
der hvor 'a' er startværdi og 'b' er slutværdi.
"""

import random

primes_until_fifty = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}
