COMMENT
Since this is an electrode current, positive values of i depolarize the cell
and in the presence of the extracellular mechanism there will be a change
in vext since i is not a transmembrane current but a current injected
directly to the inside of the cell.
ENDCOMMENT

NEURON {
	POINT_PROCESS intermitStimGaus
	RANGE del, dur, i
	RANGE tau_rise, tau_fall, t0, Imax
	RANGE interval, j, k, cnt, flg
	RANGE nStim,Imax2
	
	RANGE forseed, stdev, average,temp,sigma_o
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
	
	stdev = 1.0
	average = 0.0
	forseed = 0
	
	sigma_o = 0.09
	
}
ASSIGNED {
    i  (nA)
    i1 (nA)
    a (cm2)
    
    cnt
    flg
    j
    k
    nStim
    v1
    v2
    s
    temp
    
    counter 
}

INITIAL {
    i = 0
    cnt = 0
    j = 0
    k = 0
    flg = 0
    counter = 0

    VERBATIM
    /*printf("forseed is %lf\n",forseed);*/
    srand((unsigned)time(NULL)+forseed);
    /*srand(25525);*/
    ENDVERBATIM
}

BREAKPOINT {
	at_time(del)
	at_time(del+dur)
	
	VERBATIM
	/*printf("%lf\t",t);*/
	ENDVERBATIM
	
	
	if(k == nStim){
	    Imax = Imax2
	}
	
	if(counter == 50){
	    VERBATIM
	    do {
		v1 =  2 * ((double) rand() / RAND_MAX) - 1;
		v2 =  2 * ((double) rand() / RAND_MAX) - 1;
		s = v1 * v1 + v2 * v2;
	    } while (s >= 1 || s == 0);
	    
	    s = sqrt( (-2 * log(s)) / s );
	    
	    temp = v1 * s;
	    temp = (stdev * temp) + average;
	    /*printf("%lf",temp);*/
	    ENDVERBATIM
	    counter = 0
	}

	if(t < del + t0 + interval * j && t >= del + interval * j) {
	    i1 = stim1(t-del-interval*j)
	    i =  i1*(1.0 + sigma_o*temp)
	    cnt = 0
	    k = j
	}else if(t>= del + t0 + interval * k){
	    i1 = stim1(t0)*exp(-(t-t0-del-interval*k)/tau_fall)
	    i =  i1*(1.0 + sigma_o*temp)
	    cnt = cnt + 1
	    if(cnt == 1){
		flg = 1
	    }
	}else{
	    i = 0
	}
	counter = counter + 1
	if(flg == 1){
	    j = j + 1
	    flg = 0
	}
}

FUNCTION stim1(t){
    a = 10^-8 * area
    stim1 = Imax*(1-exp(-(t)/tau_rise)) * a
}
