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

random_color, random_seed = c.random_select_color()
print(random_color, random_seed)

