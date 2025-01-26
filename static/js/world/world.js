var socket = new Socket(config)
socket.init(config.map_name)

socket.on('message', (msg) => {
    console.log('Message: ', msg)
}) 

socket.on('move_objects', (data) => {
    console.log('move_objects: ', data)
}) 

class World {
    //.... func init()
}

