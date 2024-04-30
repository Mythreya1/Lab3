import price_info

def test_total_cost_shopping():
    total_cost = price_info.total_cost_shopping()
    test_total_cost = 46.75

    assert (test_total_cost == total_cost)


def test_cost_of_fruit():
    test_quantities = {'apple': 5, 'orange': 3, 'watermelon': 1, 'pineapple': 2,
        'pear': 10, 'papaya': 1, 'pomegranate': 2}
    
    test_costs = {'apple': 6.0, 'orange': 4.2, 'watermelon': 6.5, 'pineapple': 5.4,
        'pear': 9.0, 'papaya': 2.95, 'pomegranate': 9.9}

    for fruit in test_quantities.keys():
        cost = price_info.cost_of_fruit(fruit, test_quantities[fruit])
        
        for key in test_costs.keys():
            if key == fruit:
                test_cost = test_costs[key]

    assert (test_cost == cost)
