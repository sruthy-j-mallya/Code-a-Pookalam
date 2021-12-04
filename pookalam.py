#stage1 not that good some circles over other in differenct collors

p1 = point(x=0,y=50)
p2 = point(x=-50,y=35)
p3 = point(x=-50,y=-35)
p4 = point(x=0,y=-50)
p5 = point(x=50,y=-35)
p6 = point(x=50,y=35)
hexagon = polygon([p1,p2,p3,p4,p5,p6],stroke_width=0,fill="#0a5c04")
colorful_disc = circle(r=8,fill="#a7db18",stroke_width=0) + circle(r=5,fill="#eb549d",stroke_width=0) + circle(r=3,fill="#54c3eb",stroke_width=0)
large_disc = colorful_disc | scale(2) | translate(y = 50) | repeat(4*4, rotate(30))
pookalam = hexagon + large_disc
show(pookalam)

#stage2 

colorful_disc = ellipse(w=8,h=25,fill="#a7db18",stroke_width=0) + ellipse(w=5,h=25,fill="#eb549d",stroke_width=0) + ellipse(w=3,h=25,fill="#54c3eb",stroke_width=0)
rotated_shape = colorful_disc | scale(3) |(repeat(16,rotate(30)))
flower = rotated_shape + circle(r=8,fill="#5c0436",stroke_width=0)
show(flower | scale(3))

#stage3
petal = ellipse(x=0,y=50,w=20,h=50,stroke_width=0,fill="#5c0436") + ellipse(x=0,y=40,w=10,h=30,stroke_width=0,fill="#dec509")
show(petal | scale(2) | translate(y=-50) | repeat(15,rotate(30)))

#stage4
petal = ellipse(x=0,y=50,w=20,h=50,stroke_width=0,fill="#5c0436") + ellipse(x=0,y=40,w=10,h=30,stroke_width=0,fill="#dec509")
flower = petal | scale(2) | translate(y=-50) | repeat(15,rotate(30))
stem = line(x1=0,y1=0,x2=-100,y2=60,stroke_width=5,stroke="#dec509")
show(flower+stem)

#stage5
petal1 = ellipse(x=0,y=50,w=20,h=50,stroke_width=0,fill="#5c0436")
petal2 = ellipse(x=0,y=40,w=10,h=30,stroke_width=0,fill="#dec509")
flower1 = petal1 | scale(2) | translate(y=-50) | repeat(15,rotate(30))
flower2 = petal2 | scale(2) | translate(y=-50) | repeat(15,rotate(30))
show(flower1+flower2)

#stage6 - star
def star(c):
    p1 = point(x=-100,y=-50)
    p2 = point(x=0,y=100)
    p3 = point(x=100,y=-50)
    triangle1 = polygon([p1,p2,p3],stroke_width=0,fill=c)
    triangle2 = triangle1 | scale(y=-1)
    return((triangle1 + triangle2) | scale(x=0.8) )
lightgreen = "#34eb89"
greenStar = star(lightgreen)
show(greenStar)

#stage7
def star1(c):
    p1 = point(x=-100,y=-50)
    p2 = point(x=0,y=100)
    p3 = point(x=100,y=-50)
    triangle1 = polygon([p1,p2,p3],stroke_width=0,fill=c)
    triangle2 = triangle1 | scale(y=-1)
    return((triangle1 + triangle2) | scale(x=0.8) )
def star2(c,s):
    p1 = point(x=-100,y=-50)
    p2 = point(x=0,y=100)
    p3 = point(x=100,y=-50)
    triangle1 = polygon([p1,p2,p3],stroke_width=2,stroke=s,fill=c)
    triangle2 = triangle1 | scale(y=-1)
    return((triangle1 + triangle2) | scale(x=0.8) )
skinColor = "#f5dbab"
orange = "#f5aa20"
brown = "#6e0707"
black = "#000000"
transparentColor = color(242, 196, 136,0.5)
borderStar = star2(transparentColor,brown)
withoutborder = star1(orange)
show(withoutborder,borderStar)


#stage8 - upright
def rhombus(c):
    p1 = point(x=-100,y=0)
    p2 = point(x=0,y=50)
    p3 = point(x=100,y=0)
    p4 = point(x=0,y=-50)
    return(polygon([p1,p2,p3,p4],stroke_width=0,fill=c))
def parallelogram(c):
    p1 = point(x=-50,y=100)
    p2 = point(x=-50,y=0)
    p3 = point(x=50,y=-50)
    p4 = point(x=50,y=50)
    return(polygon([p1,p2,p3,p4],stroke_width=0,fill=c))
black = color(0,0,0)
brown = color(173, 57, 10)
orange = color(219, 95, 7)
blue = color(8, 11, 84)
saffron = color(245, 152, 32)
outerRhombus = rhombus(black)
innerRhombus = rhombus(saffron) | scale(0.25)
top = outerRhombus + innerRhombus
outerParallelogram = parallelogram(brown) 
innerParallelogram = (parallelogram(blue) | scale(0.35) | translate(y=15) )
leftside = (outerParallelogram + innerParallelogram) | translate(x=-50,y=-100)
outerParallelogram = parallelogram(orange) 
innerParallelogram = (parallelogram(black) | scale(0.35) | translate(y=15) )
rightside = (outerParallelogram + innerParallelogram) | translate(x=-50,y=-100) | scale(x=-1)
cube = top + leftside + rightside
show(cube)

#stage9 - onside
def rhombus(c):
    p1 = point(x=0,y=-100)
    p2 = point(x=50,y=0)
    p3 = point(x=0,y=100)
    p4 = point(x=-50,y=0)
    return(polygon([p1,p2,p3,p4],stroke_width=0,fill=c))
def parallelogram(c):
    p1 = point(x=100,y=-50)
    p2 = point(x=0,y=-50)
    p3 = point(x=-50,y=50)
    p4 = point(x=50,y=50)
    return(polygon([p1,p2,p3,p4],stroke_width=0,fill=c))
black = color(0,0,0)
brown = color(173, 57, 10)
orange = color(219, 95, 7)
blue = color(8, 11, 84)
saffron = color(245, 152, 32)
outerRhombus = rhombus(black)
innerRhombus = rhombus(saffron) | scale(0.25)
top = outerRhombus + innerRhombus
outerParallelogram = parallelogram(brown) 
innerParallelogram = (parallelogram(blue) | scale(0.35) | translate(x=15) )
leftside = (outerParallelogram + innerParallelogram) | translate(x=50,y=50)
outerParallelogram = parallelogram(orange) 
innerParallelogram = (parallelogram(black) | scale(0.35) | translate(x=15) )
rightside = (outerParallelogram + innerParallelogram) | translate(x=50,y=50) | scale(y=-1)
cube = top + leftside + rightside
show(cube)

#stage10 
def rhombus(c):
    p1 = point(x=0,y=-100)
    p2 = point(x=50,y=0)
    p3 = point(x=0,y=100)
    p4 = point(x=-50,y=0)
    return(polygon([p1,p2,p3,p4],stroke_width=0,fill=c))
def parallelogram(c):
    p1 = point(x=100,y=-50)
    p2 = point(x=0,y=-50)
    p3 = point(x=-50,y=50)
    p4 = point(x=50,y=50)
    return(polygon([p1,p2,p3,p4],stroke_width=0,fill=c))
def star(c):
    p1 = point(x=-100,y=-50)
    p2 = point(x=0,y=100)
    p3 = point(x=100,y=-50)
    triangle1 = polygon([p1,p2,p3],stroke_width=0,fill=c)
    triangle2 = triangle1 | scale(y=-1)
    return((triangle1 + triangle2) | scale(x=0.8) )
def starWithStroke(c,s):
    p1 = point(x=-100,y=-50)
    p2 = point(x=0,y=100)
    p3 = point(x=100,y=-50)
    triangle1 = polygon([p1,p2,p3],stroke_width=2,stroke=s,fill=c)
    triangle2 = triangle1 | scale(y=-1)
    return((triangle1 + triangle2) | scale(x=0.8) )

black = color(0,0,0)
brown = color(173, 57, 10)
orange = color(219, 95, 7)
blue = color(8, 11, 84)
saffron = color(245, 152, 32)
outerRhombus = rhombus(black)
innerRhombus = rhombus(saffron) | scale(0.25)
top = outerRhombus + innerRhombus
outerParallelogram = parallelogram(brown) 
innerParallelogram = (parallelogram(blue) | scale(0.35) | translate(x=15) )
leftside = (outerParallelogram + innerParallelogram) | translate(x=50,y=50)
outerParallelogram = parallelogram(orange) 
innerParallelogram = (parallelogram(black) | scale(0.35) | translate(x=15) )
rightside = (outerParallelogram + innerParallelogram) | translate(x=50,y=50) | scale(y=-1)
cube = top + leftside + rightside
cubeSequence = cube | scale(0.25) | translate(x=-100) | repeat(6,rotate(60))
show(sequence)

#stage11
teal = color(3, 74, 49)
greenYellow = color(197, 219, 29)
sequence = circle(r=50,stroke=teal,stroke_width=5,x=0,y=30)
sequence = sequence + (circle(r=50,stroke=greenYellow,stroke_width=5,x=0,y=30) | rotate(10))
sequence = sequence | repeat(10,rotate(36))
flower = sequence | scale(0.4) | translate(y=100) | repeat(10,rotate(36))
background = circle(r=100,fill=color(240, 200, 24),stroke_width=45,stroke=color(232, 35, 124)) + flower

petal = ellipse(x=0,y=50,w=20,h=50,stroke_width=0,fill="#5c0436") + ellipse(x=0,y=40,w=10,h=30,stroke_width=0,fill="#dec509")
violetFlower = petal | scale(2) | translate(y=-50) | repeat(15,rotate(30))
flower4qua = violetFlower | scale(0.20) |translate(x=20,y=20) | repeat(4,rotate(90))

show(background + flower4qua)
    

#stage 12 failure 1
def rhombus(c):
    p1 = point(x=0,y=-100)
    p2 = point(x=50,y=0)
    p3 = point(x=0,y=100)
    p4 = point(x=-50,y=0)
    return(polygon([p1,p2,p3,p4],stroke_width=0,fill=c))
def parallelogram(c):
    p1 = point(x=100,y=-50)
    p2 = point(x=0,y=-50)
    p3 = point(x=-50,y=50)
    p4 = point(x=50,y=50)
    return(polygon([p1,p2,p3,p4],stroke_width=0,fill=c))
black = color(0,0,0)
brown = color(173, 57, 10)
orange = color(219, 95, 7)
blue = color(8, 11, 84)
saffron = color(245, 152, 32)
outerRhombus = rhombus(black)
innerRhombus = rhombus(saffron) | scale(0.25)
top = outerRhombus + innerRhombus
outerParallelogram = parallelogram(brown) 
innerParallelogram = (parallelogram(blue) | scale(0.35) | translate(x=15) )
leftside = (outerParallelogram + innerParallelogram) | translate(x=50,y=50)
outerParallelogram = parallelogram(orange) 
innerParallelogram = (parallelogram(black) | scale(0.35) | translate(x=15) )
rightside = (outerParallelogram + innerParallelogram) | translate(x=50,y=50) | scale(y=-1)
cube = top + leftside + rightside
cubeSequence = cube | scale(0.15) | translate(x=-60) | repeat(6,rotate(60))


teal = color(3, 74, 49)
greenYellow = color(197, 219, 29)
sequence = circle(r=50,stroke=teal,stroke_width=2,x=0,y=30)
sequence = sequence + (circle(r=50,stroke=greenYellow,stroke_width=2,x=0,y=30) | rotate(10))
sequence = sequence | repeat(10,rotate(36))
# flower = sequence | scale(0.3) | translate(y=100) | repeat(10,rotate(36))
background = circle(r=100,fill=color(240, 200, 24),stroke_width=45,stroke="#5c0436") + (sequence | scale(0.4))

# petal = ellipse(x=0,y=50,w=20,h=50,stroke_width=0,fill="#5c0436") + ellipse(x=0,y=40,w=10,h=30,stroke_width=0,fill="#dec509")
# violetFlower = petal | scale(2) | translate(y=-50) | repeat(15,rotate(30))
# flower4qua = violetFlower | scale(0.10) |translate(x=10,y=10) | repeat(8,rotate(45))

show(background + cubeSequence)

#stage 12
def random_color():
    r = random(100)
    g = random(100)
    b = random(100)
    return color(r=r, g=g, b=b)
def triangle(c):
    p1 = point(x=0,y=0)
    p2 = point(x=0,y=100)
    p3 = point(x=50,y=75)
    return polygon([p1,p2,p3],stroke_width=0,fill=c,y=10)

light = "#e52165"
dark = "#0d1137"

newShape = triangle(light)
for i in range(12):
    if(i%2 == 0):
        newShape = newShape + (triangle(dark) | rotate(i * -30))
    else:
        newShape = newShape + (triangle(light) | rotate(i * -30))
    
show(newShape)

#stage 13
light = color(255, 215, 0)
dark = "#C0C0C0"
def triangle(c):
    p1 = point(x=0,y=0)
    p2 = point(x=0,y=100)
    p3 = point(x=50,y=75)
    return (polygon([p1,p2,p3],stroke_width=0,fill=c))
 
def spiral(light,dark):
    newShape = triangle(light)
    for i in range(12):
        if(i%2 == 0):
            newShape = newShape + (triangle(dark) | rotate(i * -30))
        else:
            newShape = newShape + (triangle(light) | rotate(i * -30))
    return (newShape)
    
show(spiral(light,dark) + circle(r=10,stroke_width=0,fill="#000000"))

#stage14

def petal(c,s):
    p1 = point(x=-50,y=50)
    p2 = point(x=50,y=50)
    p3 = point(x=25,y=-50)
    p4 = point(x=-25,y=-50)
    combined_shape = polygon([p1,p2,p3,p4],fill=c,stroke_width=0) + cirlce(r=50,y=50,fill=c,stroke_width=2,stroke=s)
    return (combined_shape)

#colors
black = color(0,0,0)
lavender = color(150, 109, 237)
magenta = color(207, 2, 57)
cream = color(245, 184, 64)
orange = color(232, 50, 9)


small_black_circle = circle(r=10,fill=black,x=0,y=30)
black_circle = small_black_circle | repeat(12,rotate(36))

violet_circle = circle(r=35,fill=lavender)

magenta_circle = circle(r=40,fill=magenta)

small_flower = combine([magenta_circle,black_circle,violet_circle])

small_petals = petal(cream,orange) | scale(0.3) | translate(y=38) | repeat(10,rotate(36))

medium_flower = small_flower + small_petals

show(medium_flower)

#half success

#functions
def triangle(c):
    p1 = point(x=0,y=0)
    p2 = point(x=0,y=100)
    p3 = point(x=50,y=75)
    return polygon([p1,p2,p3],stroke_width=0,fill=c,y=10)

def spiral(light,dark):
    newShape = triangle(light)
    for i in range(12):
        if(i%2 == 0):
            newShape = newShape + (triangle(dark) | rotate(i * -30))
        else:
            newShape = newShape + (triangle(light) | rotate(i * -30))
    return (newShape)

def petal(c,s):
    p1 = point(x=-50,y=50)
    p2 = point(x=50,y=50)
    p3 = point(x=25,y=-50)
    p4 = point(x=-25,y=-50)
    combined_shape = circle(r=50,y=50,fill=c,stroke_width=8,stroke=s) + polygon([p1,p2,p3,p4],fill=c,stroke_width=0)
    return (combined_shape)

#colors
black = color(0,0,0)
lavender = color(73, 84, 235)
magenta = color(207, 2, 57)
white = color(255,255,255)
cream = color(245, 184, 64)
orange = color(232, 50, 9)
yellow = color(232, 206, 9)
silver = color(111, 114, 117)
dull_blue = color(34, 88, 163)
violet = "#5c0436"
yellowish = "#dec509"
green = color(213, 232, 5)
teal = color(0, 86, 89)

small_black_circle = circle(r=8,fill=black,x=0,y=30,stroke=white)
black_circle = small_black_circle | repeat(12,rotate(30))

violet_circle = circle(r=25,fill=lavender)

magenta_circle = circle(r=40,fill=magenta,stroke_width=0)

small_flower = combine([magenta_circle,black_circle,violet_circle])

small_petals = petal(cream,orange) | scale(0.3) | translate(y=38) | repeat(10,rotate(36))

medium_flower = small_petals + small_flower

spiral_around = spiral(yellowish,violet)

show(spiral_around + medium_flower)






