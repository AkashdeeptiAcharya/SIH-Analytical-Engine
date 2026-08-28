from modules.capacity import estimate_capacity
from modules.risk import compute_risk
from modules.realtime import realtime_dashboard


def main() -> None:
    """Entry point for the analytics engine."""
    print("Analytics engine started.")
    print("Capacity:", estimate_capacity())
    print("Risk:", compute_risk())
    realtime_dashboard()


if __name__ == "__main__":
    main()
