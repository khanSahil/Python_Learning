import pdb

x = [1,2,3]
y = 5
z = 9

sum_1 = y + z

pdb.set_trace()

sum_2 = y + x
"""
python3 python_debugger.py 
> /home/sahkhan/Python_Learning/python_debugger/python_debugger.py(4)<module>()
-> x = [1,2,3]
(Pdb) b 4
Breakpoint 1 at /home/sahkhan/Python_Learning/python_debugger/python_debugger.py:4
(Pdb) n
> /home/sahkhan/Python_Learning/python_debugger/python_debugger.py(5)<module>()
-> y = 5
(Pdb) 
> /home/sahkhan/Python_Learning/python_debugger/python_debugger.py(6)<module>()
-> z = 9
(Pdb) 
> /home/sahkhan/Python_Learning/python_debugger/python_debugger.py(8)<module>()
-> sum_1 = y + z
(Pdb) 
> /home/sahkhan/Python_Learning/python_debugger/python_debugger.py(12)<module>()
-> sum_2 = y + x
(Pdb) 
TypeError: unsupported operand type(s) for +: 'int' and 'list'
> /home/sahkhan/Python_Learning/python_debugger/python_debugger.py(12)<module>()
-> sum_2 = y + x
(Pdb) exit()
Traceback (most recent call last):
  File "/home/sahkhan/Python_Learning/python_debugger/python_debugger.py", line 12, in <module>
    
  File "/usr/lib/python3.10/bdb.py", line 96, in trace_dispatch
    return self.dispatch_exception(frame, arg)
  File "/usr/lib/python3.10/bdb.py", line 176, in dispatch_exception
    if self.quitting: raise BdbQuit
bdb.BdbQuit
"""