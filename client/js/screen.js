var map_container_width = screen.width * 1
var map_container_height = screen.height
// MAP CONTAINER //
$("#map_container").css("width", `${map_container_width}`) 
// UP //
up_scroll_width = map_container_width * 0.8
up_scroll_height = map_container_height * 0.11
$("#up_scroll").css("width", `${up_scroll_width}`) 
$("#up_scroll").css("height", `${up_scroll_height}`) 
$("#up_scroll").css("left", `${(map_container_width - up_scroll_width) / 2}`) 
// DOWN //
down_scroll_width = up_scroll_width
down_scroll_height = up_scroll_height
$("#down_scroll").css("width", `${down_scroll_width}`) 
$("#down_scroll").css("height", `${down_scroll_height}`) 
$("#down_scroll").css("left", `${(map_container_width - down_scroll_width) / 2}`) 
// RIGHT //
var right_scroll_width = map_container_width * 0.08
var right_scroll_height = map_container_height
$("#right_scroll").css("width", `${right_scroll_width}`)
// $("#right_scroll").css("height", `${right_scroll_height}`) 
$("#right_scroll").css("height", `${map_container_height}`) 
// LEFT //
var left_scroll_width = right_scroll_width
var left_scroll_height = map_container_height
$("#left_scroll").css("width", `${left_scroll_width}`)
$("#left_scroll").css("height", `${left_scroll_height}`) 
$("#left_scroll").css("top", `${(map_container_height - left_scroll_height) / 2}`)
// console.log((map_container_height - left_scroll_height) / 2)
console.log(map_container_height)