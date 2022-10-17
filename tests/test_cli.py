import fileinput

from cli import main


def test_example_a(monkeypatch, capsys):
    monkeypatch.setattr(
        fileinput, "input", open("tests/fixtures/example_a_input.txt").readlines
    )
    main()
    captured = capsys.readouterr()
    assert captured.out == "0,1,NORTH\n"


def test_example_b(monkeypatch, capsys):
    monkeypatch.setattr(
        fileinput, "input", open("tests/fixtures/example_b_input.txt").readlines
    )
    main()
    captured = capsys.readouterr()
    assert captured.out == "0,0,WEST\n"


def test_example_c(monkeypatch, capsys):
    monkeypatch.setattr(
        fileinput, "input", open("tests/fixtures/example_c_input.txt").readlines
    )
    main()
    captured = capsys.readouterr()
    assert captured.out == "3,3,NORTH\n"
