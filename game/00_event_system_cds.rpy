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
    def check_events():
        for event_label in renpy.get_all_labels():
            if event_label.startswith('event_'):
                renpy.call(event_label)