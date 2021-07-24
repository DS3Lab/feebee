from absl import app
from absl import flags
from absl import logging
import os
import pandas as pd

FLAGS = flags.FLAGS

LSF_PREFIX = "_lsf."
CSV_SUFFIX = ".csv"

def main(argv):

    base_path = "outputs/"

    columns = ["dataset", "method", "split", "identifier", "status"]
    results = []

    for dataset in sorted(os.listdir(base_path)):
        print(dataset)

        for method in sorted(os.listdir(os.path.join(base_path, dataset))):
            print(" ", method)

            for split in sorted(os.listdir(os.path.join(base_path, dataset, method))):
                print("  ", split)

                path = os.path.join(base_path, dataset, method, split)

                suffix = {}

                files = sorted(os.listdir(path))

                for f in files:
                    if f.startswith(LSF_PREFIX):
                        identifier = f[len(LSF_PREFIX):]
                        if identifier in suffix:
                            continue
                        if f"{identifier}{CSV_SUFFIX}" not in files:
                            logging.log(logging.INFO, f"{identifier} in folder {path} has LSF file but no CSV files.")
                            # TODO check for timeout or other error (e.g., OOM)
                            # suffix[identifier] = "TIMEOUT"
                            suffix[identifier] = "ERROR"
                        else:
                            suffix[identifier] = "OK"
                    elif f.endswith(CSV_SUFFIX):
                        identifier = f[:-len(CSV_SUFFIX)]
                        if identifier in suffix:
                            continue
                        if f"{LSF_PREFIX}{identifier}" not in files:
                            logging.log(logging.WARNING, f"{identifier} in folder {path} has a CSV file but no LSF files.")
                        suffix[identifier] = "OK"
                    else:
                        logging.log(logging.ERROR, f"{f} in folder {path} has an invalid format.")
                        continue

                    results.append([dataset, method, split, identifier, suffix[identifier]])

    df = pd.DataFrame(data=results, columns=columns)
    df.to_csv("results_overview.csv")

if __name__ == "__main__":
    app.run(main)
