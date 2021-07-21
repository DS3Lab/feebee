script="scripts/estimate/de_knn.sh"

for dataset in mnist cifar10 cifar100
do
  for suffix in raw pca_32 pca_64 pca_128 nca_64 alexnet_pt googlenet_pt inception_v3_tf efficientnet_b0_tf efficientnet_b1_tf efficientnet_b2_tf efficientnet_b3_tf efficientnet_b4_tf efficientnet_b5_tf efficientnet_b6_tf efficientnet_b7_tf resetnet_v2_101_tf resetnet_v2_152_tf resetnet_v2_50_tf vgg16_pt vgg19_pt
  do
    bash $script $dataset $suffix
  done
done

for dataset in imdb sst2
do
  for suffix in bow bow_tfidf bert elmo nnlm50 nnlm50_norm nnl128 nnlm128_norm use pca_8 pca_16 pca_32 pca_64 pca_128
  do
    bash $script $dataset $suffix
  done
done

dataset="yelp"
for suffix in bert elmo nnlm50 nnlm50_norm nnl128 nnlm128_norm use 
do
  bash $script $dataset $suffix
done