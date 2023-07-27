select_all_female_bears_return_name_and_age = """
    SELECT 
        bears.name, 
        bears.age
    FROM bears 
    WHERE sex='F';
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT 
        bears.name 
    FROM bears 
    GROUP BY name; 
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    WHERE alive = 1
    GROUP BY age, name;
"""

select_oldest_bear_and_returns_name_and_age = """
    SELECT
        name,
        MAX(age)
    FROM bears
"""
select_youngest_bear_and_returns_name_and_age = """
    SELECT
        name,
        MIN(age)
    FROM bears
"""