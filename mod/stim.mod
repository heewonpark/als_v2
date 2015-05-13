COMMENT
Since this is an electrode current, positive values of i depolarize the cell
and in the presence of the extracellular mechanism there will be a change
in vext since i is not a transmembrane current but a current injected
directly to the inside of the cell.
ENDCOMMENT

NEURON {
	POINT_PROCESS Stim
	RANGE del, dur, i
	RANGE tau_rise, tau_fall, t0, Imax

	ELECTRODE_CURRENT i
}
UNITS {
	:(mA) = (milliamp)
	(nA) = (nanoamp)
}

PARAMETER {
	del (ms)
	dur (ms)	<0,1e9>
	amp (nA)
	
	Imax = 15000 (nA/cm2)
	tau_rise = 5 (ms)
	t0 = 50 (ms)
	tau_fall = 4000 (ms)
}
ASSIGNED {
    i (nA)
    a (cm2)
}

INITIAL {
	i = 0
}

BREAKPOINT {
	at_time(del)
	at_time(del+dur)
	
	if (t < del + t0 && t >= del) {
	    i = stim1(t)
	}else if(t>= del + t0){
	    i = stim1(del+t0)*exp(-(t-t0-del)/tau_fall)
	}else{
	    i = 0
	}
}

FUNCTION stim1(t){
    a = 10^-8 * area
    stim1 = Imax*(1-exp(-(t-del)/tau_rise)) * a
}
