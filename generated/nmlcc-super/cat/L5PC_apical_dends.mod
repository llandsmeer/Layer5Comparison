NEURON {
  SUFFIX L5PC_apical_dends
  USEION ca READ cai
  USEION k WRITE ik READ ek
  USEION na WRITE ina READ ena
  NONSPECIFIC_CURRENT i
}

STATE { Im_gates_m_q NaTa_t_gates_h_q NaTa_t_gates_m_q SK_E2_gates_z_q SKv3_1_gates_m_q }

INITIAL {
  LOCAL SKv3_1_gates_m_steadyState_x, SK_E2_gates_z_steadyState_ca_conc, SK_E2_gates_z_steadyState_x, NaTa_t_gates_m_reverseRate_x, NaTa_t_gates_m_reverseRate_r, NaTa_t_gates_m_forwardRate_x, NaTa_t_gates_m_forwardRate_r, NaTa_t_gates_m_inf, NaTa_t_gates_h_reverseRate_x, NaTa_t_gates_h_reverseRate_r, NaTa_t_gates_h_forwardRate_x, NaTa_t_gates_h_forwardRate_r, NaTa_t_gates_h_inf, Im_gates_m_forwardRate_r, Im_gates_m_reverseRate_r, Im_gates_m_inf

  SKv3_1_gates_m_steadyState_x = (1 + exp(-0.10309278553230808 * (-18.700000762939453 + v)))^-1
  SK_E2_gates_z_steadyState_ca_conc = 0.000001 * cai
  SK_E2_gates_z_steadyState_x = (1 + (0.0000000004300000078227839 * SK_E2_gates_z_steadyState_ca_conc^-1)^4.800000190734863)^-1
  NaTa_t_gates_m_reverseRate_x = -0.16666666666666666 * (38 + v)
  if (NaTa_t_gates_m_reverseRate_x != 0) {
    NaTa_t_gates_m_reverseRate_r = 0.7440000176429749 * NaTa_t_gates_m_reverseRate_x * (1 + -1 * exp(-1 * NaTa_t_gates_m_reverseRate_x))^-1
  } else {
    if (NaTa_t_gates_m_reverseRate_x == 0) {
      NaTa_t_gates_m_reverseRate_r = 0.7440000176429749
    } else {
      NaTa_t_gates_m_reverseRate_r = 0
    }
  }
  NaTa_t_gates_m_forwardRate_x = 0.16666666666666666 * (38 + v)
  if (NaTa_t_gates_m_forwardRate_x != 0) {
    NaTa_t_gates_m_forwardRate_r = 1.0920000076293945 * NaTa_t_gates_m_forwardRate_x * (1 + -1 * exp(-1 * NaTa_t_gates_m_forwardRate_x))^-1
  } else {
    if (NaTa_t_gates_m_forwardRate_x == 0) {
      NaTa_t_gates_m_forwardRate_r = 1.0920000076293945
    } else {
      NaTa_t_gates_m_forwardRate_r = 0
    }
  }
  NaTa_t_gates_m_inf = NaTa_t_gates_m_forwardRate_r * (NaTa_t_gates_m_forwardRate_r + NaTa_t_gates_m_reverseRate_r)^-1
  NaTa_t_gates_h_reverseRate_x = 0.16666666666666666 * (66 + v)
  if (NaTa_t_gates_h_reverseRate_x != 0) {
    NaTa_t_gates_h_reverseRate_r = 0.09000000357627869 * NaTa_t_gates_h_reverseRate_x * (1 + -1 * exp(-1 * NaTa_t_gates_h_reverseRate_x))^-1
  } else {
    if (NaTa_t_gates_h_reverseRate_x == 0) {
      NaTa_t_gates_h_reverseRate_r = 0.09000000357627869
    } else {
      NaTa_t_gates_h_reverseRate_r = 0
    }
  }
  NaTa_t_gates_h_forwardRate_x = -0.16666666666666666 * (66 + v)
  if (NaTa_t_gates_h_forwardRate_x != 0) {
    NaTa_t_gates_h_forwardRate_r = 0.09000000357627869 * NaTa_t_gates_h_forwardRate_x * (1 + -1 * exp(-1 * NaTa_t_gates_h_forwardRate_x))^-1
  } else {
    if (NaTa_t_gates_h_forwardRate_x == 0) {
      NaTa_t_gates_h_forwardRate_r = 0.09000000357627869
    } else {
      NaTa_t_gates_h_forwardRate_r = 0
    }
  }
  NaTa_t_gates_h_inf = NaTa_t_gates_h_forwardRate_r * (NaTa_t_gates_h_forwardRate_r + NaTa_t_gates_h_reverseRate_r)^-1
  Im_gates_m_forwardRate_r = 0.0032999999821186066 * exp(0.1 * (35 + v))
  Im_gates_m_reverseRate_r = 0.0032999999821186066 * exp(-0.1 * (35 + v))
  Im_gates_m_inf = Im_gates_m_forwardRate_r * (Im_gates_m_forwardRate_r + Im_gates_m_reverseRate_r)^-1
  Im_gates_m_q = Im_gates_m_inf
  NaTa_t_gates_h_q = NaTa_t_gates_h_inf
  NaTa_t_gates_m_q = NaTa_t_gates_m_inf
  SK_E2_gates_z_q = SK_E2_gates_z_steadyState_x
  SKv3_1_gates_m_q = SKv3_1_gates_m_steadyState_x
}

DERIVATIVE dstate {
  LOCAL SKv3_1_gates_m_steadyState_x, SKv3_1_gates_m_timeCourse_t, SK_E2_gates_z_steadyState_ca_conc, SK_E2_gates_z_steadyState_x, NaTa_t_gates_m_reverseRate_x, NaTa_t_gates_m_reverseRate_r, NaTa_t_gates_m_forwardRate_x, NaTa_t_gates_m_forwardRate_r, NaTa_t_gates_m_inf, NaTa_t_gates_m_tau, NaTa_t_gates_h_reverseRate_x, NaTa_t_gates_h_reverseRate_r, NaTa_t_gates_h_forwardRate_x, NaTa_t_gates_h_forwardRate_r, NaTa_t_gates_h_inf, NaTa_t_gates_h_tau, Im_gates_m_forwardRate_r, Im_gates_m_reverseRate_r, Im_gates_m_inf, Im_gates_m_tau

  SKv3_1_gates_m_steadyState_x = (1 + exp(-0.10309278553230808 * (-18.700000762939453 + v)))^-1
  SKv3_1_gates_m_timeCourse_t = 4 * (1 + exp(-0.022655188351328265 * (46.560001373291016 + v)))^-1
  SK_E2_gates_z_steadyState_ca_conc = 0.000001 * cai
  SK_E2_gates_z_steadyState_x = (1 + (0.0000000004300000078227839 * SK_E2_gates_z_steadyState_ca_conc^-1)^4.800000190734863)^-1
  NaTa_t_gates_m_reverseRate_x = -0.16666666666666666 * (38 + v)
  if (NaTa_t_gates_m_reverseRate_x != 0) {
    NaTa_t_gates_m_reverseRate_r = 0.7440000176429749 * NaTa_t_gates_m_reverseRate_x * (1 + -1 * exp(-1 * NaTa_t_gates_m_reverseRate_x))^-1
  } else {
    if (NaTa_t_gates_m_reverseRate_x == 0) {
      NaTa_t_gates_m_reverseRate_r = 0.7440000176429749
    } else {
      NaTa_t_gates_m_reverseRate_r = 0
    }
  }
  NaTa_t_gates_m_forwardRate_x = 0.16666666666666666 * (38 + v)
  if (NaTa_t_gates_m_forwardRate_x != 0) {
    NaTa_t_gates_m_forwardRate_r = 1.0920000076293945 * NaTa_t_gates_m_forwardRate_x * (1 + -1 * exp(-1 * NaTa_t_gates_m_forwardRate_x))^-1
  } else {
    if (NaTa_t_gates_m_forwardRate_x == 0) {
      NaTa_t_gates_m_forwardRate_r = 1.0920000076293945
    } else {
      NaTa_t_gates_m_forwardRate_r = 0
    }
  }
  NaTa_t_gates_m_inf = NaTa_t_gates_m_forwardRate_r * (NaTa_t_gates_m_forwardRate_r + NaTa_t_gates_m_reverseRate_r)^-1
  NaTa_t_gates_m_tau = (2.9528825283050537 * (NaTa_t_gates_m_forwardRate_r + NaTa_t_gates_m_reverseRate_r))^-1
  NaTa_t_gates_h_reverseRate_x = 0.16666666666666666 * (66 + v)
  if (NaTa_t_gates_h_reverseRate_x != 0) {
    NaTa_t_gates_h_reverseRate_r = 0.09000000357627869 * NaTa_t_gates_h_reverseRate_x * (1 + -1 * exp(-1 * NaTa_t_gates_h_reverseRate_x))^-1
  } else {
    if (NaTa_t_gates_h_reverseRate_x == 0) {
      NaTa_t_gates_h_reverseRate_r = 0.09000000357627869
    } else {
      NaTa_t_gates_h_reverseRate_r = 0
    }
  }
  NaTa_t_gates_h_forwardRate_x = -0.16666666666666666 * (66 + v)
  if (NaTa_t_gates_h_forwardRate_x != 0) {
    NaTa_t_gates_h_forwardRate_r = 0.09000000357627869 * NaTa_t_gates_h_forwardRate_x * (1 + -1 * exp(-1 * NaTa_t_gates_h_forwardRate_x))^-1
  } else {
    if (NaTa_t_gates_h_forwardRate_x == 0) {
      NaTa_t_gates_h_forwardRate_r = 0.09000000357627869
    } else {
      NaTa_t_gates_h_forwardRate_r = 0
    }
  }
  NaTa_t_gates_h_inf = NaTa_t_gates_h_forwardRate_r * (NaTa_t_gates_h_forwardRate_r + NaTa_t_gates_h_reverseRate_r)^-1
  NaTa_t_gates_h_tau = (2.9528825283050537 * (NaTa_t_gates_h_forwardRate_r + NaTa_t_gates_h_reverseRate_r))^-1
  Im_gates_m_forwardRate_r = 0.0032999999821186066 * exp(0.1 * (35 + v))
  Im_gates_m_reverseRate_r = 0.0032999999821186066 * exp(-0.1 * (35 + v))
  Im_gates_m_inf = Im_gates_m_forwardRate_r * (Im_gates_m_forwardRate_r + Im_gates_m_reverseRate_r)^-1
  Im_gates_m_tau = (2.9528825283050537 * (Im_gates_m_forwardRate_r + Im_gates_m_reverseRate_r))^-1
  Im_gates_m_q' = (Im_gates_m_inf + -1 * Im_gates_m_q) * Im_gates_m_tau^-1
  NaTa_t_gates_h_q' = (NaTa_t_gates_h_inf + -1 * NaTa_t_gates_h_q) * NaTa_t_gates_h_tau^-1
  NaTa_t_gates_m_q' = (NaTa_t_gates_m_inf + -1 * NaTa_t_gates_m_q) * NaTa_t_gates_m_tau^-1
  SK_E2_gates_z_q' = SK_E2_gates_z_steadyState_x + -1 * SK_E2_gates_z_q
  SKv3_1_gates_m_q' = (SKv3_1_gates_m_steadyState_x + -1 * SKv3_1_gates_m_q) * SKv3_1_gates_m_timeCourse_t^-1
}

BREAKPOINT {
  SOLVE dstate METHOD cnexp
  LOCAL NaTa_t_gates_m_fcond, NaTa_t_fopen0, NaTa_t_g, g_na, Im_g, SK_E2_g, SKv3_1_g, g_k

  NaTa_t_gates_m_fcond = NaTa_t_gates_m_q * NaTa_t_gates_m_q * NaTa_t_gates_m_q
  NaTa_t_fopen0 = NaTa_t_gates_h_q * NaTa_t_gates_m_fcond
  NaTa_t_g = 0.02129999923706055 * NaTa_t_fopen0
  g_na = NaTa_t_g
  Im_g = 0.00006750000268220902 * Im_gates_m_q
  SK_E2_g = 0.0012000000476837158 * SK_E2_gates_z_q
  SKv3_1_g = 0.00026100000739097596 * SKv3_1_gates_m_q
  g_k = Im_g + SK_E2_g + SKv3_1_g
  i = 0.00005889999866485596 * (90 + v)
  ik = g_k * (v + -1 * ek)
  ina = g_na * (v + -1 * ena)
}

