from main.stage_manager import Validate_Stage_Data

def test_T06():
    assert Validate_Stage_Data(['stage 1',5, 'field']) == 'valid input'
    
def test_T07():
    assert Validate_Stage_Data(['stage 123123', 123123, 'london']) == 'valid input'
    
def test_T08():
    assert Validate_Stage_Data(5) == 'invalid input'
    
def test_T09():
    assert Validate_Stage_Data('jamie') == 'invalid input'
    
def test_T10():
    assert Validate_Stage_Data([]) == 'invalid input'
    
def test_T11():
    assert Validate_Stage_Data(['str', 'str', 'str']) == 'invalid input'
    
def test_T12():
    assert Validate_Stage_Data([1,2,3,4,5]) == 'invalid input'
    
def test_T13():
    assert Validate_Stage_Data(['stage1', 4, 'field', 555]) == 'invalid input'