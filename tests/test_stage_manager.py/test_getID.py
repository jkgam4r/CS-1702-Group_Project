from main.stage_manager import getID

def test_T01():
    assert getID('Stage 1') == 'Stage_1'
    
def test_T02():
    assert getID('Stage 3 and Stage 4') == 'Stage_3_and_Stage_4'
    
def test_T03():
    assert getID('stage') == 'stage'

def test_T04():
    assert getID(5) == None
    
def test_T05():
    assert getID('') == None