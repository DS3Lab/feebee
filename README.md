# FeeBee
FeeBee is a ***F***ram***e***work for ***e***valuating ***B***ayes ***e***rror ***e***stimators on real-world data with unknown underlying distribution.

## How-To: Run the Framework

Running the evaluation on all datasets, feature transformations, methods and their hyper-parameters involves four major steps.

### (1) Export all dataset representations
The app used for exporting dataset representation into numpy arrays is can be found in the file `export.py`.
In order to export all representations inspect and run the following scripts:

- `bash scripts/export/mnist.sh`
- `bash scripts/export/cifar10.sh`
- `bash scripts/export/cifar100.sh`
- `bash scripts/export/imdb.sh`
- `bash scripts/export/sst2.sh`
- `bash scripts/export/yelp.sh`

### (2) Estimate the lower and upper bounds

Running all defined methods for a fixed feature transformation, dataset, and set of hyper-parameters can be done using the app given in the file `estimate.py`.
Every method should have a corresponding script in the folder `scripts/estimate/`. The current scripts are written such that they can be executed using [slurm](https://slurm.schedmd.com/documentation.html). Finally, the script `scripts/estimate/run_all.sh` runs all the methods on all datasets.

### (3) Collect the results

Every method executed for a fixed feature transformation, dataset, and set of hyper-parameters creates a single csv file. In order to collect these results into a exported pandas dataframe (`results.csv`), the corresponding script `collect_results.py` needs to be executed.

Running the script `run_analysis.py` allows to collect the failure state of single executions (timeout or memory error).

### Estimate the areas

## How-To: Perform the analysis

Public colab available under: https://colab.research.google.com/drive/1hFmFVyl78eSs8zE2cYx100nAArxa0rRQ?usp=sharing

## How-To: Contribute

In order to test your BER estimator using FeeBee, please submit a pull-request with your own BER estimator as a new file in the folder `methods`.
Your method needs to implement the follow

### Interface BER Estimator

Input: lib/dataset
Output: Upper and lower bound
