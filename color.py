import random
import time
import matplotlib.pyplot as plt
import numpy as np

class color:
    '''
    You can choose bright or dark color. Moreover, you can pick color randomly.
    '''
    def __init__(self, number_color, random_seed=None, color_list=None) :

        self.number_color = number_color

        self.random_seed = random_seed

        if color_list : 
            self.color_list = color_list 
        else : self.color_list = ['#0FC2C0', '#0CABA8', '#008F8C', '#015958', '#023535', # Green: from bright to dark
                                  '#0087CC', '#007FBF', '#006EA6', '#00547F', '#002A40', # Blue: from bright to dark
                                  '#FF5C4F', '#FF4237', '#FF241C', '#A90F0A', '#8B0200', # Red: from bright to dark
                                  '#A8E6CF', '#DCEDC1', '#FFD3B6', '#FFAAA5', '#FF8B94', # Rainbow: from light blue to light red
                                  '#FAACC4', '#F2CED8', '#D9B4BE', '#8C2641', '#732634', # LoveHeart: from light pink to dark pink
                                  '#F2F2F2', '#D7D7D9', '#A19FA6', '#3C3840', '#89728C', # FrenchVintage: from light white to light purple
                                  '#A68F97', '#79717A', '#4B4952', '#1F2024', '#004F4D', # Gremlins: drak colors
                                  '#FAFCFB', '#F9D4C1', '#C0614B', '#733250', '#402129', # Luxury: from white to dark purple
                                  '#EDFFC7', '#99D68F', '#C2F5A6', '#1E3B05', '#517D08', # FernandoVerde: from bright green to dark green
                                  '#F8F7FF', '#836EFF', '#2C15B0', '#2A1F69', '#1B1733', # Website: from white to dark blue and purple
                                  '#DCDCDC', '#A0A0A0', '#646464', '#323232', '#101010', # Shades: from white to black
                                  '#F2E3D5', '#D0B4A7', '#8B6C59', '#A16564', '#623637', # StrongWing: from blown to dark blown
                                  '#ECFFCB', '#FCCCA4', '#FF6A53', '#DD1805', '#B11000', # Autum: from light yellow to dark red
                                  '#D9AD5B', '#A66F2D', '#593202', '#011526', '#0D0D0D', # Luxury1: from light blown to black
                                  '#F2E9BB', '#F19C28', '#EE8228', '#DB5B1C', '#EC5B26', # OrangeBox: from light to dark orange
                                  '#F2C641', '#F2BB16', '#F2A007', '#F28705', '#594011'] # Yellow: from bright to dark
            
    def select_seed(self) :

        self.random_seed = int(time.time())

        return self.random_seed 

    def random_select_color(self) :

        if not self.random_seed :
            self.random_seed = self.select_seed()

        random.seed(self.random_seed)

        selected_color = random.sample(self.color_list, self.number_color)

        return selected_color, self.random_seed
    
    def get_green(self) :
        return self.color_list[0:5]   
    def get_blue(self) :
        return self.color_list[5:10]
    def get_red(self) :
        return self.color_list[10:15]
    def get_orange(self) :
        return self.color_list[70:75]
    def get_yellow(self) :
        return self.color_list[75:80]
    def get_all_color(self) :
        return self.color_list
    def gradient_color(self, level) :
        # There are five levels about color: level 1 to level5(bright -> dark)
        if level == 1 :
            color = self.color_list[0::5]
        elif level == 2 :
            color = self.color_list[1::5]
        elif level == 3 :
            color = self.color_list[2::5]
        elif level == 4 :
            color = self.color_list[3::5]
        elif level == 5 :
            color = self.color_list[4::5]
        return color
    
    def show_color(self, show_color_list) :
        
        plt.figure(figsize=(12, 8))

        for i, color in enumerate(show_color_list):
            plt.bar(i, 1, color=color)

        plt.xticks(np.arange(len(show_color_list)))
        plt.yticks([])
        plt.title('Custom Color Palette')
        plt.show()

    

    
# Initialize the class by specifying the number of colors you want to generate. 
# The second parameter is the random seed. If the seed is not provided, a seed will be automatically generated and can be retrieved after the code runs. 
c = color(3, 17) 
random_color, random_seed = c.random_select_color() # Get random colors and seed
level_color = c.gradient_color(1) # Find bright or dark color by level (1-5, bright -> drak)
all_color = c.get_all_color()
print(random_color, random_seed)
print(c.show_color(all_color)) # Show color


