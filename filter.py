#!/usr/bin/env python3
#Filter the TED-LIUM corpus according to IWSLT exclusion list

def read_names(exclusion_list):
  names = []
  with open(exclusion_list) as f:
    for talk in [line.rsplit("/",1)[1] for line in f]:
      firstname, lastname, *topic = talk.strip().split("_")
      names.append((firstname, lastname))
  return names

def line_filter(kaldi_line, names):
  normalised_line = kaldi_line.lower()
  for firstname, lastname in names:
    if firstname in normalised_line and lastname in normalised_line:
      return False
  else:
    return True

def filter_lines(kaldi_file, names):
  with open(kaldi_file) as f:
    for line in f:
      if line_filter(line, names):
        yield line


if __name__ == "__main__":
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument("exclusion_list")
  parser.add_argument("kaldi_file")
  args = parser.parse_args()

  names = read_names(args.exclusion_list)
  for accepted_line in filter_lines(args.kaldi_file, names):
    print(accepted_line, end="")
