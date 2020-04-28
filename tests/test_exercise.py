import pytest
import src.exercise

def test_exercise():
    input_values = ["6","4","-1"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert [output[0],output[1],output[2],output[3]] == ["Give numbers:","Give numbers:","Give numbers:","Thx! Bye!"]
    assert [output[4],output[5],output[6],output[7],output[8]] == ["Sum: 10","Numbers: 2","Average: 5.0","Even: 2","Odd: 0"]
