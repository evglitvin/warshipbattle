********************
##Game

###Description
Turn-based game 

###App Requirements:
1. UI:
`@lytvyn`
    - Local (OS dependent: PyQt, pygame)
    - Web (???)

1. API:
`@kushnir`
    - HTTP Requests
        - Accounts
        - Registration/login
        - Session
        - Swagger
    
1. Connection modes:
    - Single game
    - Multiplayer (local, over HTTP)

1. Observer system:
    - Each player can observe any game


###Game requirements:
1. Level system:
    `@daragan`
    - Every `map` consists of:
        > objects (warships, obstacles)
    - Objects behavior
    - Resources
    
    
1. Game logic:
    `@vovan`
    - Initializing game
        - Selecting level and opponent
    - Battle
    - Winning logic
        - winners and scores
  
1. Game states (state pattern):
    `@smushtyn`
    - Before battle
    - During the battle
    - After

##TBD