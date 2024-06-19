

label main_menu:
    return

label start:
    'begin'
    $lvl = 1
    while True:
        'your level is [lvl]'
        call check_events
        'keep training'
        '....'
        'nice!'
        $lvl+=1
    return

label event_lvl_3:
    check:
        lvl == 3
        not 'lvl3_checked' in globals()
    'you passed level three!'
    $lvl3_checked = True
    return