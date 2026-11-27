def test_benchmark():

    # Opening and purchase stock
    flour = 100 + 60 - 40
    oil = 30 - 10.5
    spice = 5 - 1.2
    pouches = 500 - 188 - 6

    # Finished goods
    finished_stock = 50 + 188
    dispatched_stock = finished_stock - 150

    # Variance
    yield_variance = ((188 - 200) / 200) * 100
    oil_variance = ((10.5 - 10) / 10) * 100

    # GST
    taxable = 150 * 50
    cgst = taxable * 0.025
    sgst = taxable * 0.025
    invoice = taxable + cgst + sgst

    outstanding = invoice - 4000

    # Costing
    material_cost = 1725 + 1470 + 240 + 485 + 135
    total_cost = material_cost + 1200 + 600
    cost_per_packet = total_cost / 188

    assert flour == 120
    assert oil == 19.5
    assert round(spice, 1) == 3.8
    assert pouches == 306
    assert finished_stock == 238
    assert dispatched_stock == 88
    assert yield_variance == -6
    assert oil_variance == 5
    assert invoice == 7875
    assert outstanding == 3875
    assert round(cost_per_packet, 2) == 31.14

    print("ALL BENCHMARK TESTS PASSED")


if __name__ == "__main__":
    test_benchmark()
