print("hi hi welcome to funland!!")
print("ur mission: just chill n play lol")

first_choice = input("u at park gate... go 'left' 2 rides or 'right' 2 food?\n").strip().lower()

if first_choice == 'left':
    ride_choice = input("u see big roller coaster, spooky house n ferris wheel. pick 1: 'coaster', 'haunted', or 'ferris'\n").strip().lower()
    if ride_choice == 'coaster':
        print("AAAAA so fast!!! hair go brrrr lol")
    elif ride_choice == 'haunted':
        print("ghost say boo, u drop phone T-T")
    elif ride_choice == 'ferris':
        print("nice view!! u take 999 pics")
    else:
        print("u walk round round... waste all day lol rip fun")

elif first_choice == 'right':
    food_choice = input("smell yummy!! 'popcorn', 'cotton' or 'hotdog' ??\n").strip().lower()
    if food_choice == 'popcorn':
        print("crunch crunch yum yum")
    elif food_choice == 'cotton':
        print("fluffy sugar cloud, but sticky hand ew")
    elif food_choice == 'hotdog':
        print("nom nom hotdog, but u eat too fast n tummy say nooo")
    else:
        print("u think too long, shop close lol sad")

else:
    print("uhhh wrong way... now u in parking lot... game over lol")
