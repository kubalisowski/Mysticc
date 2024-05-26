//---> COMBINED WITH screen.css <---//

///// MAP CONTAINER 
$("#map_container").css("width", `${config.map_container_width}`) 
///// SCROLLS
$(".scroll_bar").css("position", 'fixed') 
$(".scroll_bar").css("z-index", `${10}`)
$(".scroll_bar_corner").css("position", 'fixed') 
$(".scroll_bar_corner").css("z-index", `${20}`)
// UP 
var up_scroll_width = config.map_container_width //config.map_container_width * 0.8
var up_scroll_height = config.map_container_height * 0.11
$("#up_scroll").css("width", `${up_scroll_width}`) 
$("#up_scroll").css("height", `${up_scroll_height}`) 
$("#up_scroll").css("top", `${0}`) 
$("#up_scroll").css("left", `${(config.map_container_width - up_scroll_width) / 2}`) 
// DOWN 
var down_scroll_width = up_scroll_width
var down_scroll_height = up_scroll_height
$("#down_scroll").css("width", `${down_scroll_width}`) 
$("#down_scroll").css("height", `${down_scroll_height}`) 
$("#down_scroll").css("bottom", `${0}`) 
$("#down_scroll").css("left", `${(config.map_container_width - down_scroll_width) / 2}`) 
// RIGHT 
var right_scroll_width = config.map_container_width * 0.08
var right_scroll_height = config.map_container_height
$("#right_scroll").css("width", `${right_scroll_width}`)
$("#right_scroll").css("height", `${config.map_container_height}`) 
$("#right_scroll").css("right", `${(screen.width - config.map_container_width)}`) 
// LEFT 
var left_scroll_width = right_scroll_width
var left_scroll_height = config.map_container_height
$("#left_scroll").css("width", `${left_scroll_width}`)
$("#left_scroll").css("height", `${left_scroll_height}`) 
$("#left_scroll").css("left", `${0}`) 
// UP-LEFT 
var up_left_width = left_scroll_width
var up_left_height = up_scroll_height
$("#up_left_scroll").css("width", `${up_left_width}`)
$("#up_left_scroll").css("height", `${up_left_height}`) 
$("#up_left_scroll").css("top", `${0}`)
$("#up_left_scroll").css("left", `${0}`)
// UP-RIGHT
var up_right_width = right_scroll_width
var up_right_height = up_scroll_height
$("#up_right_scroll").css("width", `${up_right_width}`)
$("#up_right_scroll").css("height", `${up_right_height}`) 
$("#up_right_scroll").css("top", `${0}`)
$("#up_right_scroll").css("right", `${(screen.width - config.map_container_width)}`)
// DOWN-RIGHT
var down_left_width = left_scroll_width
var down_left_height = down_scroll_height
$("#down_left_scroll").css("width", `${down_left_width}`)
$("#down_left_scroll").css("height", `${down_left_height}`) 
$("#down_left_scroll").css("bottom", `${0}`)
$("#down_left_scroll").css("left", `${(screen.width - config.map_container_width)}`)
// DOWN-RIGHT
var down_right_width = right_scroll_width
var down_right_height = down_scroll_height
$("#down_right_scroll").css("width", `${down_right_width}`)
$("#down_right_scroll").css("height", `${down_right_height}`) 
$("#down_right_scroll").css("bottom", `${0}`)
$("#down_right_scroll").css("right", `${(screen.width - config.map_container_width)}`)

///// DEBUG 
var debug = document.currentScript.getAttribute('debug')
if (debug == 'true') {
    $("#up_scroll").css("border-style", "solid") 
    $("#down_scroll").css("border-style", "solid") 
    $("#right_scroll").css("border-style", "solid") 
    $("#left_scroll").css("border-style", "solid") 

    $("#up_left_scroll").css("border-style", "solid") 
    $("#up_right_scroll").css("border-style", "solid") 
    $("#down_left_scroll").css("border-style", "solid") 
    $("#down_right_scroll").css("border-style", "solid") 
}