class WorldObject {
    constructor (id, x, y, width, height, frameX, frameY, speed, moving, img_src, player=false) {
        this.id = id
        this.x = x
        this.y = y
        this.width = width
        this.height = height
        this.frameX = frameX
        this.frameY = frameY
        this.speed = speed
        this.moving = moving
        this.img_src = img_src
        this.player = player

        this.img_object
    }
}