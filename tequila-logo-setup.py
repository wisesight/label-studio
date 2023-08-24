import argparse
import os

import pandas as pd


def main(path: str) -> None:
    df = pd.read_csv(path)

    for idx in df.index:
        row = df.loc[idx]
        email = row["email"]  # tequila.internal@wisesight.com
        password = row["password"]  # wsdev!
        user_token = row["user_token"]  # wisesighttoken
        port = row["port"]  # 8080

        os.system(
            f"sh tequila-start.sh {email} {password} {user_token} {port} logo{str(idx + 1).zfill(2)}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Set the default for the dataset argument
    parser.add_argument("path", type=str, help="Path to CSV config file")
    args = parser.parse_args()

    main(args.path)
