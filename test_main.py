import os
from main import calculate_average_gdp, run_report


def test_calculate_average_gdp():
    """Test calculation of average GDP."""
    data = [
        {"country": "TestCountry", "gdp": "100"},
        {"country": "TestCountry", "gdp": "200"},
    ]

    headers, rows = calculate_average_gdp(data)

    assert rows[0] == ["TestCountry", "150.00"]


def test_report_run(capsys):
    """Test report running."""
    with open("test.csv", "w") as f:
        f.write("country,gdp\nChina,500\nUSA,100")

    run_report(["test.csv"], "average-gdp")

    out, _ = capsys.readouterr()
    assert "China" in out
    assert "500.00" in out

    os.remove("test.csv")
