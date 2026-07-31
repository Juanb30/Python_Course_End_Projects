# This script analyzes customer orders to identify spending patterns,
# product trends, customer classifications, and category revenue.

from collections import Counter

LINE = "=" * 72
DIVIDER = "-" * 72


# -------------------------------------------------------------------
# Predefined customer and order data
# -------------------------------------------------------------------

customer_names = [
    "Alice",
    "Brian",
    "Carla",
    "David",
    "Emma",
    "Frank",
    "Grace",
    "Henry",
]

# Each tuple contains:
# (customer name, product, price, category)
orders = [
    ("Alice", "Laptop", 899.99, "Electronics"),
    ("Alice", "T-Shirt", 24.99, "Clothing"),
    ("Alice", "Desk Lamp", 34.99, "Home Essentials"),
    ("Brian", "Headphones", 79.99, "Electronics"),
    ("Brian", "Jeans", 59.99, "Clothing"),
    ("Carla", "Coffee Maker", 89.99, "Home Essentials"),
    ("Carla", "Blender", 64.99, "Home Essentials"),
    ("David", "Smartphone", 699.99, "Electronics"),
    ("David", "Jacket", 119.99, "Clothing"),
    ("Emma", "T-Shirt", 24.99, "Clothing"),
    ("Frank", "Tablet", 249.99, "Electronics"),
    ("Frank", "Coffee Maker", 89.99, "Home Essentials"),
    ("Grace", "Headphones", 79.99, "Electronics"),
    ("Grace", "Jeans", 59.99, "Clothing"),
    ("Grace", "Desk Lamp", 34.99, "Home Essentials"),
    ("Henry", "Blender", 64.99, "Home Essentials"),
]

# Dictionary that maps products to categories.
product_categories = {
    "Laptop": "Electronics",
    "Headphones": "Electronics",
    "Smartphone": "Electronics",
    "Tablet": "Electronics",
    "T-Shirt": "Clothing",
    "Jeans": "Clothing",
    "Jacket": "Clothing",
    "Desk Lamp": "Home Essentials",
    "Coffee Maker": "Home Essentials",
    "Blender": "Home Essentials",
}


def build_customer_orders(order_data):
    """Create a dictionary of customers and the products they purchased."""

    customer_orders = {}

    for customer, product, price, category in order_data:
        if customer not in customer_orders:
            customer_orders[customer] = []

        customer_orders[customer].append(product)

    return customer_orders


def get_unique_categories(category_mapping):
    """Return a set containing all available product categories."""

    return set(category_mapping.values())


def calculate_customer_totals(customer_list, order_data):
    """Calculate the total amount spent by each customer."""

    customer_totals = {}

    for customer in customer_list:
        customer_totals[customer] = 0.0

    for customer, product, price, category in order_data:
        customer_totals[customer] += price

    return customer_totals


def classify_customer(total_spent):
    """Classify a customer based on total spending."""

    if total_spent > 100:
        return "High-Value Buyer"

    if total_spent >= 50:
        return "Moderate Buyer"

    return "Low-Value Buyer"


def classify_all_customers(customer_totals):
    """Create a dictionary containing each customer's classification."""

    customer_classifications = {}

    for customer, total_spent in customer_totals.items():
        customer_classifications[customer] = classify_customer(total_spent)

    return customer_classifications


def calculate_category_revenue(order_data):
    """Calculate total revenue for each product category."""

    category_revenue = {}

    for customer, product, price, category in order_data:
        category_revenue[category] = category_revenue.get(category, 0.0) + price

    return category_revenue


def get_unique_products(order_data):
    """Return a set of all unique products in the order data."""

    return {product for customer, product, price, category in order_data}


def get_electronics_customers(order_data):
    """Return customers who purchased at least one electronics product."""

    electronics_customers = [
        customer
        for customer, product, price, category in order_data
        if category == "Electronics"
    ]

    return sorted(set(electronics_customers))


def get_top_customers(customer_totals, number_of_customers=3):
    """Return the highest-spending customers using sorting."""

    sorted_customers = sorted(
        customer_totals.items(),
        key=lambda customer_record: customer_record[1],
        reverse=True,
    )

    return sorted_customers[:number_of_customers]


def build_customer_category_sets(customer_list, order_data):
    """Create a dictionary mapping customers to purchased categories."""

    customer_categories = {}

    for customer in customer_list:
        customer_categories[customer] = set()

    for customer, product, price, category in order_data:
        customer_categories[customer].add(category)

    return customer_categories


def get_multi_category_customers(customer_categories):
    """Return customers who purchased from more than one category."""

    return {
        customer
        for customer, categories in customer_categories.items()
        if len(categories) > 1
    }


def get_customers_by_category(order_data, target_category):
    """Return a set of customers who purchased from a target category."""

    return {
        customer
        for customer, product, price, category in order_data
        if category == target_category
    }


def get_product_purchase_counts(order_data):
    """Count how many times each product was purchased."""

    product_names = [product for customer, product, price, category in order_data]

    return Counter(product_names)


def get_most_frequent_products(product_counts):
    """Return the products with the highest purchase frequency."""

    if not product_counts:
        return []

    highest_count = max(product_counts.values())

    return sorted(
        product for product, count in product_counts.items() if count == highest_count
    )


def display_title():
    """Display the project title."""

    print(f"\n{LINE}")
    print("                 CUSTOMER ORDER ANALYSIS")
    print("              E-Commerce Business Insights")
    print(LINE)


def display_customer_order_dictionary(customer_orders):
    """Display each customer and the products they purchased."""

    print("\nCUSTOMER ORDER RECORDS")
    print(DIVIDER)

    for customer, products in customer_orders.items():
        product_list = ", ".join(products)
        print(f"{customer:<10} : {product_list}")


def display_categories(unique_categories):
    """Display all available product categories."""

    print("\nAVAILABLE PRODUCT CATEGORIES")
    print(DIVIDER)

    for category in sorted(unique_categories):
        print(f"- {category}")


def display_customer_summary(customer_totals, customer_classifications):
    """Display customer spending totals and classifications."""

    print("\nCUSTOMER SPENDING SUMMARY")
    print(DIVIDER)
    print(f"{'Customer':<12}{'Total Spent':>15}{'Classification':>30}")
    print(DIVIDER)

    for customer, total_spent in customer_totals.items():
        classification = customer_classifications[customer]

        print(f"{customer:<12}" f"${total_spent:>14,.2f}" f"{classification:>30}")


def display_category_revenue(category_revenue):
    """Display total sales revenue by category."""

    print("\nREVENUE BY PRODUCT CATEGORY")
    print(DIVIDER)
    print(f"{'Category':<25}{'Revenue':>18}")
    print(DIVIDER)

    sorted_revenue = sorted(
        category_revenue.items(),
        key=lambda category_record: category_record[1],
        reverse=True,
    )

    for category, revenue in sorted_revenue:
        print(f"{category:<25}${revenue:>17,.2f}")


def display_unique_products(unique_products):
    """Display all unique products."""

    print("\nUNIQUE PRODUCTS SOLD")
    print(DIVIDER)

    for product in sorted(unique_products):
        print(f"- {product}")


def display_electronics_customers(electronics_customers):
    """Display customers who purchased electronics."""

    print("\nCUSTOMERS WHO PURCHASED ELECTRONICS")
    print(DIVIDER)

    for customer in electronics_customers:
        print(f"- {customer}")


def display_top_customers(top_customers):
    """Display the top three highest-spending customers."""

    print("\nTOP THREE HIGHEST-SPENDING CUSTOMERS")
    print(DIVIDER)

    for position, customer_record in enumerate(top_customers, start=1):
        customer, total_spent = customer_record
        print(f"{position}. {customer:<10} ${total_spent:,.2f}")


def display_category_customer_analysis(
    customer_categories,
    multi_category_customers,
    common_customers,
):
    """Display customer category purchasing patterns."""

    print("\nCUSTOMER CATEGORY PURCHASES")
    print(DIVIDER)

    for customer, categories in customer_categories.items():
        category_list = ", ".join(sorted(categories))
        print(f"{customer:<10} : {category_list}")

    print("\nCUSTOMERS WHO PURCHASED FROM MULTIPLE CATEGORIES")
    print(DIVIDER)

    if multi_category_customers:
        for customer in sorted(multi_category_customers):
            print(f"- {customer}")
    else:
        print("No customers purchased from multiple categories.")

    print("\nCUSTOMERS WHO PURCHASED BOTH ELECTRONICS AND CLOTHING")
    print(DIVIDER)

    if common_customers:
        for customer in sorted(common_customers):
            print(f"- {customer}")
    else:
        print("No customers purchased both electronics and clothing.")


def display_product_frequency(product_counts, most_frequent_products):
    """Display purchase frequency for each product."""

    print("\nPRODUCT PURCHASE FREQUENCY")
    print(DIVIDER)
    print(f"{'Product':<25}{'Purchases':>12}")
    print(DIVIDER)

    sorted_counts = sorted(
        product_counts.items(),
        key=lambda product_record: (
            -product_record[1],
            product_record[0],
        ),
    )

    for product, count in sorted_counts:
        print(f"{product:<25}{count:>12}")

    print("\nMOST FREQUENTLY PURCHASED PRODUCT(S)")
    print(DIVIDER)

    highest_count = max(product_counts.values())

    for product in most_frequent_products:
        print(f"- {product}: {highest_count} purchases")


def display_business_insights(
    customer_totals,
    customer_classifications,
    category_revenue,
    top_customers,
    most_frequent_products,
    electronics_customers,
    multi_category_customers,
):
    """Display major business insights from the analysis."""

    high_value_customers = [
        customer
        for customer, classification in customer_classifications.items()
        if classification == "High-Value Buyer"
    ]

    top_category = max(
        category_revenue,
        key=category_revenue.get,
    )

    total_revenue = sum(category_revenue.values())
    average_customer_spending = total_revenue / len(customer_totals)

    print("\nKEY BUSINESS INSIGHTS")
    print(DIVIDER)

    print(f"1. Total business revenue was ${total_revenue:,.2f}.")

    print(
        "2. The most profitable category was "
        f"{top_category} with ${category_revenue[top_category]:,.2f} "
        "in revenue."
    )

    print(f"3. There were {len(high_value_customers)} " "high-value customers.")

    print(
        f"4. The highest-spending customer was "
        f"{top_customers[0][0]} with ${top_customers[0][1]:,.2f}."
    )

    print(
        "5. The most frequently purchased product(s) were: "
        f"{', '.join(most_frequent_products)}."
    )

    print(f"6. {len(electronics_customers)} customers purchased " "electronics.")

    print(
        f"7. {len(multi_category_customers)} customers purchased "
        "products from multiple categories."
    )

    print(f"8. Average customer spending was " f"${average_customer_spending:,.2f}.")

    print(
        "9. High-value customers should be targeted with loyalty "
        "offers and premium product recommendations."
    )

    print(
        f"10. Inventory planning should prioritize {top_category} "
        "because it generated the most revenue."
    )


def main():
    """Run the complete customer order analysis."""

    display_title()

    customer_orders = build_customer_orders(orders)
    unique_categories = get_unique_categories(product_categories)
    customer_totals = calculate_customer_totals(
        customer_names,
        orders,
    )
    customer_classifications = classify_all_customers(customer_totals)
    category_revenue = calculate_category_revenue(orders)
    unique_products = get_unique_products(orders)
    electronics_customers = get_electronics_customers(orders)
    top_customers = get_top_customers(customer_totals)

    customer_categories = build_customer_category_sets(
        customer_names,
        orders,
    )

    multi_category_customers = get_multi_category_customers(customer_categories)

    electronics_customer_set = get_customers_by_category(
        orders,
        "Electronics",
    )

    clothing_customer_set = get_customers_by_category(
        orders,
        "Clothing",
    )

    # Set intersection identifies customers in both categories.
    common_customers = electronics_customer_set & clothing_customer_set

    product_counts = get_product_purchase_counts(orders)
    most_frequent_products = get_most_frequent_products(product_counts)

    display_customer_order_dictionary(customer_orders)
    display_categories(unique_categories)

    display_customer_summary(
        customer_totals,
        customer_classifications,
    )

    display_category_revenue(category_revenue)
    display_unique_products(unique_products)
    display_electronics_customers(electronics_customers)
    display_top_customers(top_customers)

    display_category_customer_analysis(
        customer_categories,
        multi_category_customers,
        common_customers,
    )

    display_product_frequency(
        product_counts,
        most_frequent_products,
    )

    display_business_insights(
        customer_totals,
        customer_classifications,
        category_revenue,
        top_customers,
        most_frequent_products,
        electronics_customers,
        multi_category_customers,
    )

    print(f"\n{LINE}")
    print("                ANALYSIS COMPLETE")
    print(LINE)


if __name__ == "__main__":
    main()
