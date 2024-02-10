from PIL import Image



#This function will take an image and an integer called num_of_columns as an input
#This function will split the image into the number of columns specified by num_of_columns and will copy the
#first column of pixels repeatedly into the other columns.
#Ex: If you give "The Rhythmic Boat" as image and integer 3 as num_of_columns, the function will make this image display
#the first third of itself repeated 3 times.
def divide_image_by_columns(image, num_of_columns):
    width, height = image.size
    for y in range(height):
        targetx = 0
        for x in range(width):
            if x < width//num_of_columns:
                r, g, b = image.getpixel((x,y))
                column_num = width//num_of_columns
                for column in range(2, num_of_columns + 1): 
                    image.putpixel((targetx + column_num, y), (r, g, b))
                    column_num += width//num_of_columns
            targetx += 1
    return image





#The function will take an image and four integers "startx, starty, endx, endy" as inputs. Each of these last four inputs
#represents the boundaries of the portion (in form of rectangle) of the image to be read.
#The function will output a 2D list of tuples, each tuple having information about each pixel in the portion of the image.
def read_m_by_n_pixels(image, startx, starty, endx, endy):
    width, height  = image.size
    list = []
    if -1 < startx <= width and -1 < starty <= height and -1 < endx <= width and -1 < endy <= height:
        for y in range(starty, endy):
            row = []
            for x in range(startx, endx):
                r, g, b = image.getpixel((x, y))
                row.append((r, g, b))
            list.append(row)
    return list


#The function will take a 2D list of tuples as an input, each tuple having information about the color of each pixel.
#The function will output a tuple having the average color of all the pixels provided by all tuples in the 2D list
#Ex: if you input [[(r1, g1, b1)],[(r2, g2, b2)]], the function will return ((r1 + r2)/2, (g1 + g2)/2, (b1 + b2)/2)
def average_color_of_pixels(list):
    r = 0
    g = 0
    b = 0
    count = 0
    tuple = (0, 0, 0)
    for row in list:
        for column in row:
            r += column[0]
            g += column[1]
            b += column[2]
            count += 1
    if count > 0:
        #print(list)
        tuple = (r//count, g//count, b//count)
    return tuple


# This function will take two images and four integers as inputs, startx, starty, endx, endy,
# where we do not include the pixels at endx nor endy.
# The function will use the two images to combine them together, and the four integers to determine which
# portion of image2 will be placed on which portion of image. Note: the coordinates of the rectangle copied from
# image2 will be pasted on the same coordinates of image1.
def rectangle_image2_on_image1(image, image2, startx, starty, endx, endy):
    width, height = image.size
    width2, height2 = image2.size
    # Check if rectangle could be placed in the first image.
    if endx > width or endy > height or startx > width or starty > height:
        return image

    # Check if the rectangle is in the second image.
    if endx > width2 or endy > height2 or startx > width2 or starty > height2:
        return image

    # Copy the second subimage onto the first image.
    for x in range(startx, endx):
        for y in range(starty, endy):
            r, g, b = image2.getpixel((x, y))
            image.putpixel((x, y), (r, g, b))
    return image



#This function will take an image and an integer called num_of_pixels_to_blurr as inputs.
#The function will make this image like its original state but with x by x spots having the same color.
#Ex: you input an image that contains 10 by 10 pixels with different colors, and an integer 5. This will
#make that 10 by 10 image that instead of having each pixel (1 x 1) with the same color, it will have
#each 5 x 5 pixels with the same color. Note: if the function is not evenly divisible by the integer, the
#function will blurr the last pixels (edge pixels) by calculating their average color.
def blurr_image(image, num_of_pixels_to_blurr):
    width, height = image.size
    for starty in range(0, height, num_of_pixels_to_blurr):
        # Get the y range of the subimage: (starty, endy)
        endy = starty + num_of_pixels_to_blurr
        # Edge case: near the height of the image.
        if endy > height:
            endy = height

        for startx in range(0, width, num_of_pixels_to_blurr):
            # Get the x range of the subimage: (startx, endx)
            endx = startx + num_of_pixels_to_blurr
            # Edge case: near the width of the image.
            if endx > width:
                endx = width

            # Get the subimage: (startx, starty) to (endx, endy)
            list = read_m_by_n_pixels(image, startx, starty, endx, endy)
            color = average_color_of_pixels(list)
            for y2 in range(starty, endy):
                for x2 in range(startx, endx):
                    image.putpixel((x2, y2), color)
    return image





#This function will take two images and an two integers called grid_size_width and grid_size_height as inputs.
#The function will output an altered version of image1 with image1 (in its original state) and image2 combined
#in a grid with the dimensions given by the two grid_sizes.
#Ex: you give "The Rhythmic Boat" as image1, "Summerfall" as image2, 3 as grid_size_width, and 4 as grid_size_height.
#This will make "The Rhythmic Boat" a 4 by 3 square image, half of the squares with parts of "The Rhythmic Boat"
#and the rest with parts of "The Seasons". The location of the square in the output image ("Rhythmic Boat") will influence
#what portion of image2 will be placed on the square. For example, if a square in the top right corner of the output image
#needs to have a portion of the "Summerfall" image, then the function will paste the top right corner of
#the "Summerfall" image on that square in the output image.
#If images are not the same size, then the pixels with coordinates that don't exist in both images will be cut off
#and only the function will alter image1 with the pixels that exist in both images.
def combine_to_images_in_grid(image1, image2, grid_size_width, grid_size_height):
    width1, height1 = image1.size
    width2, height2 = image2.size
    if width1 > width2:
        width1 = width2
    else:
        width2 = width1
    if height1 > height2:
        height1 = height2
    else:
        height2 = height1
    image1.resize((width1, height1))
    image2.resize((width2, height2))
    startx = 0
    starty = 0
    endx = width1//grid_size_width
    endy = height1//grid_size_height
    i = 0
    j = 0
    for y in range(0, height1, height1//grid_size_height):
        for x in range(0, width1, width1//grid_size_width):
            if i % 2 == 1:
                rectangle_image2_on_image1(image1, image2, startx, starty, endx, endy)
                i += 1
            else:
                i += 1
            startx += width1//grid_size_width
            endx += width1//grid_size_width
        j += 1
        i = j
        startx = 0
        endx = width1//grid_size_width
        starty += height1//grid_size_height
        endy += height1//grid_size_height
    return image1




#This function will take an image and an integer called "level" as inputs.
#The function will output the same image but brighter. It will do this by making each color in (red, green, blue) have
#the level integer added to it. If one of the colors + level is greater than 255, the color will only be set to 255.
def adjust_brightness(image, level):
    width, height = image.size
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x,y))
            image.putpixel((x,y), (r + level, g + level, b + level))
    return image


#This function will take three images as inputs, image1, image2, and image3. The function will first alter each image and
#then will output a new image. This new image will have those altered images combined together in a grid. The images will
#be altered in the following way: image1 will be blurred, image2 will be made darker, and image3 will be divided into columns.
#The function will then combine the three images so that the new image will have image3 occupying nearly half the space
#and images 2 and 3 with fourth of the space.
def project(image1, image2, image3):
    Image1 = blurr_image(image1, 10)
    Image2 = adjust_brightness(image2, -100)
    Image3 = divide_image_by_columns(image3, 4)
    x = combine_to_images_in_grid(Image1, Image2, 2, 2)
    New_Image = combine_to_images_in_grid(x, Image3, 4, 4)
    return New_Image



#This function calls the project function to create a new image and save it as "result.jpg" and display it.
#The main purpose of this function is to show a product of how all my functions would work together.
def main():
    y = Image.open("The Rhythmic Boat.jpg")
    The_Rhythmic_Boat = y.resize((530, 700))
    The_Rhythmic_Boat.show()


    x = Image.open("The Last Tree.jpg")
    The_Last_Tree = x.resize((530, 700))
    The_Last_Tree.show()


    z = Image.open("Summerfall.jpg")
    Summerfall = z.resize((530, 700))
    Summerfall.show()
    result = project(The_Rhythmic_Boat, Summerfall, The_Last_Tree)
    result.save("result.jpg")
    return result.show("result.jpg")

if __name__ == "__main__":
    main()
