# IE6 error debugging notes

The solution to the LZ compress error was to replace, in line 127, the line from: 
```
context_c = uncompressed[ii]; 
```
to
```
context_c = uncompressed.charAt(ii);
```

apperently accessing a character that way doesn't work on IE6, and context_c became undefined
the way I semulated IE6 was with IE's competability mode.

my process of solving the problem was to place a breakpoint at the start of the func, and see if anything acts differently.
seeing that this action returned a different output for a different browser, I checked for other ways to get a char in a specifik location in JS, and used it.