---
Reason for the error
---
Python executes the entire file c.py from top to bottom at the time of import. That includes any function definitions, class definitions, global variable declarations, and also statements like the print("TRY TO STOP THIS FROM BEING PRINTED IN FILE a.py WITHOUT DELETING THIS PRINT STATEMENT"). 
One of the ways to fix the error is to put the statement in if __name__ =='__main__': print(....). This statement will make sure that the print statement is only printed when c.py is run and not printed when a.py is run.
