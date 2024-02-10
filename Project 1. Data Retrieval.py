#Main question:
#How does the average temperature of different regions, regarding latitude, vary from 1880-2022 with each other?
#1.  Has the average annual temperature of the tropical region, 24S-24N, varied more from 1880-2022
#    than the average annual temperature of the temperate regions, 24N-64N and 64S-24S?
#       -If not, by how much did the temperate regions vary more?
#       -If yes, by how much did the tropical region vary more?
#2.  Has the average annual temperature of the temperate regions, 24N-64N and 64S-24S, varied more from
#    1880-2022 than the average annual temperature of the polar regions 64N-90N and 90S-64S.
#       -If not, by how much did the arctic and antarctic regions vary more?
#       -If yes, by how much did the temperate regions vary more?
#3.  Has the average annual temperature of the polar regions, 64N-90N and 90S-64S, varied more from
#    1880-2022 than the average annual temperature of the tropical region, 24S-24N?
#       -If not, by how much did the tropical region vary more?
#       -If yes, by how much did the arctic and antarctic regions vary more?
#4.   Which region has the highest variance in average annual temperature from 1880-2022?
#Last:  What does the result tell us about how global warming affects different parts of the world?
#Note: by variace I mean the sum of all the differences between x year and x+1 year.

#For region_variance function, region is a positive integer from 0 to 14 corresponding to the colums in the zonnan_temps file
#The following values of region correspond to the following regions:
#5 = 24S-24N (tropical region)
#9 = 24N-44N (part of north temperate region)
#8 = 44N-64N (part of north temperate region)
#13 = 64S-44S (part of south temperate region)
#12 = 44S-24S (part of south temperate region)
#7 = 64N-90N (arctic region)
#14 = 90S-64S (antarctic region)


import math
def region_variance(region):
    import csv
    with open("zonann_temps.csv") as x:
        file = csv.reader(x)
        region_list = []
        #A list where all the values of the region are stored
        region_variance = 0
        #The desired answer
        x = 0
        #The first number in a subraction of two
        next(file)
        for row in file:
            region_list.append(row[region])
        for index in region_list:
            if x != len(region_list) - 1:
        #region_variance(3, -2, 1)
                region_variance += abs(float(region_list[x]) - float(region_list[x+1]))
                x += 1
        return region_variance

def temperate_region_variance():
    north_temperate_region_variance = region_variance(9) + region_variance(8)
    south_temperate_region_variance = region_variance(13) + region_variance(12) 
    temperate_region_variance = (north_temperate_region_variance + south_temperate_region_variance) / 2
    return math.trunc(temperate_region_variance)

def polar_region_variance():
    arctic_region_variance = region_variance(7)
    antarctic_region_variance = region_variance(14)
    polar_region_variance = (arctic_region_variance + antarctic_region_variance) / 2
    return math.trunc(polar_region_variance)

def tropical_region_variance():
    tropical_region_variance = region_variance(5)
    return math.trunc(tropical_region_variance)


def answering_question_1():
    TR = tropical_region_variance()
    TE = temperate_region_variance()
    print("Question 1:")
    print("Has the average annual temperature of the tropical region, 24S-24N, varied more from 1880-2022\
 than the average annual temperature of the temperate regions, 24N-64N and 64S-24S?")
    print("")
    if TR > TE:
        print("Yes, the average temperature of the tropical region has varied more from 1880-2022 than the temperate regions by\
", TR - TE, "degrees celsius")
    elif TR < TE:
        print("No, the average temperature of the temperate regions has varied more from 1880-2022 than the tropical region by\
",TE - TR, "degrees celsius")
    else:
        print("No, the average temperature of the tropical region has varied the same as the temperate regions from 1880-2022")
    print("")
    print("")

def answering_question_2():
    TE = temperate_region_variance()
    P = polar_region_variance()
    print("Question 2:")
    print("Has the average annual temperature of the temperate regions, 24N-64N and 64S-24S, varied more from\
 1880-2022 than the average annual temperature of the polar regions 64N-90N and 90S-64S.")
    print("")
    if TE > P:
        print("Yes, the average temperature of the temperate regions has varied more from 1880-2022 than the polar regions by\
", TE - P, "degrees celsius")
    elif TE < P:
        print("No, the average temperature of the polar regions has varied more from 1880-2022 than the temperate regions by\
", P - TE, "degrees celsius")
    else:
        print("No, the average temperature of the temperate regions has varied the same as the polar regions from 1880-2022")
    print("")
    print("")

def answering_question_3():
    TR = tropical_region_variance()
    P = polar_region_variance()
    print("Question 3:")
    print("Has the average annual temperature of the polar regions, 64N-90N and 90S-64S, varied more from\
 1880-2022 than the average annual temperature of the tropical region, 24S-24N?")
    print("")
    if P > TR:
        print("Yes, the average temperature of the polar regions has varied more from 1880-2022 than the tropical region by\
", P - TR, "degrees celsius")
    elif P < TR:
        print("No, the average temperature of the tropical region has varied more from 1880-2022 than the polar regions by\
", TR - P, "degrees celsius")
    else:
        print("No, the average temperature of the polar regions has varied the same as the tropical region from 1880-2022")
    print("")
    print("")

def answering_question_4():
    TR = tropical_region_variance()
    TE = temperate_region_variance()
    P = polar_region_variance()
    print("Question 4:")
    print("Which region has the highest variance in average annual temperature from 1880-2022?")
    print("")
    if TR > TE and TR > P:
        print("The tropical region has the highest variance in average annual temperature from 1880-2022\
 with a total variance of", TR, "degrees celsius")
    elif TE > TR and TE > P:
        print("The temperate regions have the highest variance in average annual temperature from 1880-2022\
 with a total variance of", TE, "degrees celsius")
    elif P > TR and P > TE:
        print("The polar regions have the highest variance in average annual temperature from 1880-2022\
 with a total variance of", P, "degrees celsius")
    else:
        print("Either two or three of the regions have the highest variance in average annual temperature from 1880-2022")
    print("")
    print("")

def answering_last_question():
    print("Answering the Last question:")
    print("What does the result tell us about how global warming affects different parts of the world?")
    print("")
    print("Given how the poles had the highest temperature variance from the data and how industries have emitted high levels\
 of CO2 since 1880 this fact could be evidence that demonstrates how climate change has affected the poles the most")
    print("")
    print("")

def project():
    answering_question_1()
    answering_question_2()
    answering_question_3()
    answering_question_4()
    answering_last_question()
project()
