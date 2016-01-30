NEURON {
	POINT_PROCESS normrand
	RANGE del, dur, i
	RANGE tau_rise, tau_fall, t0, Imax
	RANGE interval, j, k, cnt, flg
	RANGE nStim, Imax2
	RANGE norm
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
	interval = 300 (ms)
	Imax2 = 15000 (nA/cm2)
}
ASSIGNED {
    i (nA)
    a (cm2)
    
    cnt
    flg
    j
    k
    nStim 
    norm
}

INITIAL {
	i = 0
	cnt = 0
	j = 0
	k = 0
	flg = 0
}

BREAKPOINT {
	at_time(del)
	at_time(del+dur)
	norm = normrand(0,1)
	i=1
}

FUNCTION stim1(t){
    a = 10^-8 * area
    stim1 = Imax*(1-exp(-(t)/tau_rise)) * a
}
