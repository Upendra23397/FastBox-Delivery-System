import json
import math
import csv
import random
from pathlib import Path


def load_data(file_path):
    """Read the input JSON file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_location(items, item_id):
    """Get a location from either supported JSON layout."""
    if isinstance(items, dict):
        value = items[item_id]
        return value.get("location") if isinstance(value, dict) else value

    for item in items:
        if item.get("id") == item_id:
            return item.get("location")

    raise KeyError(f"Unknown item: {item_id}")


def get_ids(items):
    """Return IDs from either a dictionary or a list of records."""
    if isinstance(items, dict):
        return list(items.keys())
    return [item["id"] for item in items]


def get_warehouse_id(package):
    return package.get("warehouse") or package.get("warehouse_id")


def distance(point_a, point_b):
    """Return Euclidean distance between two [x, y] points."""
    return math.sqrt(
        (point_a[0] - point_b[0]) ** 2
        + (point_a[1] - point_b[1]) ** 2
    )


def assign_packages(data):
    """Assign every package to the closest agent."""
    assignments = {agent_id: [] for agent_id in get_ids(data["agents"])}

    for package in data["packages"]:
        warehouse_id = get_warehouse_id(package)
        warehouse_location = get_location(data["warehouses"], warehouse_id)

        nearest_agent = min(
            get_ids(data["agents"]),
            key=lambda agent_id: distance(
                get_location(data["agents"], agent_id),
                warehouse_location,
            ),
        )

        assignments[nearest_agent].append(package)

    return assignments


def simulate_delivery(data):
    """
    Simulate delivery for each package.

    The assignment is based on the agent's starting location. Each package is
    treated as an individual delivery trip, so its distance is:

        agent -> warehouse + warehouse -> destination

    This keeps the simulation deterministic and does not depend on the order
    in which packages happen to be listed in the JSON file.
    """
    assignments = assign_packages(data)

    report = {}
    delivery_details = []

    for agent_id, packages in assignments.items():
        agent_location = get_location(data["agents"], agent_id)
        total_distance = 0.0

        for package in packages:
            warehouse_id = get_warehouse_id(package)
            warehouse_location = get_location(data["warehouses"], warehouse_id)

            pickup_distance = distance(agent_location, warehouse_location)
            delivery_distance = distance(
                warehouse_location, package["destination"]
            )
            trip_distance = pickup_distance + delivery_distance

            total_distance += trip_distance

            delivery_details.append(
                {
                    "package_id": package["id"],
                    "agent_id": agent_id,
                    "warehouse_id": warehouse_id,
                    "pickup_distance": round(pickup_distance, 2),
                    "delivery_distance": round(delivery_distance, 2),
                    "total_trip_distance": round(trip_distance, 2),
                }
            )

        count = len(packages)
        efficiency = total_distance / count if count else 0.0

        report[agent_id] = {
            "packages_delivered": count,
            "total_distance": round(total_distance, 2),
            "efficiency": round(efficiency, 2),
        }

    active_agents = [
        agent_id for agent_id in report if report[agent_id]["packages_delivered"] > 0
    ]

    if active_agents:
        best_agent = min(
            active_agents,
            key=lambda agent_id: report[agent_id]["efficiency"],
        )
    else:
        best_agent = None

    report["best_agent"] = best_agent

    return report, assignments, delivery_details


def save_report(report, file_path="report.json"):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)


def save_delivery_details(details, file_path="delivery_details.json"):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(details, file, indent=4)


def save_top_performer_csv(report, file_path="top_performer.csv"):
    best_agent = report.get("best_agent")

    if not best_agent:
        return

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["agent_id", "packages_delivered", "total_distance", "efficiency"]
        )

        data = report[best_agent]
        writer.writerow(
            [
                best_agent,
                data["packages_delivered"],
                data["total_distance"],
                data["efficiency"],
            ]
        )


def make_ascii_routes(data, assignments):
    """Create a small text summary of the assigned routes."""
    lines = ["FastBox Route Summary", "======================="]

    for agent_id, packages in assignments.items():
        package_ids = [package["id"] for package in packages]
        if package_ids:
            lines.append(f"{agent_id}: " + " -> ".join(package_ids))
        else:
            lines.append(f"{agent_id}: no packages")

    return "\n".join(lines)


def main():
    input_file = Path("data.json")
    report_file = Path("report.json")

    data = load_data(input_file)
    report, assignments, details = simulate_delivery(data)

    save_report(report, report_file)
    save_delivery_details(details)

    # Optional bonus outputs.
    Path("routes.txt").write_text(
        make_ascii_routes(data, assignments),
        encoding="utf-8",
    )
    save_top_performer_csv(report)

    print("FastBox delivery simulation completed.")
    print(f"Packages processed: {len(data['packages'])}")
    print(f"Report saved to: {report_file}")
    print(f"Best agent: {report['best_agent']}")


if __name__ == "__main__":
    main()
