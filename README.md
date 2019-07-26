Pancake flipper take home test

In order to determine the smallest number of flips required for making sure that 
all pancakes in any stack are always facing up, any time there is a difference
in which way a pancake is facing (determined by instructions as +- or -+) then this
counts as a flip is required. This makes sure that all previous pancakes before the
change in direction are all now alligned. Finally, if the stack is all upside down,
which can be realized by the very last value of the stack being face down (-) there
will need to be one final flip.

After beginning script, any invalid entry or out of the range as specified in the
instrutions, the script will exit. If a case is given that does not contain expected
`+` or `-`, that specific use case will be skipped over. (Though about just exitting
but nothing pointed in the instructions so I just decided that made sense.)

Requires python3.6 because 2.7 needs to die and fStrings are my friend. (I recommend
latest but sometimes we can't have nice things in life.)

Execute Test:
    `python3 -m unittest`

    Tests check for valid format, lengths, and 

Excute actual script (assumes you have python3 correctly configured):
    `./pancake.py`
