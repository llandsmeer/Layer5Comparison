NEURON {
  SUFFIX L5PC_axon_group
  NONSPECIFIC_CURRENT i
}

BREAKPOINT {
  i = 0.000032499998807907105 * (90 + v)
}

