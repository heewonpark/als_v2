TITLE Slow Ca-dependent potassium current
:IAHP.mod is based on belmabrouk et al 2011
:by park

:
:   Ca++ dependent K+ current IC responsible for slow AHP
:   Differential equations
:
:   Model based on a first order kinetic scheme
:
:      <closed> + n cai <-> <open>	(alpha,beta)
:
:   Following this model, the activation fct will be half-activated at 
:   a concentration of Cai = (beta/alpha)^(1/n) = cac (parameter)
:
:   The mod file is here written for the case n=2 (2 binding sites)
:   ---------------------------------------------
:
:   This current models the "slow" IK[Ca] (IAHP): 
:      - potassium current
:      - activated by intracellular calcium
:      - NOT voltage dependent
:
:   A minimal value for the time constant has been added
:
:   Ref: Destexhe et al., J. Neurophysiology 72: 803-818, 1994.
:   See also: http://www.cnl.salk.edu/~alain , http://cns.fmed.ulaval.ca
:

INDEPENDENT {t FROM 0 TO 1 WITH 1 (ms)}

NEURON {
    SUFFIX IAHP2debug
    USEION k WRITE ik
    USEION ca READ cai,ica
    RANGE gahpbar, q, channel_flow, ctau
    RANGE eahp
}

UNITS {
    (mA) = (milliamp)
    (mV) = (millivolt)
    (molar) = (1/liter)
    (mM) = (millimolar)
    (S)  = (siemens)
}

PARAMETER {
    v		(mV)
    gahpbar = 0.004 (S/cm2)
    eahp    = -140 (mV)
    ctau    = 0.0000125 (1/ms)
}

STATE {
    cai (mM) <1e-10>
}

ASSIGNED {
    ica (mA/cm2)
    ik	(mA/cm2)
    q
}

BREAKPOINT { 
    q = cai / (30 + cai)
    ik = gahpbar * q * (v - eahp)
    VERBATIM
    printf("IAHP2 cai:%.10lf ik:%.10lf\t",cai,ik);
    ENDVERBATIM
}
