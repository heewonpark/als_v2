/* Created by Language version: 6.2.0 */
/* NOT VECTORIZED */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "scoplib_ansi.h"
#undef PI
#define nil 0
#include "md1redef.h"
#include "section.h"
#include "nrniv_mf.h"
#include "md2redef.h"
 
#if METHOD3
extern int _method3;
#endif

#if !NRNGPU
#undef exp
#define exp hoc_Exp
extern double hoc_Exp(double);
#endif
 
#define _threadargscomma_ /**/
#define _threadargs_ /**/
 
#define _threadargsprotocomma_ /**/
#define _threadargsproto_ /**/
 	/*SUPPRESS 761*/
	/*SUPPRESS 762*/
	/*SUPPRESS 763*/
	/*SUPPRESS 765*/
	 extern double *getarg();
 static double *_p; static Datum *_ppvar;
 
#define t nrn_threads->_t
#define dt nrn_threads->_dt
#define gnabar _p[0]
#define a_m _p[1]
#define v_m _p[2]
#define ena_fixed _p[3]
#define gkdrbar _p[4]
#define sigma _p[5]
#define a_W _p[6]
#define v_W _p[7]
#define ek_fixed _p[8]
#define lambda _p[9]
#define gl _p[10]
#define el _p[11]
#define kca _p[12]
#define vol _p[13]
#define caGain _p[14]
#define gcatbar _p[15]
#define tau_X _p[16]
#define a_X _p[17]
#define v_X _p[18]
#define gkcabar _p[19]
#define C_gamma _p[20]
#define tau_sk _p[21]
#define a_sk _p[22]
#define gA _p[23]
#define tau_B _p[24]
#define a_A _p[25]
#define a_B _p[26]
#define v_A _p[27]
#define v_B _p[28]
#define ina _p[29]
#define ik _p[30]
#define ikD _p[31]
#define ikAHP _p[32]
#define ica _p[33]
#define icaT _p[34]
#define ilk _p[35]
#define iA _p[36]
#define m_inf _p[37]
#define ena _p[38]
#define W_inf _p[39]
#define tau_W _p[40]
#define ek _p[41]
#define eca _p[42]
#define X_inf _p[43]
#define q_inf _p[44]
#define A_inf _p[45]
#define B_inf _p[46]
#define W _p[47]
#define X _p[48]
#define Csk _p[49]
#define B _p[50]
#define DW _p[51]
#define cai _p[52]
#define Dcai _p[53]
#define cao _p[54]
#define Dcao _p[55]
#define nai _p[56]
#define Dnai _p[57]
#define nao _p[58]
#define Dnao _p[59]
#define ki _p[60]
#define Dki _p[61]
#define ko _p[62]
#define Dko _p[63]
#define DX _p[64]
#define DCsk _p[65]
#define DB _p[66]
#define _g _p[67]
#define _ion_cai	*_ppvar[0]._pval
#define _ion_cao	*_ppvar[1]._pval
#define _ion_ica	*_ppvar[2]._pval
#define _ion_dicadv	*_ppvar[3]._pval
#define _style_ca	*((int*)_ppvar[4]._pvoid)
#define _ion_ki	*_ppvar[5]._pval
#define _ion_ko	*_ppvar[6]._pval
#define _ion_ik	*_ppvar[7]._pval
#define _ion_dikdv	*_ppvar[8]._pval
#define _ion_nai	*_ppvar[9]._pval
#define _ion_nao	*_ppvar[10]._pval
#define _ion_ina	*_ppvar[11]._pval
#define _ion_dinadv	*_ppvar[12]._pval
#define area	*_ppvar[13]._pval
 
#if MAC
#if !defined(v)
#define v _mlhv
#endif
#if !defined(h)
#define h _mlhh
#endif
#endif
 
#if defined(__cplusplus)
extern "C" {
#endif
 static int hoc_nrnpointerindex =  -1;
 /* external NEURON variables */
 extern double celsius;
 /* declaration of user functions */
 static void _hoc_evaluate_fct(void);
 static int _mechtype;
extern void _nrn_cacheloop_reg(int, int);
extern void hoc_register_prop_size(int, int, int);
extern void hoc_register_limits(int, HocParmLimits*);
extern void hoc_register_units(int, HocParmUnits*);
extern void nrn_promote(Prop*, int, int);
extern Memb_func* memb_func;
 extern void _nrn_setdata_reg(int, void(*)(Prop*));
 static void _setdata(Prop* _prop) {
 _p = _prop->param; _ppvar = _prop->dparam;
 }
 static void _hoc_setdata() {
 Prop *_prop, *hoc_getdata_range(int);
 _prop = hoc_getdata_range(_mechtype);
   _setdata(_prop);
 hoc_retpushx(1.);
}
 /* connect user functions to hoc names */
 static VoidFunc hoc_intfunc[] = {
 "setdata_GPeA", _hoc_setdata,
 "evaluate_fct_GPeA", _hoc_evaluate_fct,
 0, 0
};
 /* declare global and static user variables */
#define R R_GPeA
 double R = 8.31441;
#define T T_GPeA
 double T = 0;
 /* some parameters have upper and lower limits */
 static HocParmLimits _hoc_parm_limits[] = {
 0,0,0
};
 static HocParmUnits _hoc_parm_units[] = {
 "R_GPeA", "Gas",
 "T_GPeA", "Absolute",
 "gnabar_GPeA", "S/cm2",
 "v_m_GPeA", "mV",
 "ena_fixed_GPeA", "mV",
 "gkdrbar_GPeA", "S/cm2",
 "sigma_GPeA", "1",
 "v_W_GPeA", "mV",
 "ek_fixed_GPeA", "mV",
 "gl_GPeA", "S/cm2",
 "el_GPeA", "mV",
 "kca_GPeA", "1/ms",
 "vol_GPeA", "L",
 "gcatbar_GPeA", "S/cm2",
 "tau_X_GPeA", "ms",
 "v_X_GPeA", "mV",
 "gkcabar_GPeA", "S/cm2",
 "C_gamma_GPeA", "nM",
 "tau_sk_GPeA", "ms",
 "a_sk_GPeA", "1",
 "gA_GPeA", "S/cm2",
 "tau_B_GPeA", "ms",
 "v_A_GPeA", "mV",
 "v_B_GPeA", "mV",
 "Csk_GPeA", "nM",
 "ina_GPeA", "mA/cm2",
 "ik_GPeA", "mA/cm2",
 "ikD_GPeA", "mA/cm2",
 "ikAHP_GPeA", "mA/cm2",
 "ica_GPeA", "mA/cm2",
 "icaT_GPeA", "mA/cm2",
 "ilk_GPeA", "mA/cm2",
 "iA_GPeA", "mA/cm2",
 "ena_GPeA", "mV",
 "tau_W_GPeA", "ms",
 "ek_GPeA", "mV",
 "eca_GPeA", "mV",
 "q_inf_GPeA", "mM",
 0,0
};
 static double B0 = 0;
 static double Csk0 = 0;
 static double W0 = 0;
 static double X0 = 0;
 static double cao0 = 0;
 static double cai0 = 0;
 static double delta_t = 0.01;
 static double ko0 = 0;
 static double ki0 = 0;
 static double nao0 = 0;
 static double nai0 = 0;
 static double v = 0;
 /* connect global user variables to hoc */
 static DoubScal hoc_scdoub[] = {
 "R_GPeA", &R_GPeA,
 "T_GPeA", &T_GPeA,
 0,0
};
 static DoubVec hoc_vdoub[] = {
 0,0,0
};
 static double _sav_indep;
 static void nrn_alloc(Prop*);
static void  nrn_init(_NrnThread*, _Memb_list*, int);
static void nrn_state(_NrnThread*, _Memb_list*, int);
 static void nrn_cur(_NrnThread*, _Memb_list*, int);
static void  nrn_jacob(_NrnThread*, _Memb_list*, int);
 
static int _ode_count(int);
static void _ode_map(int, double**, double**, double*, Datum*, double*, int);
static void _ode_spec(_NrnThread*, _Memb_list*, int);
static void _ode_matsol(_NrnThread*, _Memb_list*, int);
 
#define _cvode_ieq _ppvar[14]._i
 /* connect range variables in _p that hoc is supposed to know about */
 static const char *_mechanism[] = {
 "6.2.0",
"GPeA",
 "gnabar_GPeA",
 "a_m_GPeA",
 "v_m_GPeA",
 "ena_fixed_GPeA",
 "gkdrbar_GPeA",
 "sigma_GPeA",
 "a_W_GPeA",
 "v_W_GPeA",
 "ek_fixed_GPeA",
 "lambda_GPeA",
 "gl_GPeA",
 "el_GPeA",
 "kca_GPeA",
 "vol_GPeA",
 "caGain_GPeA",
 "gcatbar_GPeA",
 "tau_X_GPeA",
 "a_X_GPeA",
 "v_X_GPeA",
 "gkcabar_GPeA",
 "C_gamma_GPeA",
 "tau_sk_GPeA",
 "a_sk_GPeA",
 "gA_GPeA",
 "tau_B_GPeA",
 "a_A_GPeA",
 "a_B_GPeA",
 "v_A_GPeA",
 "v_B_GPeA",
 0,
 "ina_GPeA",
 "ik_GPeA",
 "ikD_GPeA",
 "ikAHP_GPeA",
 "ica_GPeA",
 "icaT_GPeA",
 "ilk_GPeA",
 "iA_GPeA",
 "m_inf_GPeA",
 "ena_GPeA",
 "W_inf_GPeA",
 "tau_W_GPeA",
 "ek_GPeA",
 "eca_GPeA",
 "X_inf_GPeA",
 "q_inf_GPeA",
 "A_inf_GPeA",
 "B_inf_GPeA",
 0,
 "W_GPeA",
 "X_GPeA",
 "Csk_GPeA",
 "B_GPeA",
 0,
 0};
 extern Node* nrn_alloc_node_;
 static Symbol* _ca_sym;
 static Symbol* _k_sym;
 static Symbol* _na_sym;
 
extern Prop* need_memb(Symbol*);

static void nrn_alloc(Prop* _prop) {
	Prop *prop_ion;
	double *_p; Datum *_ppvar;
 	_p = nrn_prop_data_alloc(_mechtype, 68, _prop);
 	/*initialize range parameters*/
 	gnabar = 0.12;
 	a_m = 0.065;
 	v_m = -31;
 	ena_fixed = 55;
 	gkdrbar = 0.005;
 	sigma = 1;
 	a_W = 0.055;
 	v_W = -46;
 	ek_fixed = -70;
 	lambda = 0.05;
 	gl = 0.0003;
 	el = -50;
 	kca = 2;
 	vol = 3.355e-11;
 	caGain = 0.1;
 	gcatbar = 0.0001;
 	tau_X = 50;
 	a_X = 0.071;
 	v_X = -10;
 	gkcabar = 0.002;
 	C_gamma = 113;
 	tau_sk = 250;
 	a_sk = 0.9;
 	gA = 0.022;
 	tau_B = 20;
 	a_A = 0.02;
 	a_B = -0.1;
 	v_A = -20;
 	v_B = -70;
 	_prop->param = _p;
 	_prop->param_size = 68;
 	_ppvar = nrn_prop_datum_alloc(_mechtype, 15, _prop);
 	_prop->dparam = _ppvar;
 	/*connect ionic variables to this model*/
 	_ppvar[13]._pval = &nrn_alloc_node_->_area; /* diam */
 prop_ion = need_memb(_ca_sym);
 nrn_check_conc_write(_prop, prop_ion, 1);
 nrn_promote(prop_ion, 3, 0);
 	_ppvar[0]._pval = &prop_ion->param[1]; /* cai */
 	_ppvar[1]._pval = &prop_ion->param[2]; /* cao */
 	_ppvar[2]._pval = &prop_ion->param[3]; /* ica */
 	_ppvar[3]._pval = &prop_ion->param[4]; /* _ion_dicadv */
 	_ppvar[4]._pvoid = (void*)(&(prop_ion->dparam[0]._i)); /* iontype for ca */
 prop_ion = need_memb(_k_sym);
 nrn_promote(prop_ion, 1, 0);
 	_ppvar[5]._pval = &prop_ion->param[1]; /* ki */
 	_ppvar[6]._pval = &prop_ion->param[2]; /* ko */
 	_ppvar[7]._pval = &prop_ion->param[3]; /* ik */
 	_ppvar[8]._pval = &prop_ion->param[4]; /* _ion_dikdv */
 prop_ion = need_memb(_na_sym);
 nrn_promote(prop_ion, 1, 0);
 	_ppvar[9]._pval = &prop_ion->param[1]; /* nai */
 	_ppvar[10]._pval = &prop_ion->param[2]; /* nao */
 	_ppvar[11]._pval = &prop_ion->param[3]; /* ina */
 	_ppvar[12]._pval = &prop_ion->param[4]; /* _ion_dinadv */
 
}
 static void _initlists();
  /* some states have an absolute tolerance */
 static Symbol** _atollist;
 static HocStateTolerance _hoc_state_tol[] = {
 "Csk_GPeA", 1e-10,
 0,0
};
 static void _update_ion_pointer(Datum*);
 extern Symbol* hoc_lookup(const char*);
extern void _nrn_thread_reg(int, int, void(*f)(Datum*));
extern void _nrn_thread_table_reg(int, void(*)(double*, Datum*, Datum*, _NrnThread*, int));
extern void hoc_register_tolerance(int, HocStateTolerance*, Symbol***);
extern void _cvode_abstol( Symbol**, double*, int);

 void _pGPeA_fukuda_reg() {
	int _vectorized = 0;
  _initlists();
 	ion_reg("ca", -10000.);
 	ion_reg("k", -10000.);
 	ion_reg("na", -10000.);
 	_ca_sym = hoc_lookup("ca_ion");
 	_k_sym = hoc_lookup("k_ion");
 	_na_sym = hoc_lookup("na_ion");
 	register_mech(_mechanism, nrn_alloc,nrn_cur, nrn_jacob, nrn_state, nrn_init, hoc_nrnpointerindex, 0);
 _mechtype = nrn_get_mechtype(_mechanism[1]);
     _nrn_setdata_reg(_mechtype, _setdata);
     _nrn_thread_reg(_mechtype, 2, _update_ion_pointer);
  hoc_register_dparam_size(_mechtype, 15);
 	nrn_writes_conc(_mechtype, 0);
 	hoc_register_cvode(_mechtype, _ode_count, _ode_map, _ode_spec, _ode_matsol);
 	hoc_register_tolerance(_mechtype, _hoc_state_tol, &_atollist);
 	hoc_register_var(hoc_scdoub, hoc_vdoub, hoc_intfunc);
 	ivoc_help("help ?1 GPeA /home/park/code/neuron/al_V2/mod/x86_64/pGPeA_fukuda.mod\n");
 hoc_register_limits(_mechtype, _hoc_parm_limits);
 hoc_register_units(_mechtype, _hoc_parm_units);
 }
 static double FARADAY = 96485.3;
 static double PI = 3.14159;
static int _reset;
static char *modelname = "Belmabrouk et al. 2011";

static int error;
static int _ninits = 0;
static int _match_recurse=1;
static void _modl_cleanup(){ _match_recurse=1;}
static int evaluate_fct(double);
 
static int _ode_spec1(_threadargsproto_);
/*static int _ode_matsol1(_threadargsproto_);*/
 static int _slist1[5], _dlist1[5];
 static int states(_threadargsproto_);
 
/*CVODE*/
 static int _ode_spec1 () {_reset=0;
 {
   evaluate_fct ( _threadargscomma_ v ) ;
   DW = ( W_inf - W ) / tau_W ;
   DX = ( X_inf - X ) / tau_X ;
   Dcai = caGain * ( - ica * area * 1e-11 / ( 2.0 * FARADAY * vol ) - kca * cai ) ;
   DCsk = - a_sk * ica - ( Csk - C_gamma ) / tau_sk ;
   DB = ( B_inf - B ) / tau_B ;
   }
 return _reset;
}
 static int _ode_matsol1 () {
 evaluate_fct ( _threadargscomma_ v ) ;
 DW = DW  / (1. - dt*( ( ( ( - 1.0 ) ) ) / tau_W )) ;
 DX = DX  / (1. - dt*( ( ( ( - 1.0 ) ) ) / tau_X )) ;
 Dcai = Dcai  / (1. - dt*( (caGain)*(( ( - (kca)*(1.0) ) )) )) ;
 DCsk = DCsk  / (1. - dt*( ( - ( ( 1.0 ) ) / tau_sk ) )) ;
 DB = DB  / (1. - dt*( ( ( ( - 1.0 ) ) ) / tau_B )) ;
 return 0;
}
 /*END CVODE*/
 static int states () {_reset=0;
 {
   evaluate_fct ( _threadargscomma_ v ) ;
    W = W + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / tau_W)))*(- ( ( ( W_inf ) ) / tau_W ) / ( ( ( ( - 1.0) ) ) / tau_W ) - W) ;
    X = X + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / tau_X)))*(- ( ( ( X_inf ) ) / tau_X ) / ( ( ( ( - 1.0) ) ) / tau_X ) - X) ;
    cai = cai + (1. - exp(dt*((caGain)*(( ( - (kca)*(1.0) ) )))))*(- ( (caGain)*(( ( ((- ica)*(area))*(1e-11) ) / ( 2.0 * FARADAY * vol ) )) ) / ( (caGain)*(( ( - (kca)*(1.0)) )) ) - cai) ;
    Csk = Csk + (1. - exp(dt*(( - ( ( 1.0 ) ) / tau_sk ))))*(- ( (- a_sk)*(ica) - ( ( ( - C_gamma ) ) ) / tau_sk ) / ( ( - ( ( 1.0 ) ) / tau_sk) ) - Csk) ;
    B = B + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / tau_B)))*(- ( ( ( B_inf ) ) / tau_B ) / ( ( ( ( - 1.0) ) ) / tau_B ) - B) ;
   }
  return 0;
}
 
static int  evaluate_fct (  double _lv ) {
   
/*VERBATIM*/
    /*if(v>400){*/
	/*printf("too high v is investigated!!\n");
	/*printf("time is %lf, v = %lf\n",t,v);*/
	/*printf("too large v (v= %lf) is detected at t=%lf\n",v,t);*/
	/*sleep(1);*/
	/*printf("before v = %lf\n",v);*/
	/*v = -65;*/
	/*printf("after v = %lf \n",v);*/
    /*}else if(v<-250){*/
	/*printf("too small v (v= %lf) is detected at t = %lf\n",v,t);*/
	/*v = -65;*/
    /*}*/
 m_inf = 1.0 / ( 1.0 + exp ( - 2.0 * a_m * ( _lv - v_m ) ) ) ;
   W_inf = 1.0 / ( 1.0 + exp ( - 2.0 * a_W * ( _lv - v_W ) ) ) ;
   tau_W = 1.0 / ( lambda * ( exp ( a_W * ( _lv - v_W ) ) + exp ( - a_W * ( _lv - v_W ) ) ) ) ;
   X_inf = 1.0 / ( 1.0 + exp ( - 2.0 * a_X * ( _lv - v_X ) ) ) ;
   if ( ( Csk - C_gamma ) < 0.00001 ) {
     Csk = C_gamma + 0.00001 ;
     }
   q_inf = 1.0 / ( 1.0 + exp ( - 1.120 - 2.508 * log ( ( Csk - C_gamma ) / 50.0 ) ) ) ;
   A_inf = 1.0 / ( 1.0 + exp ( - 2.0 * a_A * ( _lv - v_A ) ) ) ;
   B_inf = 1.0 / ( 1.0 + exp ( - 2.0 * a_B * ( _lv - v_B ) ) ) ;
    return 0; }
 
static void _hoc_evaluate_fct(void) {
  double _r;
   _r = 1.;
 evaluate_fct (  *getarg(1) );
 hoc_retpushx(_r);
}
 
static int _ode_count(int _type){ return 5;}
 
static void _ode_spec(_NrnThread* _nt, _Memb_list* _ml, int _type) {
   Datum* _thread;
   Node* _nd; double _v; int _iml, _cntml;
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _nd = _ml->_nodelist[_iml];
    v = NODEV(_nd);
  cai = _ion_cai;
  cao = _ion_cao;
  cai = _ion_cai;
  ki = _ion_ki;
  ko = _ion_ko;
  nai = _ion_nai;
  nao = _ion_nao;
     _ode_spec1 ();
   _ion_cai = cai;
   }}
 
static void _ode_map(int _ieq, double** _pv, double** _pvdot, double* _pp, Datum* _ppd, double* _atol, int _type) { 
 	int _i; _p = _pp; _ppvar = _ppd;
	_cvode_ieq = _ieq;
	for (_i=0; _i < 5; ++_i) {
		_pv[_i] = _pp + _slist1[_i];  _pvdot[_i] = _pp + _dlist1[_i];
		_cvode_abstol(_atollist, _atol, _i);
	}
 	_pv[2] = &(_ion_cai);
 }
 
static void _ode_matsol(_NrnThread* _nt, _Memb_list* _ml, int _type) {
   Datum* _thread;
   Node* _nd; double _v; int _iml, _cntml;
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _nd = _ml->_nodelist[_iml];
    v = NODEV(_nd);
  cai = _ion_cai;
  cao = _ion_cao;
  cai = _ion_cai;
  ki = _ion_ki;
  ko = _ion_ko;
  nai = _ion_nai;
  nao = _ion_nao;
 _ode_matsol1 ();
 }}
 extern void nrn_update_ion_pointer(Symbol*, Datum*, int, int);
 static void _update_ion_pointer(Datum* _ppvar) {
   nrn_update_ion_pointer(_ca_sym, _ppvar, 0, 1);
   nrn_update_ion_pointer(_ca_sym, _ppvar, 1, 2);
   nrn_update_ion_pointer(_ca_sym, _ppvar, 2, 3);
   nrn_update_ion_pointer(_ca_sym, _ppvar, 3, 4);
   nrn_update_ion_pointer(_k_sym, _ppvar, 5, 1);
   nrn_update_ion_pointer(_k_sym, _ppvar, 6, 2);
   nrn_update_ion_pointer(_k_sym, _ppvar, 7, 3);
   nrn_update_ion_pointer(_k_sym, _ppvar, 8, 4);
   nrn_update_ion_pointer(_na_sym, _ppvar, 9, 1);
   nrn_update_ion_pointer(_na_sym, _ppvar, 10, 2);
   nrn_update_ion_pointer(_na_sym, _ppvar, 11, 3);
   nrn_update_ion_pointer(_na_sym, _ppvar, 12, 4);
 }

static void initmodel() {
  int _i; double _save;_ninits++;
 _save = t;
 t = 0.0;
{
  B = B0;
  Csk = Csk0;
  W = W0;
  X = X0;
 {
   evaluate_fct ( _threadargscomma_ v ) ;
   W = W_inf ;
   X = X_inf ;
   Csk = C_gamma + 0.00001 ;
   B = B_inf ;
   }
  _sav_indep = t; t = _save;

}
}

static void nrn_init(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; double _v; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 v = _v;
  cai = _ion_cai;
  cao = _ion_cao;
  cai = _ion_cai;
  ki = _ion_ki;
  ko = _ion_ko;
  nai = _ion_nai;
  nao = _ion_nao;
 initmodel();
   _ion_cai = cai;
  nrn_wrote_conc(_ca_sym, (&(_ion_cai)) - 1, _style_ca);
  }}

static double _nrn_current(double _v){double _current=0.;v=_v;{ {
   T = 273.0 + celsius - 9.5 ;
   ina = gnabar * m_inf * m_inf * m_inf * ( 1.0 - W ) * ( v - ena ) ;
   ikD = gkdrbar * pow( ( W / sigma ) , 4.0 ) * ( v - ek ) ;
   ikAHP = gkcabar * ( v - ek ) * q_inf * q_inf ;
   iA = gA * A_inf * B * ( v - ek ) ;
   ik = ikD + ikAHP + iA ;
   ilk = gl * ( v - el ) ;
   ica = gcatbar * X * ( v - eca ) ;
   }
 _current += ilk;
 _current += ica;
 _current += ik;
 _current += ina;

} return _current;
}

static void nrn_cur(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; int* _ni; double _rhs, _v; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
  cai = _ion_cai;
  cao = _ion_cao;
  cai = _ion_cai;
  ki = _ion_ki;
  ko = _ion_ko;
  nai = _ion_nai;
  nao = _ion_nao;
 _g = _nrn_current(_v + .001);
 	{ double _dina;
 double _dik;
 double _dica;
  _dica = ica;
  _dik = ik;
  _dina = ina;
 _rhs = _nrn_current(_v);
  _ion_dicadv += (_dica - ica)/.001 ;
  _ion_dikdv += (_dik - ik)/.001 ;
  _ion_dinadv += (_dina - ina)/.001 ;
 	}
 _g = (_g - _rhs)/.001;
  _ion_ica += ica ;
  _ion_cai = cai;
  _ion_ik += ik ;
  _ion_ina += ina ;
#if CACHEVEC
  if (use_cachevec) {
	VEC_RHS(_ni[_iml]) -= _rhs;
  }else
#endif
  {
	NODERHS(_nd) -= _rhs;
  }
 
}}

static void nrn_jacob(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml];
#if CACHEVEC
  if (use_cachevec) {
	VEC_D(_ni[_iml]) += _g;
  }else
#endif
  {
     _nd = _ml->_nodelist[_iml];
	NODED(_nd) += _g;
  }
 
}}

static void nrn_state(_NrnThread* _nt, _Memb_list* _ml, int _type){
 double _break, _save;
Node *_nd; double _v; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
 _nd = _ml->_nodelist[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 _break = t + .5*dt; _save = t;
 v=_v;
{
  cai = _ion_cai;
  cao = _ion_cao;
  cai = _ion_cai;
  ki = _ion_ki;
  ko = _ion_ko;
  nai = _ion_nai;
  nao = _ion_nao;
 { {
 for (; t < _break; t += dt) {
 error =  states();
 if(error){fprintf(stderr,"at line 131 in file pGPeA_fukuda.mod:\n    \n"); nrn_complain(_p); abort_run(error);}
 
}}
 t = _save;
 }   _ion_cai = cai;
  }}

}

static void terminal(){}

static void _initlists() {
 int _i; static int _first = 1;
  if (!_first) return;
 _slist1[0] = &(W) - _p;  _dlist1[0] = &(DW) - _p;
 _slist1[1] = &(X) - _p;  _dlist1[1] = &(DX) - _p;
 _slist1[2] = &(cai) - _p;  _dlist1[2] = &(Dcai) - _p;
 _slist1[3] = &(Csk) - _p;  _dlist1[3] = &(DCsk) - _p;
 _slist1[4] = &(B) - _p;  _dlist1[4] = &(DB) - _p;
_first = 0;
}
