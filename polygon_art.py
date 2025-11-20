import turtle
import random

# ------------------------------
# Polygon Object
# ------------------------------
class Shape:
    def __init__(self, sides, length, heading, pos, fill, pen):
        self.sides = sides
        self.length = length
        self.heading = heading
        self.pos = pos
        self.fill = fill
        self.pen = pen

    def render(self):
        turtle.penup()
        turtle.goto(self.pos[0], self.pos[1])
        turtle.setheading(self.heading)
        turtle.pensize(self.pen)
        turtle.color(self.fill)
        turtle.pendown()

        angle = 360 / self.sides
        for _ in range(self.sides):
            turtle.forward(self.length)
            turtle.left(angle)

        turtle.penup()


# ------------------------------
# Art Manager
# ------------------------------
class ArtMaker:
    def __init__(self):
        turtle.bgcolor("black")
        turtle.speed(0)
        turtle.colormode(255)
        turtle.tracer(0)

    # random helpers
    def rand_color(self):
        return tuple(random.randint(0, 255) for _ in range(3))

    def rand_pos(self):
        return [random.randint(-300, 300),
                random.randint(-250, 250)]

    def generate_one(self, n_sides):
        side_len = random.randint(30, 150)
        rot = random.randint(0, 360)
        col = self.rand_color()
        thick = random.randint(1, 6)
        xy = self.rand_pos()

        Shape(n_sides, side_len, rot, xy, col, thick).render()

    # --- ART PATTERNS ---
    def pattern_tri(self):
        for _ in range(35):
            self.generate_one(3)

    def pattern_square(self):
        for _ in range(35):
            self.generate_one(4)

    def pattern_pent(self):
        for _ in range(35):
            self.generate_one(5)

    def pattern_mixed_basic(self):
        for _ in range(40):
            self.generate_one(random.choice([3, 4, 5]))

    # -------- Nested patterns (tri, sq, pent, mix) ----------
    def nested_generic(self, side_list):
        for _ in range(30):
            base = random.randint(60, 150)
            location = self.rand_pos()
            rotate = random.randint(0, 360)
            clr = self.rand_color()
            n_layers = random.randint(3, 6)
            current_len = base
            chosen_side = random.choice(side_list)

            for layer in range(n_layers):
                pen_w = 3 if layer == 0 else 1
                Shape(chosen_side, current_len, rotate, location, clr, pen_w).render()

                current_len *= 0.70
                rotate += random.randint(-12, 12)

    def pattern_nested_tri(self):
        self.nested_generic([3])

    def pattern_nested_sq(self):
        self.nested_generic([4])

    def pattern_nested_pent(self):
        self.nested_generic([5])

    def pattern_nested_mix(self):
        self.nested_generic([3, 4, 5])

    # Free style
    def pattern_free(self):
        for _ in range(40):
            sides = random.choice([3, 4, 5])
            length = random.randint(40, 140)
            pos = self.rand_pos()
            ang = random.randint(0, 360)
            col = self.rand_color()
            border = random.randint(2, 5)

            Shape(sides, length, ang, pos, col, border).render()


# ------------------------------
# MAIN PROGRAM
# ------------------------------
def main():
    print("\nChoose a pattern:")
    print("1. Triangles")
    print("2. Squares")
    print("3. Pentagons")
    print("4. Mixed Polygons")
    print("5. Nested Triangles")
    print("6. Nested Squares")
    print("7. Nested Pentagons")
    print("8. Mixed Nested")
    print("9. Free Mixed")

    try:
        opt = int(input("\nEnter option (1-9): "))
    except:
        print("Invalid input.")
        return

    drawer = ArtMaker()

    actions = {
        1: drawer.pattern_tri,
        2: drawer.pattern_square,
        3: drawer.pattern_pent,
        4: drawer.pattern_mixed_basic,
        5: drawer.pattern_nested_tri,
        6: drawer.pattern_nested_sq,
        7: drawer.pattern_nested_pent,
        8: drawer.pattern_nested_mix,
        9: drawer.pattern_free
    }

    if opt in actions:
        actions[opt]()
    else:
        print("Invalid selection.")
        return

    turtle.update()
    turtle.done()


main()
