import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.bgcolor("white")

# Hàm vẽ một cánh hoa
def draw_petal(t, radius, angle):
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)

# Hàm vẽ hoa hướng dương
def draw_sunflower(t, petals, radius, angle):
    t.color("pink", "pink")  # Màu cánh hoa
    t.begin_fill()
    for _ in range(petals):
        draw_petal(t, radius, angle)
        t.left(360 / petals)
    t.end_fill()

# Hàm vẽ nhụy hoa
def draw_center(t, radius):
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.color("purple")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Hàm vẽ thân cây
def draw_stem(t, length):
    t.color("green")
    t.right(90)
    t.forward(length)

# Hàm vẽ lá chi tiết
def draw_detailed_leaf(t, angle, size):
    t.setheading(angle)  # Đặt góc cho turtle
    t.begin_fill()
    t.fillcolor("green")
    
    # Vẽ nửa bên trái của lá
    t.circle(size, 90)  # Vẽ cung tròn 90 độ
    t.left(90)
    t.circle(size // 2, 90)
    
    # Vẽ răng cưa
    for _ in range(3):
        t.left(120)
        t.forward(size // 6)
        t.right(120)
        t.forward(size // 6)
    
    # Kết thúc lá
    t.right(60)
    t.circle(size // 2, 90)
    t.left(90)
    t.circle(size, 90)
    t.end_fill()

# Hàm vẽ chữ chúc mừng
def draw_text(text, x, y, font_size):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("blue")
    pen.write(text, align="center", font=("Arial", font_size, "bold"))

# Khởi tạo turtle để vẽ hoa hướng dương
sunflower = turtle.Turtle()
sunflower.shape("turtle")
sunflower.speed(10)

# Vẽ cánh hoa hướng dương
draw_sunflower(sunflower, petals=20, radius=100, angle=60)

# Vẽ nhụy hoa ở giữa
draw_center(sunflower, radius=20)

# Di chuyển xuống để vẽ thân và lá
sunflower.penup()
sunflower.goto(0, -100)
sunflower.pendown()

# Vẽ thân cây
draw_stem(sunflower, 300)

# Vẽ lá thứ nhất
sunflower.penup()
sunflower.goto(-30, -170)
sunflower.pendown()
draw_detailed_leaf(sunflower, 45, 50)

# Vẽ lá thứ hai
sunflower.penup()
sunflower.goto(30, -220)
sunflower.pendown()
draw_detailed_leaf(sunflower, -45, 50)

# Thêm dòng chữ chúc mừng
draw_text("Tặng một bông hoa nhân ngày sinh nhật cho người đẹp", 0, -310, 16)
draw_text("Chúc bé luôn xinh đẹp và cười tươi mỗi ngày", 0, -350, 16)

# Giữ cửa sổ để xem kết quả
turtle.done()