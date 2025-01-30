def say_hello(name, num):

    i = 0
    while i < num:
         print(f"hello {name}!")
         i += 1

say_hello("Walter", 3)
say_hello("Helen", 2)
say_hello("Larry", 1)
say_hello("Ruth", 2)


if __name__ == "__main__":
    say_hello("world", 3);
