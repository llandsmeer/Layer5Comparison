TITLE Mod file for component: Component(id=SK_E2 type=ionChannelHH)

COMMENT

    This NEURON file has been generated by org.neuroml.export (see https://github.com/NeuroML/org.neuroml.export)
         org.neuroml.export  v1.9.0
         org.neuroml.model   v1.9.0
         jLEMS               v0.10.7

ENDCOMMENT

NEURON {
    SUFFIX SK_E2
    USEION ca READ cai,cao VALENCE 2
    USEION k WRITE ik VALENCE 1 ? Assuming valence = 1; TODO check this!!
    
    RANGE gion                           
    RANGE gmax                              : Will be changed when ion channel mechanism placed on cell!
    RANGE conductance                       : parameter
    
    RANGE g                                 : exposure
    
    RANGE fopen                             : exposure
    RANGE z_instances                       : parameter
    
    RANGE z_tau                             : exposure
    
    RANGE z_inf                             : exposure
    
    RANGE z_rateScale                       : exposure
    
    RANGE z_fcond                           : exposure
    RANGE z_timeCourse_TIME_SCALE           : parameter
    RANGE z_timeCourse_VOLT_SCALE           : parameter
    RANGE z_timeCourse_CONC_SCALE           : parameter
    
    RANGE z_timeCourse_t                    : exposure
    RANGE z_steadyState_TIME_SCALE          : parameter
    RANGE z_steadyState_VOLT_SCALE          : parameter
    RANGE z_steadyState_CONC_SCALE          : parameter
    
    RANGE z_steadyState_x                   : exposure
    RANGE z_timeCourse_V                    : derived variable
    RANGE z_timeCourse_ca_conc              : derived variable
    RANGE z_steadyState_V                   : derived variable
    RANGE z_steadyState_ca_conc             : derived variable
    RANGE z_tauUnscaled                     : derived variable
    RANGE conductanceScale                  : derived variable
    RANGE fopen0                            : derived variable
    
}

UNITS {
    
    (nA) = (nanoamp)
    (uA) = (microamp)
    (mA) = (milliamp)
    (A) = (amp)
    (mV) = (millivolt)
    (mS) = (millisiemens)
    (uS) = (microsiemens)
    (molar) = (1/liter)
    (kHz) = (kilohertz)
    (mM) = (millimolar)
    (um) = (micrometer)
    (umol) = (micromole)
    (S) = (siemens)
    
}

PARAMETER {
    
    gmax = 0  (S/cm2)                       : Will be changed when ion channel mechanism placed on cell!
    
    conductance = 1.0E-5 (uS)
    z_instances = 1 
    z_timeCourse_TIME_SCALE = 1 (ms)
    z_timeCourse_VOLT_SCALE = 1 (mV)
    z_timeCourse_CONC_SCALE = 1000000 (mM)
    z_steadyState_TIME_SCALE = 1 (ms)
    z_steadyState_VOLT_SCALE = 1 (mV)
    z_steadyState_CONC_SCALE = 1000000 (mM)
}

ASSIGNED {
    
    gion   (S/cm2)                          : Transient conductance density of the channel? Standard Assigned variables with ionChannel
    v (mV)
    celsius (degC)
    temperature (K)
    ek (mV)
    
    cai (mM)
    
    cao (mM)
    
    
    z_timeCourse_V                         : derived variable
    
    z_timeCourse_ca_conc                   : derived variable
    
    z_timeCourse_t (ms)                    : derived variable
    
    z_steadyState_V                        : derived variable
    
    z_steadyState_ca_conc                  : derived variable
    
    z_steadyState_x                        : derived variable
    
    z_rateScale                            : derived variable
    
    z_fcond                                : derived variable
    
    z_inf                                  : derived variable
    
    z_tauUnscaled (ms)                     : derived variable
    
    z_tau (ms)                             : derived variable
    
    conductanceScale                       : derived variable
    
    fopen0                                 : derived variable
    
    fopen                                  : derived variable
    
    g (uS)                                 : derived variable
    rate_z_q (/ms)
    
}

STATE {
    z_q  
    
}

INITIAL {
    ek = -85.0
    
    temperature = celsius + 273.15
    
    rates(v)
    rates(v) ? To ensure correct initialisation.
    
    z_q = z_inf
    
}

BREAKPOINT {
    
    SOLVE states METHOD cnexp
    
    ? DerivedVariable is based on path: conductanceScaling[*]/factor, on: Component(id=SK_E2 type=ionChannelHH), from conductanceScaling; null
    ? Path not present in component, using factor: 1
    
    conductanceScale = 1 
    
    ? DerivedVariable is based on path: gates[*]/fcond, on: Component(id=SK_E2 type=ionChannelHH), from gates; Component(id=z type=gateHHtauInf)
    ? multiply applied to all instances of fcond in: <gates> ([Component(id=z type=gateHHtauInf)]))
    fopen0 = z_fcond ? path based, prefix = 
    
    fopen = conductanceScale  *  fopen0 ? evaluable
    g = conductance  *  fopen ? evaluable
    gion = gmax * fopen 
    
    ik = gion * (v - ek)
    
}

DERIVATIVE states {
    rates(v)
    z_q' = rate_z_q 
    
}

PROCEDURE rates(v) {
    LOCAL caConc
    
    caConc = cai
    
    z_timeCourse_V = v /  z_timeCourse_VOLT_SCALE ? evaluable
    z_timeCourse_ca_conc = caConc /  z_timeCourse_CONC_SCALE ? evaluable
    z_timeCourse_t = 1.0  *  z_timeCourse_TIME_SCALE ? evaluable
    z_steadyState_V = v /  z_steadyState_VOLT_SCALE ? evaluable
    z_steadyState_ca_conc = caConc /  z_steadyState_CONC_SCALE ? evaluable
    z_steadyState_x = 1/(1+(4.3e-10/ z_steadyState_ca_conc )^4.8) ? evaluable
    ? DerivedVariable is based on path: q10Settings[*]/q10, on: Component(id=z type=gateHHtauInf), from q10Settings; null
    ? Path not present in component, using factor: 1
    
    z_rateScale = 1 
    
    z_fcond = z_q ^ z_instances ? evaluable
    ? DerivedVariable is based on path: steadyState/x, on: Component(id=z type=gateHHtauInf), from steadyState; Component(id=null type=SK_E2_z_inf_inf)
    z_inf = z_steadyState_x ? path based, prefix = z_
    
    ? DerivedVariable is based on path: timeCourse/t, on: Component(id=z type=gateHHtauInf), from timeCourse; Component(id=null type=SK_E2_z_tau_tau)
    z_tauUnscaled = z_timeCourse_t ? path based, prefix = z_
    
    z_tau = z_tauUnscaled  /  z_rateScale ? evaluable
    
     
    
     
    
     
    
     
    
     
    
     
    
     
    
     
    
     
    
     
    
     
    
     
    rate_z_q = ( z_inf  -  z_q ) /  z_tau ? Note units of all quantities used here need to be consistent!
    
     
    
     
    
     
    
}

