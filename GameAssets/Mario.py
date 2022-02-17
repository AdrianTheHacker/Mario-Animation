from GameAssets.GameObject import GameObject


class Mario(GameObject):
    """
    Init Method

    everything from GameObject.init() except:
        1. Direction Variable added
        2. Width and Height are set to GameSetup.tileSize
        3. Colour set to Red
    """

    """
    Move Method
    
    changes the x position to move Mario across the screen
    """

    """
    Update Method
    
    everything from GameObject.init() except:
        1. Also runs Move() method
    """