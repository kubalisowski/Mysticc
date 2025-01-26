class Socket {
    constructor(config) {
        this.config = config
        this.socket = io.connect(config.host)
        this.currentRoom = null
    }

    init(room_name) {
        if (currentRoom != null) {
            this.leaveRoom(room_name)
            this.currentRoom == null
        }

        this.joinRoom(room_name)
    }

    joinRoom(room_name) {
        socket.on('connect', () => {
            socket.emit('join_room', { room: room_name })
        })
    }

    leaveRoom(room_name) {
        socket.emit('leave_room', { room: room_name })
    }
}





