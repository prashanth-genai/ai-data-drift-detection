from src.processor import DriftDetector

def test_no_drift_detected():
    detector = DriftDetector(threshold=50)
    detector.baseline_data = [{"clicks": 50}, {"clicks": 60}]
    detector.current_data = [{"clicks": 55}, {"clicks": 65}]

    drift, _ = detector.detect_drift()
    assert drift is False

def test_drift_detected():
    detector = DriftDetector(threshold=10)
    detector.baseline_data = [{"clicks": 50}, {"clicks": 60}]
    detector.current_data = [{"clicks": 120}, {"clicks": 130}]

    drift, value = detector.detect_drift()
    assert drift is True
    assert value > 10

