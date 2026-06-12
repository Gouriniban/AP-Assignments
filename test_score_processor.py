import pytest
from score_processor import ScoreProcessor


def test_valid_score_file(tmp_path):
    # Create a temporary valid file
    test_file = tmp_path / "valid_score.txt"
    test_file.write_text("7")

    processor = ScoreProcessor()

    result = processor.process_score_file(str(test_file))

    assert result == 70


def test_missing_file():
    processor = ScoreProcessor()

    with pytest.raises(FileNotFoundError):
        processor.process_score_file("missing_file.txt")


def test_invalid_data_file(tmp_path):
    # Create a file with invalid data
    test_file = tmp_path / "invalid_score.txt"
    test_file.write_text("abc")

    processor = ScoreProcessor()

    with pytest.raises(ValueError):
        processor.process_score_file(str(test_file))