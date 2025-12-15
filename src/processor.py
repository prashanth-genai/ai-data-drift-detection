class DriftDetector:
    """
    Detects data drift by comparing baseline and current data distributions.
    """

    def __init__(self, threshold=20):
        self.threshold = threshold
        self.baseline_data = []
        self.current_data = []

    def load_data(self, records):
        """
        Input format: data_type,metric_value
        data_type -> baseline or current
        """
        for record in records:
            try:
                data_type, value = record.split(",")
                value = float(value)

                if data_type == "baseline":
                    self.baseline_data.append(value)
                elif data_type == "current":
                    self.current_data.append(value)

            except Exception:
                continue

    def detect_drift(self):
        """
        Simple drift logic using mean difference
        """
        if not self.baseline_data or not self.current_data:
            return False, 0

        baseline_mean = sum(self.baseline_data) / len(self.baseline_data)
        current_mean = sum(self.current_data) / len(self.current_data)

        drift_value = abs(current_mean - baseline_mean)

        drift_detected = drift_value > self.threshold
        return drift_detected, round(drift_value, 2)

