class Game {
  constructor(config) {
    this.config = config

    const canvas = null
    const c      = null
    const map    = null

    const game_objects = [] 
    const keys = []

    const player = null

    let fps, fpsInterval, startTime, now, then, elapsed
  }

  init(map_object) {
    canvas = document.querySelector('#map_canvas')
    c      = canvas.getContext('2d')

    canvas.width  = map.width  * config.tile_width
    canvas.height = map.height * config.tile_height

    c.fillStyle = 'white'
    c.fillRect(0, 0, canvas.width, canvas.height)

    map     = new Image()
    map.src = map_object.img_src

    ///////////
    ///DEBUG///
    player = new GameObject ()
    player.id = 1
    player.x = 50
    player.y = 50
    player.width = 32
    player.height = 48
    player.frameX = 1
    player.frameY = 1
    player.speed = 10
    player.moving = false
    player.img_src = '../static/object/character/indianajones.png'
    let player_img = new Image()
    player_img.src = player.img_src
    player.img_object = player_img
    game_objects.push(player)
    ///////////
    ///////////

    startAnimating(10)

    window.addEventListener("keydown", function (e) {
      e.preventDefault()
      keys[e.key] = true
      game_objects[0].moving = true
    })
    window.addEventListener("keyup", function (e) {
        delete keys[e.key]
        game_objects[0].moving = false
    })
  }  
  
  drawObject(img, srcX, srcY, srcW, srcH, destX, destY, destW, destH) {
    c.drawImage(img, srcX, srcY, srcW, srcH, destX, destY, destW, destH)
  }

  startAnimating(fps) {
    fpsInterval = 1000/fps
    then = Date.now()
    startTime = then
    animate()
  }

  animate() {
    requestAnimationFrame(animate) 
    now = Date.now()
    elapsed = now - then
    if(elapsed > fpsInterval) {
      then = now - (elapsed % fpsInterval)
      c.clearRect(0, 0, c.width, c.height)
      c.drawImage(map, 0, 0)
      for (let i = 0; i < game_objects.length; i++) {
          let item = game_objects[i]    
          drawObject(item.img_object, item.width * item.frameX, item.height * item.frameY, item.width, item.height, item.x, item.y, item.width, item.height)
          moveByKey(game_objects[i])
      }
    }
  }

  moveByKey(obj) {
    if(keys['ArrowUp']) {
      moveObject(obj, 'up')
    }
    if(keys['ArrowDown']) {
      moveObject(obj, 'down')
    } 
    if(keys['ArrowLeft']) {
      moveObject(obj, 'left')
    }   
    if(keys['ArrowRight']) {
      moveObject(obj, 'right')
    }  
  }
  
  moveObject(obj, command) {
      switch(command) {
          case 'up':
              obj.y -= obj.speed
              obj.frameY = 3
              obj.moving = true
            break
          case 'down':
            obj.y += obj.speed
            obj.frameY = 0
            obj.moving = true
            break
          case 'left':
              obj.x -= obj.speed
              obj.frameY = 1
              obj.moving = true
            break
          case 'right':
              obj.x += obj.speed
              obj.frameY = 2
              obj.moving = true
            break
      }
      // handle object frame X
      if (obj.frameX < 3 && obj.moving) obj.frameX++
      else  obj.frameX = 0
  }  
}

