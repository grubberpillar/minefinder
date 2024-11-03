local D = {}

D.highscore = {}
D.custom_hs_list = {{{}}}

D.header = {"-TINY-", "-EASY-", "-NORMAL-", "-HARD-", "-INSANE-", "-CUSTOM-"}

D.description = {"pipsqueak mode", "OG minefinder size", "[fill this in]", "~get hard stay hard", "patience is ~~~~~~~~~~~~~~~", "~[max: 32x32]"}

D.mine_nums = {10, 14, 40, 99, 179, 40}
D.size_nums = {{8, 10, 16, 16, 24, 16}, {8, 10, 16, 30, 30, 16}}

D.diff = 3
D.diff_temp = nil

D.settings = {tutorial = true, profanity = false, scroll = true, scroll_slider = 3, sfx_slider = 4}

D.saved = false

D.snake = false
D.s_hs = 0

D.door_state = "closed"
D.key_is_there = true

return D