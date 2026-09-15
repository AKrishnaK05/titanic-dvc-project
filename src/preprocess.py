import pandas as pd

def preprocess(input_path="data/titanic.csv", output_path="data/processed.csv"):
    df = pd.read_csv(input_path)

    # Drop unnecessary columns
    drop_cols = [c for c in ["Name", "Ticket", "Cabin", "PassengerId"] if c in df.columns]
    df = df.drop(columns=drop_cols)

    # Handle missing values
    if "Age" in df.columns:
        df["Age"] = df["Age"].fillna(df["Age"].mean())
    if "Embarked" in df.columns:
        df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    # Encode categorical columns as numbers
    for col in ["Sex", "Embarked"]:
        if col in df.columns:
            df[col] = df[col].astype("category").cat.codes

    df.to_csv(output_path, index=False)
    print(f"Saved processed data to {output_path}")

if __name__ == "__main__":
    preprocess()