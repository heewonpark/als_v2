COMMENT
Since this is an electrode current, positive values of i depolarize the cell
and in the presence of the extracellular mechanism there will be a change
in vext since i is not a transmembrane current but a current injected
directly to the inside of the cell.
ENDCOMMENT

NEURON {
	POINT_PROCESS intermitStimNoise
	RANGE del, dur, i
	RANGE tau_rise, tau_fall, t0, Imax
	RANGE interval, j, k, cnt, flg
	RANGE nStim, Imax2
	
	RANGE norm, seed
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
    i1 (nA)
    a (cm2)
    
    cnt
    flg
    j
    k
    nStim 
    
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

	if(k == nStim){
	    Imax = Imax2
	}
	
	if(t < del + t0 + interval * j && t >= del + interval * j) {
	    i1 = stim1(t-del-interval*j)
	    i = i1 * (1 + 0.001*normrand(0,1))
	    cnt = 0
	    k = j
	}else if(t>= del + t0 + interval * k){
	    i1 = stim1(t0)*exp(-(t-t0-del-interval*k)/tau_fall)
	    i = i1 * (1 + 0.001*normrand(0,1))
	    cnt = cnt + 1
	    if(cnt == 1){
		flg = 1
	    }
	}else{
	    i = 0
	}

	if(flg == 1){
	    j = j + 1
	    flg = 0
	}
}

FUNCTION stim1(t){
    a = 10^-8 * area
    stim1 = Imax*(1-exp(-(t)/tau_rise)) * a
}
