TITLE minimal model of GABAa receptors
:GABAa model is based on Belmabrouk et al 2011
:original file is from http://senselab.med.yale.edu/ModelDB/ShowModel.cshtml?model=3670&file=\NTW_NEW\gabaa.mod
:By Heewon Park

COMMENT
-----------------------------------------------------------------------------

	Minimal kinetic model for GABA-A receptors
	==========================================

  Model of Destexhe, Mainen & Sejnowski, 1994:

	(closed) + T <-> (open)

  The simplest kinetics are considered for the binding of transmitter (T)
  to open postsynaptic receptors.   The corresponding equations are in
  similar form as the Hodgkin-Huxley model:

	dr/dt = alpha * [T] * (1-r) - beta * r

	I = gmax * [open] * (V-Erev)

  where [T] is the transmitter concentration and r is the fraction of 
  receptors in the open form.

  If the time course of transmitter occurs as a pulse of fixed duration,
  then this first-order model can be solved analytically, leading to a very
  fast mechanism for simulating synaptic currents, since no differential
  equation must be solved (see Destexhe, Mainen & Sejnowski, 1994).

-----------------------------------------------------------------------------

  Based on voltage-clamp recordings of GABAA receptor-mediated currents in rat
  hippocampal slices (Otis and Mody, Neuroscience 49: 13-32, 1992), this model
  was fit directly to experimental recordings in order to obtain the optimal
  values for the parameters (see Destexhe, Mainen and Sejnowski, 1996).

-----------------------------------------------------------------------------

  This mod file includes a mechanism to describe the time course of transmitter
  on the receptors.  The time course is approximated here as a brief pulse
  triggered when the presynaptic compartment produces an action potential.
  The pointer "pre" represents the voltage of the presynaptic compartment and
  must be connected to the appropriate variable in oc.

-----------------------------------------------------------------------------

  See details in:

  Destexhe, A., Mainen, Z.F. and Sejnowski, T.J.  An efficient method for
  computing synaptic conductances based on a kinetic model of receptor binding
  Neural Computation 6: 10-14, 1994.  

  Destexhe, A., Mainen, Z.F. and Sejnowski, T.J.  Kinetic models of 
  synaptic transmission.  In: Methods in Neuronal Modeling (2nd edition; 
  edited by Koch, C. and Segev, I.), MIT press, Cambridge, 1998, pp. 1-25.

  (electronic copy available at http://cns.iaf.cnrs-gif.fr)

  Written by Alain Destexhe, Laval University, 1995
  27-11-2002: the pulse is implemented using a counter, which is more
       stable numerically (thanks to Yann LeFranc)

-----------------------------------------------------------------------------
ENDCOMMENT



INDEPENDENT {t FROM 0 TO 1 WITH 1 (ms)}

NEURON {
	POINT_PROCESS GABAa
	POINTER pre
	RANGE C, R, g, gmax, lastrelease, TimeCount, i
	RANGE gmax2
	NONSPECIFIC_CURRENT i
	GLOBAL T, Cdur, Alpha, GABAtau, Erev, Prethresh, Deadtime, Rinf, Rtau
}
UNITS {
	(nA) = (nanoamp)
	(mV) = (millivolt)
	(umho) = (micromho)
	(mM) = (milli/liter)
	(S) = (siemens)

}

PARAMETER {
	dt		(ms)
	
	Cdur	= 1	(ms)		: transmitter duration (rising phase)
	Alpha	= 6.25	(/ms mM)	: forward (binding) rate
	GABAtau	= 10	(ms)		: backward (unbinding) rate
	Erev	= -75	(mV)		: reversal potential
	Prethresh = 0 			: voltage level nec for release
	Deadtime = 1	(ms)		: mimimum time between release events
	gmax	=0.00008	(S/cm2)		: maximum conductance
}


ASSIGNED {
	v		(mV)		: postsynaptic voltage
	i 		(nA)		: current = g*(v - Erev)
	g 		(S/cm2)		: conductance
	:C		(mM)		: transmitter concentration

	:R0				: open channels at start of release
	:R1				: open channels at end of release
	Rinf				: steady state channels open
	Rtau		(ms)		: time constant of channel binding
	pre 				: pointer to presynaptic variable
	:lastrelease	(ms)		: time of last spike
	:TimeCount	(ms)		: time counter
	
	T		(mM)		: transmitter concentration
	
	a (cm2) : area
	gmax2 (S)
}

STATE {
    R				: fraction of open channels
}

INITIAL {
    :R = 0
}

BREAKPOINT {
	SOLVE states METHOD cnexp
	a = 10^-8 * area
	gmax2 = gmax * a
	g = gmax2 * R
	i = g*(v - Erev)
}
DERIVATIVE states {
    release()
    Rinf = T*Alpha / (T*Alpha + 1/GABAtau)
    Rtau = 1 / ((Alpha * T) + 1/GABAtau)
        
    R' = (Rinf-R)/Rtau
}
PROCEDURE release(){
    T = 1/(1+exp(-pre/2))
}

NET_RECEIVE(weight(us)){
}