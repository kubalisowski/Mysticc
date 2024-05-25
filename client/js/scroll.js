// BINDING
$(".scroll_bar").mouseenter(function(){
  let direction = $(this).data('direction')
  moveMap(direction)
})

$(".scroll_bar").mouseleave(function(){
  stopMove()
})

// FUNCTIONS
const interval_arr = []
//
function moveMap(direction) {
  switch(direction) {
    case 'up':
      startMove(0, -config.scroll_pixel)
      break;
    case 'down':
      startMove(0, config.scroll_pixel)
      break;
    case 'right':
      startMove(config.scroll_pixel, 0)
      break;
    case 'left':
      startMove(-config.scroll_pixel, 0)
      break;    
  }
}

function startMove(x_axis, y_axis) {
  var interval_id = setInterval(
    function () { // https://stackoverflow.com/questions/457826/pass-parameters-in-setinterval-function
      moveScroll(x_axis, y_axis)
    },
    config.scroll_interval_ms
  )
  interval_arr.push(interval_id)
}

function moveScroll(x_axis, y_axis) {
  document.getElementById("map_container").scrollBy(x_axis, y_axis)
}

function stopMove() {
  interval_arr.forEach((item) => {
    clearInterval(item)
  })
}