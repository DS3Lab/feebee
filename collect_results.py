from absl import app
from absl import flags
from absl import logging
import os
import pandas as pd

FLAGS = flags.FLAGS

flags.DEFINE_string("path", "outputs", "Path to the matrices directory")
flags.DEFINE_string("output_file", "results.csv", "Output file. None to not store results")

CSV_SUFFIX = ".csv"

def main(argv):

    base_path = FLAGS.path

    df = None

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
                    if f.endswith(CSV_SUFFIX):
                        if df is None:
                            df = pd.read_csv(os.path.join(path, f))
                        else:
                            df = df.append(pd.read_csv(os.path.join(path, f)))

    if FLAGS.output_file and df is not None:
        df.to_csv(FLAGS.output_file)

if __name__ == "__main__":
    app.run(main)
