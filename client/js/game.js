var width = document.currentScript.getAttribute('width')
var height = document.currentScript.getAttribute('height')
var map_src = document.currentScript.getAttribute('map-src')

const canvas = document.querySelector('#map_canvas')
const c = canvas.getContext('2d')

canvas.width = width
canvas.height = height

c.fillStyle = 'white'
c.fillRect(0, 0, canvas.width, canvas.height)

const map = new Image()
map.src = map_src

map.onload = () => {
    c.drawImage(map, 0, 0)
}


