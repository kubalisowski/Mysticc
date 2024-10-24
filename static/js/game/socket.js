var socket = io.connect(config.host)
socket.on('game_objects_update', function(data) {
    console.log(data);
});