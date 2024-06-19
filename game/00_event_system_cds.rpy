

python early:
    def parse_check(lexer):
        subblock_lexer = lexer.subblock_lexer()
        check_bools = []

        while subblock_lexer.advance():
            with subblock_lexer.catch_error():
                statement = subblock_lexer.rest()
                check_bools.append(statement)

        return check_bools

    def return_if_check_fail(check_bools):
        if not all([eval(elem) for elem in check_bools]):
            renpy.return_statement()

    renpy.register_statement(
        name="check",
        block=True,
        parse=parse_check,
        execute=return_if_check_fail,
    )

init python:
    events = [label for label in renpy.get_all_labels() if label.startswith('event_')]

    def ev_check(*args,p=''):
        if args:
            parg = args[0]
        else:
            parg = p
        renpy.call('check_events',p=parg)


label check_events(p=''):
    $prefix = p
    $prefix_events = [ev for ev in events if ev.startswith('event_'+prefix)]
    $i = 0
    while i<len(prefix_events):
        $renpy.call(prefix_events[i])
        $i+=1
