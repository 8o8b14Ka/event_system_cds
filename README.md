little CDS tool to label game chapters as events with conditions to occur.
intended to eliminate huge complex if-trees on large projects

How to use:
Let's assume we have a piece of a script, 
which should happen under circumstance A and circumstance B. 
Then we write:

label event_piece1:
    check:
        is_circumstance_A
        is_circumstance_B
        True
        2+2 == 4  #boolean example

And then, at the place where the actions should occur, we write:

call check_events

Action checking supports additional prefixes, which will reduce the overall traversal
and the number of variables needed for checking.

call chack_events('eventPrefix')

will check all label event_eventPrefix_* labels