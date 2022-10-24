# Write the function box_surface_area(w,d,h)
# which returns the square feet of wood needed to build a box of width w, depth d, and height h
# using the formula area = 2wd + 2dh + 2wh corresponding to the areas of the top/bottom, left/right, and front/back sides
# respectively. Don't forget the docstring

def box_surface_area(w,d,h):
    '''Returns the square feet of wood needed to build a box of width w, depth d, and height h 
    using the formula area = 2wd + 2dh + 2wh corresponding to the areas of the top/bottom, 
    left/right, and front/back sides
    respectively.'''
    surface_area= (2*w*d)+(2*d*h)+(2*w*h)
    return surface_area


