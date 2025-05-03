# main.py
import argparse
from csv_query.core import query_csv

def main():
    parser = argparse.ArgumentParser(description="Run SQL-like queries on CSV files.")
    parser.add_argument("file", help="Path to the CSV file")
    parser.add_argument("query", help="SQL-like query string")
    parser.add_argument("--output", help="Path to save result as CSV")
    parser.add_argument("--json", help="Path to save result as JSON")

    args = parser.parse_args()

    try:
        result_df = query_csv(args.file, args.query)

        if args.output:
            result_df.to_csv(args.output, index=False)
            print(f"✅ Saved result to CSV: {args.output}")

        if args.json:
            result_df.to_json(args.json, orient="records", indent=2)
            print(f"✅ Saved result to JSON: {args.json}")

        if not args.output and not args.json:
            print(result_df.to_string(index=False))

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
