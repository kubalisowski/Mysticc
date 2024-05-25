// MAP CONTAINER //
$("#map_container").css("width", `${config.map_container_width}`) 
// UP //
var up_scroll_width = config.map_container_width * 0.8
var up_scroll_height = config.map_container_height * 0.11
$("#up_scroll").css("width", `${up_scroll_width}`) 
$("#up_scroll").css("height", `${up_scroll_height}`) 
$("#up_scroll").css("left", `${(config.map_container_width - up_scroll_width) / 2}`) 
// DOWN //
var down_scroll_width = up_scroll_width
var down_scroll_height = up_scroll_height
$("#down_scroll").css("width", `${down_scroll_width}`) 
$("#down_scroll").css("height", `${down_scroll_height}`) 
$("#down_scroll").css("left", `${(config.map_container_width - down_scroll_width) / 2}`) 
// RIGHT //
var right_scroll_width = config.map_container_width * 0.08
var right_scroll_height = config.map_container_height
$("#right_scroll").css("width", `${right_scroll_width}`)
$("#right_scroll").css("height", `${config.map_container_height}`) 
$("#right_scroll").css("right", `${(screen.width - config.map_container_width)}`) 
// LEFT //
var left_scroll_width = right_scroll_width
var left_scroll_height = config.map_container_height
$("#left_scroll").css("width", `${left_scroll_width}`)
$("#left_scroll").css("height", `${left_scroll_height}`) 

// DEBUG //
var debug = document.currentScript.getAttribute('debug')
if (debug == 'true') {
    $("#up_scroll").css("border-style", "solid") 
    $("#down_scroll").css("border-style", "solid") 
    $("#right_scroll").css("border-style", "solid") 
    $("#left_scroll").css("border-style", "solid") 
}