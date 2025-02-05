local D = {}

D.in_game = false -- tracks if the splashscreen is finished
D.os = "mac"

D.highscore = {}
D.custom_hs_list = {{{}}}

D.header = {"-TINY-", "-EASY-", "-NORMAL-", "-HARD-", "-INSANE-", "-CUSTOM-"}

D.description = {"pipsqueak mode", "OG minefinder size", "classic", "~get hard stay hard", "patience is ~~~~~~~~~~~~~~~", "~[max: 32x32]"}

D.mine_nums = {10, 14, 40, 99, 169, 40}
D.size_nums = {{8, 10, 16, 16, 24, 16}, {8, 10, 16, 30, 30, 16}}

D.diff = 3
D.diff_temp = nil 

D.gui_anims = true

D.settings = {tutorial = true, profanity = false, autosave = true, dig_around = true, scroll = true, scroll_slider = 3, sfx_slider = 4, dig_key = true, graffiti = true, splashscreen = true, gamer_lights = false}
D.more_settings = false

D.saved = false
D.save_quit = false
D.auto_save = true

D.seconds = 0
D.minutes = 0
D.hours = 0

D.snake = false
D.s_hs = 0

D.door_state = "closed"
D.key_is_there = true

return D