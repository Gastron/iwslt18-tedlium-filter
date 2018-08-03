# TED LIUM dataset filtering for IWSLT 2018
Clone this repo inside kaldi tedlium s5\_r2, then run
```
iwslt18-tedlium-filter/run_mod.sh
```
This has only been used with Kaldi revision 230d013

## Filtering principle
The exclusion list provided by IWSLT only lists certain talks, but the talks in the TED LIUM corpus distribution are not explicitly named. We took an ad-hoc approach and filter by trying to match the names of the speakers. In practice this seems to filter a small amount of talks from the training set, and none from the dev or test sets.
