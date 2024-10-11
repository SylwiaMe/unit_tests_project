from lib.gratitudes import *

def test_the_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add('health')
    assert gratitudes.format() == 'Be grateful for: health'

def test_gratitudes_second():
    g = Gratitudes()
    g.add('money')
    g.add('happiness')
    assert g.gratitudes == ["money", 'happiness']
    assert g.format() == 'Be grateful for: money, happiness'