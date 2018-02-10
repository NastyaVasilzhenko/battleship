import pytest

from filecmp import cmp
from main import play_battleship

tests = [["tests/"+str(i).zfill(2)+"__IN.txt", "tests/"+str(i).zfill(2)+"__OUT.txt"] for i in range(1, 17)]


@pytest.fixture(params=tests)
def file_paths(request):
    return request.param


def test_play_battleship(file_paths):

    print("TEST "+file_paths[0])
    play_battleship(file_paths[0], 'test_output.txt')
    assert cmp(file_paths[1], 'test_output.txt')
