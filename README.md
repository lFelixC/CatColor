# CatColor
## Color Class Usage

This documentation outlines how to use the Color class to generate and manipulate colors.

### Initialization

To start using the Color class, initialize it by specifying the desired number of colors to generate. The constructor accepts two parameters:

1. **Number of Colors**: The first parameter dictates how many colors you want to generate.
2. **Random Seed**: The second parameter is the random seed. Providing a seed ensures that the color generation is repeatable. If a seed is not provided, one will be automatically generated, and it can be retrieved after the code execution for repeatability purposes.

Example:
```python
c = Color(3, 17)
```

### Generating Random Colors

To generate random colors and retrieve the used or generated random seed, use the random_select_color method. This method returns a tuple containing the randomly selected colors and the random seed.

Example:
```
random_color, random_seed = c.random_select_color()
print(random_color, random_seed)
```

### Finding Bright or Dark Colors
The gradient_color method allows you to find either bright or dark colors based on a level you specify. Levels range from 1 to 5, where 1 corresponds to the brightest and 5 to the darkest.

Example:
```python
level_color = c.gradient_color(1)
```

### Retrieving All Generated Colors
You can retrieve all generated colors using the get_all_color method. This method returns a list of all colors currently managed by the Color class instance.

Example:
```python
all_color = c.get_all_color()
```

### Displaying Colors
To display the colors, use the show_color method. Pass the list of colors you wish to display to this method.

Example:
```python
print(c.show_color(all_color))
```


