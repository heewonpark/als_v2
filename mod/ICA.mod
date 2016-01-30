TITLE calcium current
:
:   Ca++ current responsible for low threshold spikes (LTS)
:   RETICULAR THALAMUS
:   Differential equations
:
:   Model of Huguenard & McCormick, J Neurophysiol 68: 1373-1383, 1992.
:   The kinetics is described by standard equations (NOT GHK)
:   using a m2h format, according to the voltage-clamp data
:   (whole cell patch clamp) of Huguenard & Prince, J Neurosci.
:   12: 3804-3817, 1992.  The model was introduced in Destexhe et al.
:   J. Neurophysiology 72: 803-818, 1994.
:   See http://www.cnl.salk.edu/~alain , http://cns.fmed.ulaval.ca
:
:    - Kinetics adapted to fit the T-channel of reticular neuron
:    - Q10 changed to 5 and 3
:    - Time constant tau_h fitted from experimental data
:    - shift parameter for screening charge
:
:   ACTIVATION FUNCTIONS FROM EXPERIMENTS (NO CORRECTION)
:
:   Reversal potential taken from Nernst Equation
:
:   Written by Alain Destexhe, Salk Institute, Sept 18, 1992
:

INDEPENDENT {t FROM 0 TO 1 WITH 1 (ms)}

NEURON {
    SUFFIX ICA
    USEION ca READ eca WRITE ica
    RANGE gcabar, s_inf
}

UNITS {
    (mV) =	(millivolt)
    (S)  =  (siemens)
}

PARAMETER {
    v		(mV)
    eca	        = 120	(mV)
    gcabar	= 0.005 (S/cm2)
}


ASSIGNED {
    ica	(mA/cm2)
    s_inf (1)
}

BREAKPOINT {
    s_inf = 1/(1+exp(-(v+25)/5))
    ica = gcabar * s_inf * (v-eca)
}