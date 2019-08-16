def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is a book on Hussein and good stuff"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
print("search started")
next(search)
print("Next method run")
search.send("Hussein")

search.close()
search.send("Hussein")
# input("press any key")
# search.send("Hussein and")
# input("press any key")
# search.send("thi si")
# input("press any key")
# search.send("joker")
# input("press any key")
# search.send("whats happening")


