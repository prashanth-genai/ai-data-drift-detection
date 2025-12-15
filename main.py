from src.processor import DriftDetector

def main():
    records = [
        "baseline,50",
        "baseline,60",
        "baseline,55",
        "current,120",
        "current,130",
        "current,125"
    ]

    detector = DriftDetector(threshold=10)
    detector.load_data(records)

    drift, value = detector.detect_drift()

    print("\nBaseline Data:", detector.baseline_data)
    print("Current Data:", detector.current_data)

    if drift:
        print(f"\n⚠️ Data Drift Detected! Drift Value: {value}")
    else:
        print("\n✅ No Data Drift Detected")

if __name__ == "__main__":
    main()

