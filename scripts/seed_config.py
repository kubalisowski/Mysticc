# seed config here
class ConfigCommon():
    host = 'http://127.0.0.1:5000/'

    screen = {} 

    scroll_interval_ms = 25
    scroll_pixel = 10

    tile_width = 12
    tile_height = 12

    map_name = ""
    map_container_width  = 0
    map_container_height = 0

    dirs = { "UP": 0, "RIGHT": 1, "DOWN": 2, "LEFT": 3 }


class Config():
    config_common = ConfigCommon()        
    secret_key = "secret!"
    move_object_speed_sec = 0.1
    default_map_name = "rootville"
