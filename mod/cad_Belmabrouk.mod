:*******************************************************************************************************
: cad.mod was modified by Park
: Refered 
: Roper P, Callaway J, Shevchenko T, TeruyamaR, Armstrong W
: AHP's, HAP's and DAP's: How Potassium Currents Regulate the Excitability of Rat Supraoptic Neurones
: Journal of Computational Neuroscience
: November 2003, Volume 15, Issue 3, pp 367-389
: 
: And also,
: Belmabrouk, Hana Nowotny, Thomas Rospars, Jean-Pierre Martinez, Dominique Martinez 2011
: Interaction of cellular and network mechanisms for efficient pheromone coding in moths
:*******************************************************************************************************


: original cad.mod file : https://senselab.med.yale.edu/ModelDB/ShowModel.cshtml?model=147514&file=/dendritic_complexity/cad.mod
: 26 Ago 2002 Modification of original channel to allow variable time step and to correct an initialization error.
: Done by Michael Hines(michael.hines@yale.e) and Ruggero Scorcioni(rscorcio@gmu.edu) at EU Advance Course in Computational Neuroscience. Obidos, Portugal

TITLE decay of internal calcium concentration
:
: Internal calcium concentration due to calcium currents and pump.
: Differential equations.
:
: Simple model of ATPase pump with 3 kinetic constants (Destexhe 92)
:     Cai + P <-> CaP -> Cao + P  (k1,k2,k3)
: A Michaelis-Menten approximation is assumed, which reduces the complexity
: of the system to 2 parameters: 
:       kt = <tot enzyme concentration> * k3  -> TIME CONSTANT OF THE PUMP
:	kd = k2/k1 (dissociation constant)    -> EQUILIBRIUM CALCIUM VALUE
: The values of these parameters are chosen assuming a high affinity of 
: the pump to calcium and a low transport capacity (cfr. Blaustein, 
: TINS, 11: 438, 1988, and references therein).  
:
: Units checked using "modlunit" -> factor 10000 needed in ca entry
:
: VERSION OF PUMP + DECAY (decay can be viewed as simplified buffering)
:
: All variables are range variables
:
:
: This mechanism was published in:  Destexhe, A. Babloyantz, A. and 
: Sejnowski, TJ.  Ionic mechanisms for intrinsic slow oscillations in
: thalamic relay neurons. Biophys. J. 65: 1538-1552, 1993)
:
: Written by Alain Destexhe, Salk Institute, Nov 12, 1992
:

INDEPENDENT {t FROM 0 TO 1 WITH 1 (ms)}

NEURON {
	SUFFIX cadyn
	USEION ca READ ica, cai WRITE cai
	RANGE ca
	GLOBAL depth,cainf,taur
}

UNITS {
	(molar) = (1/liter)			: moles do not appear in units
	(mM)	= (millimolar)
	(um)	= (micron)
	(mA)	= (milliamp)
	(msM)	= (ms mM)
	FARADAY = (faraday) (coulomb)
}


PARAMETER {
	depth	= .1	(um)		: depth of shell
	:taur	= 200	(ms)		: rate of calcium removal
	taur	= 250	(ms)
	:cainf	= 100e-6(mM)
	cainf	= 113e-6(mM)
	cai		(mM)
}

STATE {
	ca		(mM) <1e-5>
}

INITIAL {
	ca = cainf
	cai = ca
}

ASSIGNED {
	ica		(mA/cm2)
	drive_channel	(mM/ms)
}
	
BREAKPOINT {
	SOLVE state METHOD euler
}

DERIVATIVE state { 

	:drive_channel =  - (10000) * ica / (2 * FARADAY * depth)
	drive_channel = -0.9 * ica
	if (drive_channel <= 0.) { drive_channel = 0. }	: cannot pump inward

	ca' = drive_channel + (cainf-ca)/taur
	cai = ca
}