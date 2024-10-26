class Socket {
    constructor(config) {
        this.config = config
        this.socket = io.connect(config.host)
        var currentRoom = null
    }

    init(roomName) {
        if (currentRoom != null) {
            this.leaveRoom(roomName)
            this.currentRoom == null
        }

        this.joinRoom(roomName)
    }

    joinRoom(roomName) {
        socket.on('connect', () => {
            socket.emit('joinroom', { room: roomName })
        })
        
        socket.on('message', (msg) => {
            console.log('Message:', msg)
        }) 
    }

    leaveRoom(roomName) {
        socket.emit('leaveRoom', { room: roomName })
    }
}





