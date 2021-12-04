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
green = color(3, 48, 5)
teal = color(0, 86, 89)
pink = color(245, 66, 126,0.8)
gold = color(236, 245, 66,0.5)

small_black_circle = circle(r=8,fill=black,x=0,y=30,stroke=white)
black_circle = small_black_circle | repeat(12,rotate(30))

violet_circle = circle(r=25,fill=lavender)

magenta_circle = circle(r=40,fill=magenta,stroke_width=0)

small_flower = combine([magenta_circle,black_circle,violet_circle])

small_petals = petal(cream,orange) | scale(0.3) | translate(y=38) | repeat(10,rotate(36))

medium_flower = small_petals + small_flower

spiral_around = spiral(yellowish,violet)

teal = color(3, 74, 49)
greenYellow = color(197, 219, 29)
sequence = circle(r=50,stroke=teal,stroke_width=5,x=0,y=30)
sequence = sequence + (circle(r=50,stroke=greenYellow,stroke_width=5,x=0,y=30) | rotate(10))
sequence = sequence | repeat(10,rotate(36))
flowers_of_circles = sequence | scale(0.4) | translate(y=100) | repeat(10,rotate(36))

large_flower = flowers_of_circles + spiral_around + medium_flower

make_it_small = large_flower | scale(0.6)

ring =  circle(r=82,fill=white,stroke=dull_blue,stroke_width=5)

circular_design = ring + make_it_small

squares2= rectangle(w=170,h=170,fill=gold,stroke_width=0) | repeat(15,rotate(30))
squares1 = rectangle(w=170, h=170, fill= pink, stroke_width=0) | repeat(30,rotate(20))

pearl = circle(r=5,stroke_width=0,fill=dull_blue, x=0, y= 120) | repeat(12,rotate(30))

pookalam = combine([pearl,squares1,squares2,circular_design])

show(pookalam)
