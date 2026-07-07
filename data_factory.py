
import os
import pandas as pd


def generate_dataset():
    os.makedirs("data/raw", exist_ok=True)

    raw_json_data = [
        {
            "participant_id": 1,
            "condition": "Fake Urgency",
            "trial_id": 1,
            "eeg_theta": 5.42,
            "fnirs_hbo": 0.87,
            "fixation_duration": 312.4,
            "response_time": 1.84,
            "compliance": 1
        },
        {
            "participant_id": 1,
            "condition": "Confirmshaming",
            "trial_id": 2,
            "eeg_theta": 6.11,
            "fnirs_hbo": 1.02,
            "fixation_duration": 355.8,
            "response_time": 2.13,
            "compliance": 1
        }
    ]

    df = pd.DataFrame(raw_json_data)

    file_path = "data/raw/dark_pattern_multimodal_dataset.csv"
    df.to_csv(file_path, index=False)

    print(f"✅ Dataset generated successfully at: {file_path}")
    print(f"📊 Total Records: {len(df)}")


if __name__ == "__main__":
    generate_dataset()
