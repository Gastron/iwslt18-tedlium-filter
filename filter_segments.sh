#!/bin/bash
#Runs the IWSLT exclusion list filter on the data
#We run it on all the sets for posterity and proof,
#but there are conflicting speakers in the train data only

for datadir in data/train.orig data/dev.orig data/test.orig; do
  iwslt18-tedlium-filter/filter.py iwslt18-tedlium-filter/exclusion-list.txt \
    "$datadir"/spk2utt > "$datadir"/spk2keep
  utils/subset_data_dir.sh --spk-list "$datadir"/spk2keep "$datadir" "$datadir".filt
done
