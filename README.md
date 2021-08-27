# FeeBee
FeeBee is a ***F***ram***e***work for ***e***valuating ***B***ayes ***e***rror ***e***stimators on real-world data with unknown underlying distribution.

## How-To: Run the Framework

### Dataset export tool
App 'export.py'. Scripts in ...

### Estimate the lower and upper bounds

### Collect the results

### Estimate the areas

## How-To: Perform the analysis

Public colab available under: https://colab.research.google.com/drive/1hFmFVyl78eSs8zE2cYx100nAArxa0rRQ?usp=sharing

## How-To: Contribute

In order to test your BER estimator using FeeBee, please submit a pull-request with your own BER estimator (new file in the folder `methods`).
Your method needs to implement the follow

### Interface BER Estimator

Input: lib/dataset
Output: Upper and lower bound
