import pytest


# data provider using fixture
@pytest.fixture(params=[1, 2, 3, 4, 5])
def data_provider_fixture(request):
    return request.param


def test_fixture_data_provider(data_provider_fixture):
    print("\n")
    print(data_provider_fixture)
    print("test me")


# data provider using marks
@pytest.mark.parametrize("test_input", [1, 2, 3, 4, 5])
def test_fixture_mark_provider(test_input):
    print("\n")
    print(test_input)
    print("test me")
