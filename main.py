from gofishgame import GoFishGame

def main():
    num_players = int(input("How many players are there? "))
    game = GoFishGame(num_players)
    game.play()


if __name__ == "__main__":
    main()
