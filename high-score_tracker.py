while True:
    score_input = input("Enter your game score: ").strip().lower()

    if score_input == "stop":
        print("Game session ended!")
        break

    score = int(score_input)

    if score > 100:
        print("Wow! That’s a new high score!")
    else:
        print("Good try, keep playing!")