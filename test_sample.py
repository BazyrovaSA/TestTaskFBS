import pytest
import trianglePack


def test_positive():
    triangle1 = trianglePack.Triangle((0.5, 0.1), (0.6, 0.2), (0.7, 0.3))
    assert triangle1.existence() == True


def test_line1():
    triangle2 = trianglePack.Triangle((2.32, 1.01), (2.32, 2.02), (2.32, 3.03))
    assert triangle2.existence() == False


def test_line2():
    triangle3 = trianglePack.Triangle((1.1, 1.2), (2.1, 1.2), (3.1, 1.2))
    assert triangle3.existence() == False


def test_zeroDot():
    triangle4 = trianglePack.Triangle((0, 0), (0, 0), (0, 0))
    assert triangle4.existence() == False


def test_oneDot():
    triangle5 = trianglePack.Triangle((1, 1), (1, 1), (1, 1))
    assert triangle5.existence() == False


def test_twoDots1():
    triangle6 = trianglePack.Triangle((1, 1), (1, 1), (2, 2))
    assert triangle6.existence() == False


def test_twoDots2():
    triangle7 = trianglePack.Triangle((2, 2), (1, 1), (1, 1))
    assert triangle7.existence() == False


def test_twoDots3():
    triangle8 = trianglePack.Triangle((1, 1), (2, 2), (1, 1))
    assert triangle8.existence() == False