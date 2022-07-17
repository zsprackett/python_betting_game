from player import Player

def main():
    # load the player with a 100 dollar bank account
    player = Player(100)
    while(True):
        # keep playing until they quit or go bankrupt
        player.play_one_round()

if __name__ == "__main__":
    main()
