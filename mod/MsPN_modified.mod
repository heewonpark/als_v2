TITLE  Belmabrouk et al. 2011
: All ion channels used in Belmabrouk et al.2011 Manduca Sexta Projection Neuron Model
: Na+, K, Ca_T, sk, A and Leakage

: modified 2015.12.24 by Heewon Park.

NEURON {
    SUFFIX MsPN
    NONSPECIFIC_CURRENT il
    USEION ca READ cai, cao WRITE ica
    USEION k WRITE ik
    USEION na WRITE ina
    RANGE ina, ik, ica, iA, isk, il
    RANGE gnabar, ena, m_inf, a_m, v_m, ena_fixed                             : fast sodium
    RANGE gkdrbar, ek, W_inf, tau_W, ikD, lambda, sigma, a_W, v_W, ek_fixed   : delayed K rectifier
    RANGE gl, el                                                              : leak
    RANGE gcatbar, eca, X, X_inf, tau_X, a_X, v_X                             : T-type ca current
    RANGE gskbar, ek, isk, q_inf, C_gamma, tau_sk, a_sk                       : ca dependent SK current
    RANGE A_inf, B, B_inf, tau_B, gAbar, a_A, a_B, v_A, v_B                   : A(K) current
    RANGE CaM :Cai for Measurement
}


UNITS {
    (mA) = (milliamp)
    (mV) = (millivolt)
    (S)  = (siemens)
    (molar) = (1/liter)
    (mM)	= (millimolar)
    (nM)        = (nanomolar)
    FARADAY = (faraday) (coulomb)  :units are really coulombs/mole
    PI	= (pi) (1)
}

PARAMETER {
    R = 8.31441 (Gas constant)
    T 		(Absolute temp)
    celsius		(degC)
    
    : Fast Na channel
    gnabar   = 120e-3 (S/cm2):49e-3 (S/cm2) 
    a_m = 0.065
    v_m = -31 (mV)
    ena_fixed = 55 (mV)
    
    : delayed K rectifier 
    gkdrbar  = 5e-3 (S/cm2):57e-3	(S/cm2)
    sigma = 1 (1)
    a_W = 0.055
    v_W = -46 (mV)
    ek_fixed = -70 (mV)
    lambda = 0.05

    : Leakage current
    gl	= 0.3e-3 (S/cm2):0.35e-3	(S/cm2)
    el	= -50	(mV)
    
    : T-type ca current
    gcatbar   = 0.1e-3 (S/cm2):5e-3 (S/cm2)  
    tau_X = 50 (ms)
    a_X = 0.071
    v_X = -10 (mV)

    : sk current (Ca dependent K current)
    gskbar   = 2e-3 (S/cm2) :1e-3 (S/cm2) 
    C_gamma = 113e-6(mM)
    tau_sk = 250 (ms)
    a_sk = 0.9 (1)
    
    : A(K)
    gAbar = 22e-3 (S/cm2)
    tau_B = 20 (ms)
    a_A = 0.02
    a_B = -0.1
    v_A = -20 (mV)
    v_B = -70 (mV)
}

ASSIGNED {
    v	(mV)
    ina	(mA/cm2)
    ik	(mA/cm2) 
    ikD	(mA/cm2)   
    isk	(mA/cm2)  
    ica	(mA/cm2) 
    il	(mA/cm2)
    iA  (mA/cm2)
    
    :Fast Na
    m_inf
    ena		(mV)
    
    :K rectifier
    W_inf
    tau_W	(ms)
    ek		(mV) := -90
    
    :T-type ca current
    eca		(mV)   :calc from Nernst
    X_inf

    :AHP (Ca dependent K current)
    q_inf	(mM)

    :k
    A_inf
    B_inf

    :cai (mM)
    CaM
}

STATE {
    W 
    cai (mM) <1e-10>
    cao (mM) <1e-10>
    
    X
    B
}


BREAKPOINT {
    SOLVE states METHOD cnexp
    
    T = 273 + celsius - 9.5
    
    ina = gnabar * m_inf*m_inf*m_inf*(1-W) * (v - ena)
   
    ikD = gkdrbar * (W/sigma)^4 * (v - ek)
    isk = gskbar *q_inf * q_inf * (v - ek)
    iA  = gAbar *A_inf * B * (v-ek)
    ik  = ikD + isk + iA

    ica = gcatbar * X * (v-eca)
    il  = gl * (v - el)
}

DERIVATIVE states {   
    evaluate_fct(v)
    W' = (W_inf - W)/tau_W
    X' = (X_inf - X)/tau_X
    :(Ica mA/cm2)*(area um2)*(1e-8 cm2/um2)*(1e-3 A/mA)*(1/(2*F) mol/C)*(1e-3 sec/msec)*(1e3 mMol/mol)(1/volume 1/L)=(mM/msec)
    :cai' = caGain*(-ica*area*1e-11/(2*FARADAY*vol) - kca*cai)
    B' = (B_inf - B)/tau_B
    CaM = cai
}

UNITSOFF

INITIAL {
    evaluate_fct(v)
    W = W_inf   
    X = X_inf
    B = B_inf
}

PROCEDURE evaluate_fct(v(mV)) {     
    m_inf = 1/(1+exp(-2*a_m*(v-v_m)))
    W_inf = 1/(1+exp(-2*a_W*(v-v_W)))
    tau_W = 1/(lambda*(exp(a_W*(v-v_W))+exp(-a_W*(v-v_W))))
    X_inf = 1/(1+exp(-2*a_X*(v-v_X)))

    :q_inf = 1/(1+exp(-1.120-2.508*log((cai-C_gamma)/50)))
    q_inf = 1/(1+exp(-1.120-2.508 * llog((cai-C_gamma)/0.000050)))
    A_inf = 1/(1+exp(-2*a_A*(v-v_A)))
    B_inf = 1/(1+exp(-2*a_B*(v-v_B)))
}

FUNCTION llog(x){
    if (x<1e-3) {
        llog = -7
    }else{
        llog= log(x)
    }
}
UNITSON