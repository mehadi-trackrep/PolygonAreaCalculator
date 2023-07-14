from shape_calculator import Rectangle, Square

rectangle_obj = Rectangle(10, 5)

def test_rectangle_get_area():
    assert rectangle_obj.get_area() == 50, "get_area() should return 50"
def test_rectangle_get_perimeter():
    rectangle_obj.set_height(3)
    assert rectangle_obj.get_perimeter() == 26, "get_perimeter() should return 26"
def test_rectangle_get_picture():
    rectangle_obj.set_width(4)
    rectangle_obj.set_height(3)
    assert rectangle_obj.get_picture() == "****\n****\n****\n", "get_picture() should return the correct picture"

sq = Square(9)

def test_square_get_area():
    assert sq.get_area() == 81, "get_area() should return 81"
def test_square_set_side():
    sq.set_side(4)
    assert sq.get_area() == 16, "rectangle get_width() should set width and height to 4"
def test_square_get_diagonal():
    assert sq.get_diagonal() == (2 * (4 ** 2)) ** .5, "get_diagonal() should return sqrt(32)"
def test_square_get_picture():
    assert sq.get_picture() == "****\n****\n****\n****\n", "get_picture() should return the correct picture"