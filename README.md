# CatColor
# Initialize the class by specifying the number of colors you want to generate. 
# The second parameter is the random seed. If the seed is not provided, a seed will be automatically generated and can be retrieved after the code runs. 
c = color(3, 17) 
random_color, random_seed = c.random_select_color() # Get random colors and seed
level_color = c.gradient_color(1) # Find bright or dark color by level (1-5, bright -> drak)
all_color = c.get_all_color()
print(random_color, random_seed)
print(c.show_color(all_color)) # Show color
