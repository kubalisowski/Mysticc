CREATE TABLE `game_object` (
  `id` 		int(11)  	 NOT NULL AUTO_INCREMENT,
  `x` 		int(11)  	 DEFAULT NULL,
  `y` 		int(11)  	 DEFAULT NULL,
  `width`   int(11)  	 DEFAULT NULL,
  `height`  int(11)  	 DEFAULT NULL,
  `frameX`  int(11) 	 DEFAULT NULL,
  `frameY`  int(11) 	 DEFAULT NULL,
  `speed`   int(11) 	 DEFAULT NULL,
  `moving`  bit(1)	 	 DEFAULT NULL,
  `img_src` varchar(100) DEFAULT NULL,
  `player` 	bit(1)	 	 DEFAULT NULL,
  PRIMARY KEY (`id`)
) 

CREATE TABLE `map` (
  `id` 	   int(11) 		NOT NULL AUTO_INCREMENT,
  `name`   varchar(100) DEFAULT NULL,
  `width`  int(11) 		DEFAULT NULL,
  `height` int(11) 		DEFAULT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE map_object (
  `id` 	   		   int(11) NOT NULL AUTO_INCREMENT,
  `map_id` 		   int(11) NOT NULL,
  `game_object_id` int(11) NOT null,  
  PRIMARY KEY (`id`)
)