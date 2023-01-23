def setup():
    size(800,800)
    
    ellipse(100,100,100,100)
    
    textSize(50)# добавил надпись (работает)
    fill(0,0,0)
    text('python', 300, 200)
    img=loadImage("python.png")# добавил рисунок (работает) 
    image(img,0,0)
    
# изначальная версия кода  
# x=200
# speedX=5
# def draw():
#     background(255)
#     global x, speedX
#     x=x+speedX
#     ellipse(x,x,100,100)
#     if x>width-100/2 or x<0+100/2:
#         fill(random(255),random(255),random(255))
#         speedX=-speedX

# моя версия кода  
# добавил направление по Y (работает не коррекно - меняет сразу несколько направлений при косании края )                           
x=200
speedX=5
y=200
speedY=5
def draw():
    background(255)
    global x, speedX, y, speedY
    x=x+speedX
    y=y+speedY
    #ellipse(x,y,100,100)
    textSize(50)
    text('python', x, y)
    img=loadImage("python.png") 
    image(img,x-30,y+10)
    if x>width-100/2 or x<0+100/2:
        fill(random(128),random(128),random(128))
        speedX=-speedX
    if y>height-100/2-random(90) or y<0+100/2+random(90):
        fill(random(128),random(128),random(128))
        speedY=-speedY
    
