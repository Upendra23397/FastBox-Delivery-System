from delivery_system import load_data, assign_packages, simulate_delivery


# Load existing data
data = load_data("data.json")

# Show package -> agent assignments
assignments = assign_packages(data)

print("\n--- PACKAGE ASSIGNMENTS ---")

for agent, packages in assignments.items():
    print(f"\n{agent}:")
    
    if not packages:
        print("  No packages")
        continue

    for package in packages:
        print(
            f"  {package['id']} "
            f"-> Warehouse: {package.get('warehouse') or package.get('warehouse_id')}"
        )


# Run delivery simulation
report, assignments, details = simulate_delivery(data)

print("\n--- DELIVERY REPORT ---")

for agent, info in report.items():
    if agent == "best_agent":
        continue

    print(f"\nAgent: {agent}")
    print(f"Packages Delivered: {info['packages_delivered']}")
    print(f"Total Distance: {info['total_distance']}")
    print(f"Efficiency: {info['efficiency']}")

print("\nBest Agent:", report["best_agent"])


# Show individual delivery details
print("\n--- DELIVERY DETAILS ---")

for item in details:
    print(
        f"{item['package_id']} | "
        f"Agent: {item['agent_id']} | "
        f"Distance: {item['total_trip_distance']}"
    )