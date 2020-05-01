def append_sum(lst):

  lst += [lst[-1] + lst[-2]]
  lst += [lst[-1] + lst[-2]]
  lst += [lst[-1] + lst[-2]]
  return lst  


append_sum([1, 1, 2])