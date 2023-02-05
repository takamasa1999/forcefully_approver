from screeninfo import get_monitors

current_display = get_monitors()[0]

global main_settings
main_settings = {
    "main_window_width":current_display.width,
    "main_window_height":current_display.height,
    "window_icon_dir":"img/window_icon.png"
}
main_settings["sub_window_width"] = main_settings["main_window_width"]//4
main_settings["sub_window_height"] = main_settings["main_window_height"]//4
main_settings["center_pos_for_sub_window_x"] = main_settings["main_window_width"]//2 - main_settings["sub_window_width"]//2
main_settings["center_pos_for_sub_window_y"] = main_settings["main_window_height"]//2 - main_settings["sub_window_height"]//2