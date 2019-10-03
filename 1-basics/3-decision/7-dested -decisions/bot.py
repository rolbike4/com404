print("What type of cover should the book have(hard or soft)")

book_cover = input()

if (book_cover == "soft"):
    print("Is the book perfect bound?")
    perfect_bound = input()

    if (perfect_bound == "Yes"):
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")

else:
    (book_cover == "hard")
    print("Books with hard covers can be more expensive!")