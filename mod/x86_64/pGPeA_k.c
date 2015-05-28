/* Created by Language version: 6.2.0 */
/* VECTORIZED */
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
 
#define _threadargscomma_ _p, _ppvar, _thread, _nt,
#define _threadargs_ _p, _ppvar, _thread, _nt
 
#define _threadargsprotocomma_ double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt,
#define _threadargsproto_ double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt
 	/*SUPPRESS 761*/
	/*SUPPRESS 762*/
	/*SUPPRESS 763*/
	/*SUPPRESS 765*/
	 extern double *getarg();
 /* Thread safe. No static _p or _ppvar. */
 
#define t _nt->_t
#define dt _nt->_dt
#define gnabar _p[0]
#define kna _p[1]
#define gkdrbar _p[2]
#define kk _p[3]
#define gl _p[4]
#define el _p[5]
#define kca _p[6]
#define vol _p[7]
#define caGain _p[8]
#define gcatbar _p[9]
#define gkcabar _p[10]
#define ina _p[11]
#define ik _p[12]
#define ikD _p[13]
#define ikAHP _p[14]
#define ica _p[15]
#define icaT _p[16]
#define ilk _p[17]
#define h_inf _p[18]
#define tau_h _p[19]
#define m_inf _p[20]
#define tau_m _p[21]
#define ena _p[22]
#define gna _p[23]
#define n_inf _p[24]
#define tau_n _p[25]
#define ek _p[26]
#define gkdr _p[27]
#define p_inf _p[28]
#define q_inf _p[29]
#define tau_p _p[30]
#define tau_q _p[31]
#define eca _p[32]
#define gcat _p[33]
#define r_inf _p[34]
#define gkca _p[35]
#define m _p[36]
#define h _p[37]
#define n _p[38]
#define p _p[39]
#define q _p[40]
#define r _p[41]
#define tau_m0 _p[42]
#define tau_m1 _p[43]
#define tau_h0 _p[44]
#define tau_h1 _p[45]
#define tau_n0 _p[46]
#define tau_n1 _p[47]
#define Dm _p[48]
#define Dh _p[49]
#define Dn _p[50]
#define Dp _p[51]
#define Dq _p[52]
#define cai _p[53]
#define Dcai _p[54]
#define cao _p[55]
#define Dcao _p[56]
#define nai _p[57]
#define Dnai _p[58]
#define nao _p[59]
#define Dnao _p[60]
#define ki _p[61]
#define Dki _p[62]
#define ko _p[63]
#define Dko _p[64]
#define Dr _p[65]
#define v _p[66]
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
 static Datum* _extcall_thread;
 static Prop* _extcall_prop;
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
 _extcall_prop = _prop;
 }
 static void _hoc_setdata() {
 Prop *_prop, *hoc_getdata_range(int);
 _prop = hoc_getdata_range(_mechtype);
   _setdata(_prop);
 hoc_retpushx(1.);
}
 /* connect user functions to hoc names */
 static VoidFunc hoc_intfunc[] = {
 "setdata_GPeA_k", _hoc_setdata,
 "evaluate_fct_GPeA_k", _hoc_evaluate_fct,
 0, 0
};
 /* declare global and static user variables */
 static int _thread1data_inuse = 0;
static double _thread1data[1];
#define _gth 0
#define R R_GPeA_k
 double R = 8.31441;
#define T_GPeA_k _thread1data[0]
#define T _thread[_gth]._pval[0]
#define k_r k_r_GPeA_k
 double k_r = -8e-05;
#define k_q k_q_GPeA_k
 double k_q = 5.8;
#define k_p k_p_GPeA_k
 double k_p = -6.7;
#define k_n k_n_GPeA_k
 double k_n = -14;
#define k_h k_h_GPeA_k
 double k_h = 6.4;
#define k_m k_m_GPeA_k
 double k_m = -7;
#define power_r power_r_GPeA_k
 double power_r = 2;
#define sig_q2 sig_q2_GPeA_k
 double sig_q2 = 16;
#define sig_q1 sig_q1_GPeA_k
 double sig_q1 = -15;
#define sig_p2 sig_p2_GPeA_k
 double sig_p2 = 15;
#define sig_p1 sig_p1_GPeA_k
 double sig_p1 = -10;
#define sig_n2 sig_n2_GPeA_k
 double sig_n2 = 50;
#define sig_n1 sig_n1_GPeA_k
 double sig_n1 = -40;
#define sig_h2 sig_h2_GPeA_k
 double sig_h2 = 16;
#define sig_h1 sig_h1_GPeA_k
 double sig_h1 = -15;
#define sig_m sig_m_GPeA_k
 double sig_m = -0.7;
#define tau_r tau_r_GPeA_k
 double tau_r = 2;
#define theta_r theta_r_GPeA_k
 double theta_r = 0.00017;
#define tht_q2 tht_q2_GPeA_k
 double tht_q2 = -50;
#define tht_q1 tht_q1_GPeA_k
 double tht_q1 = -50;
#define tht_p2 tht_p2_GPeA_k
 double tht_p2 = -102;
#define tht_p1 tht_p1_GPeA_k
 double tht_p1 = -27;
#define tau_q1 tau_q1_GPeA_k
 double tau_q1 = 400;
#define tau_q0 tau_q0_GPeA_k
 double tau_q0 = 0;
#define tau_p1 tau_p1_GPeA_k
 double tau_p1 = 0.33;
#define tau_p0 tau_p0_GPeA_k
 double tau_p0 = 5;
#define theta_q theta_q_GPeA_k
 double theta_q = -85;
#define theta_p theta_p_GPeA_k
 double theta_p = -56;
#define tht_n2 tht_n2_GPeA_k
 double tht_n2 = -40;
#define tht_n1 tht_n1_GPeA_k
 double tht_n1 = -40;
#define theta_n theta_n_GPeA_k
 double theta_n = -42;
#define tht_h2 tht_h2_GPeA_k
 double tht_h2 = -50;
#define tht_h1 tht_h1_GPeA_k
 double tht_h1 = -50;
#define tht_m tht_m_GPeA_k
 double tht_m = -53;
#define theta_h theta_h_GPeA_k
 double theta_h = -45.5;
#define theta_m theta_m_GPeA_k
 double theta_m = -38;
 /* some parameters have upper and lower limits */
 static HocParmLimits _hoc_parm_limits[] = {
 0,0,0
};
 static HocParmUnits _hoc_parm_units[] = {
 "R_GPeA_k", "Gas",
 "T_GPeA_k", "Absolute",
 "theta_m_GPeA_k", "mV",
 "theta_h_GPeA_k", "mV",
 "k_m_GPeA_k", "mV",
 "k_h_GPeA_k", "mV",
 "tht_m_GPeA_k", "mV",
 "tht_h1_GPeA_k", "mV",
 "tht_h2_GPeA_k", "mV",
 "sig_m_GPeA_k", "mV",
 "sig_h1_GPeA_k", "mV",
 "sig_h2_GPeA_k", "mV",
 "theta_n_GPeA_k", "mV",
 "k_n_GPeA_k", "mV",
 "tht_n1_GPeA_k", "mV",
 "tht_n2_GPeA_k", "mV",
 "sig_n1_GPeA_k", "mV",
 "sig_n2_GPeA_k", "mV",
 "theta_p_GPeA_k", "mV",
 "theta_q_GPeA_k", "mV",
 "k_p_GPeA_k", "mV",
 "k_q_GPeA_k", "mV",
 "tau_p0_GPeA_k", "ms",
 "tau_p1_GPeA_k", "ms",
 "tau_q0_GPeA_k", "ms",
 "tau_q1_GPeA_k", "ms",
 "tht_p1_GPeA_k", "mV",
 "tht_p2_GPeA_k", "mV",
 "tht_q1_GPeA_k", "mV",
 "tht_q2_GPeA_k", "mV",
 "sig_p1_GPeA_k", "mV",
 "sig_p2_GPeA_k", "mV",
 "sig_q1_GPeA_k", "mV",
 "sig_q2_GPeA_k", "mV",
 "theta_r_GPeA_k", "mM",
 "k_r_GPeA_k", "mM",
 "tau_r_GPeA_k", "ms",
 "gnabar_GPeA_k", "S/cm2",
 "gkdrbar_GPeA_k", "S/cm2",
 "gl_GPeA_k", "S/cm2",
 "el_GPeA_k", "mV",
 "kca_GPeA_k", "1/ms",
 "vol_GPeA_k", "L",
 "gcatbar_GPeA_k", "S/cm2",
 "gkcabar_GPeA_k", "S/cm2",
 "ina_GPeA_k", "mA/cm2",
 "ik_GPeA_k", "mA/cm2",
 "ikD_GPeA_k", "mA/cm2",
 "ikAHP_GPeA_k", "mA/cm2",
 "ica_GPeA_k", "mA/cm2",
 "icaT_GPeA_k", "mA/cm2",
 "ilk_GPeA_k", "mA/cm2",
 "tau_h_GPeA_k", "ms",
 "tau_m_GPeA_k", "ms",
 "ena_GPeA_k", "mV",
 "gna_GPeA_k", "S/cm2",
 "tau_n_GPeA_k", "ms",
 "ek_GPeA_k", "mV",
 "gkdr_GPeA_k", "S/cm2",
 "tau_p_GPeA_k", "ms",
 "tau_q_GPeA_k", "ms",
 "eca_GPeA_k", "mV",
 "gcat_GPeA_k", "S/cm2",
 "gkca_GPeA_k", "S/cm2",
 0,0
};
 static double cao0 = 0;
 static double cai0 = 0;
 static double delta_t = 0.01;
 static double h0 = 0;
 static double ko0 = 0;
 static double ki0 = 0;
 static double m0 = 0;
 static double nao0 = 0;
 static double nai0 = 0;
 static double n0 = 0;
 static double p0 = 0;
 static double q0 = 0;
 static double r0 = 0;
 /* connect global user variables to hoc */
 static DoubScal hoc_scdoub[] = {
 "R_GPeA_k", &R_GPeA_k,
 "T_GPeA_k", &T_GPeA_k,
 "theta_m_GPeA_k", &theta_m_GPeA_k,
 "theta_h_GPeA_k", &theta_h_GPeA_k,
 "k_m_GPeA_k", &k_m_GPeA_k,
 "k_h_GPeA_k", &k_h_GPeA_k,
 "tht_m_GPeA_k", &tht_m_GPeA_k,
 "tht_h1_GPeA_k", &tht_h1_GPeA_k,
 "tht_h2_GPeA_k", &tht_h2_GPeA_k,
 "sig_m_GPeA_k", &sig_m_GPeA_k,
 "sig_h1_GPeA_k", &sig_h1_GPeA_k,
 "sig_h2_GPeA_k", &sig_h2_GPeA_k,
 "theta_n_GPeA_k", &theta_n_GPeA_k,
 "k_n_GPeA_k", &k_n_GPeA_k,
 "tht_n1_GPeA_k", &tht_n1_GPeA_k,
 "tht_n2_GPeA_k", &tht_n2_GPeA_k,
 "sig_n1_GPeA_k", &sig_n1_GPeA_k,
 "sig_n2_GPeA_k", &sig_n2_GPeA_k,
 "theta_p_GPeA_k", &theta_p_GPeA_k,
 "theta_q_GPeA_k", &theta_q_GPeA_k,
 "k_p_GPeA_k", &k_p_GPeA_k,
 "k_q_GPeA_k", &k_q_GPeA_k,
 "tau_p0_GPeA_k", &tau_p0_GPeA_k,
 "tau_p1_GPeA_k", &tau_p1_GPeA_k,
 "tau_q0_GPeA_k", &tau_q0_GPeA_k,
 "tau_q1_GPeA_k", &tau_q1_GPeA_k,
 "tht_p1_GPeA_k", &tht_p1_GPeA_k,
 "tht_p2_GPeA_k", &tht_p2_GPeA_k,
 "tht_q1_GPeA_k", &tht_q1_GPeA_k,
 "tht_q2_GPeA_k", &tht_q2_GPeA_k,
 "sig_p1_GPeA_k", &sig_p1_GPeA_k,
 "sig_p2_GPeA_k", &sig_p2_GPeA_k,
 "sig_q1_GPeA_k", &sig_q1_GPeA_k,
 "sig_q2_GPeA_k", &sig_q2_GPeA_k,
 "theta_r_GPeA_k", &theta_r_GPeA_k,
 "k_r_GPeA_k", &k_r_GPeA_k,
 "tau_r_GPeA_k", &tau_r_GPeA_k,
 "power_r_GPeA_k", &power_r_GPeA_k,
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
"GPeA_k",
 "gnabar_GPeA_k",
 "kna_GPeA_k",
 "gkdrbar_GPeA_k",
 "kk_GPeA_k",
 "gl_GPeA_k",
 "el_GPeA_k",
 "kca_GPeA_k",
 "vol_GPeA_k",
 "caGain_GPeA_k",
 "gcatbar_GPeA_k",
 "gkcabar_GPeA_k",
 0,
 "ina_GPeA_k",
 "ik_GPeA_k",
 "ikD_GPeA_k",
 "ikAHP_GPeA_k",
 "ica_GPeA_k",
 "icaT_GPeA_k",
 "ilk_GPeA_k",
 "h_inf_GPeA_k",
 "tau_h_GPeA_k",
 "m_inf_GPeA_k",
 "tau_m_GPeA_k",
 "ena_GPeA_k",
 "gna_GPeA_k",
 "n_inf_GPeA_k",
 "tau_n_GPeA_k",
 "ek_GPeA_k",
 "gkdr_GPeA_k",
 "p_inf_GPeA_k",
 "q_inf_GPeA_k",
 "tau_p_GPeA_k",
 "tau_q_GPeA_k",
 "eca_GPeA_k",
 "gcat_GPeA_k",
 "r_inf_GPeA_k",
 "gkca_GPeA_k",
 0,
 "m_GPeA_k",
 "h_GPeA_k",
 "n_GPeA_k",
 "p_GPeA_k",
 "q_GPeA_k",
 "r_GPeA_k",
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
 	gnabar = 0.049;
 	kna = 1;
 	gkdrbar = 0.057;
 	kk = 1;
 	gl = 0.00035;
 	el = -60;
 	kca = 2;
 	vol = 3.355e-11;
 	caGain = 0.1;
 	gcatbar = 0.005;
 	gkcabar = 0.001;
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
 0,0
};
 static void _thread_mem_init(Datum*);
 static void _thread_cleanup(Datum*);
 static void _update_ion_pointer(Datum*);
 extern Symbol* hoc_lookup(const char*);
extern void _nrn_thread_reg(int, int, void(*f)(Datum*));
extern void _nrn_thread_table_reg(int, void(*)(double*, Datum*, Datum*, _NrnThread*, int));
extern void hoc_register_tolerance(int, HocStateTolerance*, Symbol***);
extern void _cvode_abstol( Symbol**, double*, int);

 void _pGPeA_k_reg() {
	int _vectorized = 1;
  _initlists();
 	ion_reg("ca", -10000.);
 	ion_reg("k", -10000.);
 	ion_reg("na", -10000.);
 	_ca_sym = hoc_lookup("ca_ion");
 	_k_sym = hoc_lookup("k_ion");
 	_na_sym = hoc_lookup("na_ion");
 	register_mech(_mechanism, nrn_alloc,nrn_cur, nrn_jacob, nrn_state, nrn_init, hoc_nrnpointerindex, 2);
  _extcall_thread = (Datum*)ecalloc(1, sizeof(Datum));
  _thread_mem_init(_extcall_thread);
  _thread1data_inuse = 0;
 _mechtype = nrn_get_mechtype(_mechanism[1]);
     _nrn_setdata_reg(_mechtype, _setdata);
     _nrn_thread_reg(_mechtype, 1, _thread_mem_init);
     _nrn_thread_reg(_mechtype, 0, _thread_cleanup);
     _nrn_thread_reg(_mechtype, 2, _update_ion_pointer);
  hoc_register_dparam_size(_mechtype, 15);
 	nrn_writes_conc(_mechtype, 0);
 	hoc_register_cvode(_mechtype, _ode_count, _ode_map, _ode_spec, _ode_matsol);
 	hoc_register_tolerance(_mechtype, _hoc_state_tol, &_atollist);
 	hoc_register_var(hoc_scdoub, hoc_vdoub, hoc_intfunc);
 	ivoc_help("help ?1 GPeA_k /home/park/code/neuron/al_V2/mod/x86_64/pGPeA_k.mod\n");
 hoc_register_limits(_mechtype, _hoc_parm_limits);
 hoc_register_units(_mechtype, _hoc_parm_units);
 }
 static double FARADAY = 96485.3;
 static double PI = 3.14159;
static int _reset;
static char *modelname = "All ion channels used in GP models";

static int error;
static int _ninits = 0;
static int _match_recurse=1;
static void _modl_cleanup(){ _match_recurse=1;}
static int evaluate_fct(_threadargsprotocomma_ double);
 
static int _ode_spec1(_threadargsproto_);
/*static int _ode_matsol1(_threadargsproto_);*/
 static int _slist1[7], _dlist1[7];
 static int states(_threadargsproto_);
 
/*CVODE*/
 static int _ode_spec1 (double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {int _reset = 0; {
   evaluate_fct ( _threadargscomma_ v ) ;
   Dh = ( h_inf - h ) / tau_h ;
   Dm = ( m_inf - m ) / tau_m ;
   Dn = ( n_inf - n ) / tau_n ;
   Dp = ( p_inf - p ) / tau_p ;
   Dq = ( q_inf - q ) / tau_q ;
   Dcai = caGain * ( - ica * area * 1e-11 / ( 2.0 * FARADAY * vol ) - kca * cai ) ;
   Dr = ( r_inf - r ) / tau_r ;
   }
 return _reset;
}
 static int _ode_matsol1 (double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {
 evaluate_fct ( _threadargscomma_ v ) ;
 Dh = Dh  / (1. - dt*( ( ( ( - 1.0 ) ) ) / tau_h )) ;
 Dm = Dm  / (1. - dt*( ( ( ( - 1.0 ) ) ) / tau_m )) ;
 Dn = Dn  / (1. - dt*( ( ( ( - 1.0 ) ) ) / tau_n )) ;
 Dp = Dp  / (1. - dt*( ( ( ( - 1.0 ) ) ) / tau_p )) ;
 Dq = Dq  / (1. - dt*( ( ( ( - 1.0 ) ) ) / tau_q )) ;
 Dcai = Dcai  / (1. - dt*( (caGain)*(( ( - (kca)*(1.0) ) )) )) ;
 Dr = Dr  / (1. - dt*( ( ( ( - 1.0 ) ) ) / tau_r )) ;
 return 0;
}
 /*END CVODE*/
 static int states (double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) { {
   evaluate_fct ( _threadargscomma_ v ) ;
    h = h + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / tau_h)))*(- ( ( ( h_inf ) ) / tau_h ) / ( ( ( ( - 1.0) ) ) / tau_h ) - h) ;
    m = m + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / tau_m)))*(- ( ( ( m_inf ) ) / tau_m ) / ( ( ( ( - 1.0) ) ) / tau_m ) - m) ;
    n = n + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / tau_n)))*(- ( ( ( n_inf ) ) / tau_n ) / ( ( ( ( - 1.0) ) ) / tau_n ) - n) ;
    p = p + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / tau_p)))*(- ( ( ( p_inf ) ) / tau_p ) / ( ( ( ( - 1.0) ) ) / tau_p ) - p) ;
    q = q + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / tau_q)))*(- ( ( ( q_inf ) ) / tau_q ) / ( ( ( ( - 1.0) ) ) / tau_q ) - q) ;
    cai = cai + (1. - exp(dt*((caGain)*(( ( - (kca)*(1.0) ) )))))*(- ( (caGain)*(( ( ((- ica)*(area))*(1e-11) ) / ( 2.0 * FARADAY * vol ) )) ) / ( (caGain)*(( ( - (kca)*(1.0)) )) ) - cai) ;
    r = r + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / tau_r)))*(- ( ( ( r_inf ) ) / tau_r ) / ( ( ( ( - 1.0) ) ) / tau_r ) - r) ;
   }
  return 0;
}
 
static int  evaluate_fct ( _threadargsprotocomma_ double _lv ) {
   h_inf = 1.0 / ( 1.0 + exp ( ( _lv - theta_h ) / k_h ) ) ;
   m_inf = 1.0 / ( 1.0 + exp ( ( _lv - theta_m ) / k_m ) ) ;
   tau_h = tau_h0 + tau_h1 / ( exp ( - ( _lv - tht_h1 ) / sig_h1 ) + exp ( - ( _lv - tht_h2 ) / sig_h2 ) ) ;
   tau_m = tau_m0 + tau_m1 / ( 1.0 + exp ( - ( _lv - tht_m ) / sig_m ) ) ;
   n_inf = 1.0 / ( 1.0 + exp ( ( _lv - theta_n ) / k_n ) ) ;
   tau_n = tau_n0 + tau_n1 / ( exp ( - ( _lv - tht_n1 ) / sig_n1 ) + exp ( - ( _lv - tht_n2 ) / sig_n2 ) ) ;
   p_inf = 1.0 / ( 1.0 + exp ( ( _lv - theta_p ) / k_p ) ) ;
   q_inf = 1.0 / ( 1.0 + exp ( ( _lv - theta_q ) / k_q ) ) ;
   tau_p = tau_p0 + tau_p1 / ( exp ( - ( _lv - tht_p1 ) / sig_p1 ) + exp ( - ( _lv - tht_p2 ) / sig_p2 ) ) ;
   tau_q = tau_q0 + tau_q1 / ( exp ( - ( _lv - tht_q1 ) / sig_q1 ) + exp ( - ( _lv - tht_q2 ) / sig_q2 ) ) ;
   r_inf = 1.0 / ( 1.0 + exp ( ( cai - theta_r ) / k_r ) ) ;
    return 0; }
 
static void _hoc_evaluate_fct(void) {
  double _r;
   double* _p; Datum* _ppvar; Datum* _thread; _NrnThread* _nt;
   if (_extcall_prop) {_p = _extcall_prop->param; _ppvar = _extcall_prop->dparam;}else{ _p = (double*)0; _ppvar = (Datum*)0; }
  _thread = _extcall_thread;
  _nt = nrn_threads;
 _r = 1.;
 evaluate_fct ( _p, _ppvar, _thread, _nt, *getarg(1) );
 hoc_retpushx(_r);
}
 
static int _ode_count(int _type){ return 7;}
 
static void _ode_spec(_NrnThread* _nt, _Memb_list* _ml, int _type) {
   double* _p; Datum* _ppvar; Datum* _thread;
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
     _ode_spec1 (_p, _ppvar, _thread, _nt);
   _ion_cai = cai;
   }}
 
static void _ode_map(int _ieq, double** _pv, double** _pvdot, double* _pp, Datum* _ppd, double* _atol, int _type) { 
	double* _p; Datum* _ppvar;
 	int _i; _p = _pp; _ppvar = _ppd;
	_cvode_ieq = _ieq;
	for (_i=0; _i < 7; ++_i) {
		_pv[_i] = _pp + _slist1[_i];  _pvdot[_i] = _pp + _dlist1[_i];
		_cvode_abstol(_atollist, _atol, _i);
	}
 	_pv[5] = &(_ion_cai);
 }
 
static void _ode_matsol(_NrnThread* _nt, _Memb_list* _ml, int _type) {
   double* _p; Datum* _ppvar; Datum* _thread;
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
 _ode_matsol1 (_p, _ppvar, _thread, _nt);
 }}
 
static void _thread_mem_init(Datum* _thread) {
  if (_thread1data_inuse) {_thread[_gth]._pval = (double*)ecalloc(1, sizeof(double));
 }else{
 _thread[_gth]._pval = _thread1data; _thread1data_inuse = 1;
 }
 }
 
static void _thread_cleanup(Datum* _thread) {
  if (_thread[_gth]._pval == _thread1data) {
   _thread1data_inuse = 0;
  }else{
   free((void*)_thread[_gth]._pval);
  }
 }
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

static void initmodel(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {
  int _i; double _save;{
  h = h0;
  m = m0;
  n = n0;
  p = p0;
  q = q0;
  r = r0;
 {
   evaluate_fct ( _threadargscomma_ v ) ;
   m = m_inf ;
   h = h_inf ;
   n = n_inf ;
   p = p_inf ;
   q = q_inf ;
   r = r_inf ;
   }
 
}
}

static void nrn_init(_NrnThread* _nt, _Memb_list* _ml, int _type){
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; double _v; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
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
 initmodel(_p, _ppvar, _thread, _nt);
   _ion_cai = cai;
  nrn_wrote_conc(_ca_sym, (&(_ion_cai)) - 1, _style_ca);
  }}

static double _nrn_current(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt, double _v){double _current=0.;v=_v;{ {
   T = 273.0 + celsius - 9.5 ;
   ena = - ( R * T ) / FARADAY * log ( nai / nao ) * 1000.0 ;
   ek = ( R * T ) / FARADAY * log ( ko / ki ) * 1000.0 ;
   eca = - ( R * T ) / FARADAY * log ( cai / cao ) * 1000.0 / 2.0 ;
   tau_m0 = kna * 0.001 ;
   tau_m1 = kna * 0.1 ;
   tau_h0 = kna * 0.0 ;
   tau_h1 = kna * 4.5 ;
   tau_n0 = kk * 0.0 ;
   tau_n1 = kk * 2.4 ;
   gna = gnabar * m * m * m * h ;
   ina = gna * ( v - ena ) ;
   gkdr = gkdrbar * pow( n , 4.0 ) ;
   ikD = gkdr * ( v - ek ) ;
   gkca = gkcabar * pow( r , ( power_r ) ) ;
   ikAHP = gkca * ( v - ek ) ;
   ik = ikD + ikAHP ;
   ilk = gl * ( v - el ) ;
   gcat = gcatbar * p * p * q ;
   ica = gcat * ( v - eca ) ;
   }
 _current += ilk;
 _current += ica;
 _current += ik;
 _current += ina;

} return _current;
}

static void nrn_cur(_NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; int* _ni; double _rhs, _v; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
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
 _g = _nrn_current(_p, _ppvar, _thread, _nt, _v + .001);
 	{ double _dina;
 double _dik;
 double _dica;
  _dica = ica;
  _dik = ik;
  _dina = ina;
 _rhs = _nrn_current(_p, _ppvar, _thread, _nt, _v);
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

static void nrn_jacob(_NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
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

static void nrn_state(_NrnThread* _nt, _Memb_list* _ml, int _type) {
 double _break, _save;
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; double _v; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
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
   states(_p, _ppvar, _thread, _nt);
  
}}
 t = _save;
 }   _ion_cai = cai;
  }}

}

static void terminal(){}

static void _initlists(){
 double _x; double* _p = &_x;
 int _i; static int _first = 1;
  if (!_first) return;
 _slist1[0] = &(h) - _p;  _dlist1[0] = &(Dh) - _p;
 _slist1[1] = &(m) - _p;  _dlist1[1] = &(Dm) - _p;
 _slist1[2] = &(n) - _p;  _dlist1[2] = &(Dn) - _p;
 _slist1[3] = &(p) - _p;  _dlist1[3] = &(Dp) - _p;
 _slist1[4] = &(q) - _p;  _dlist1[4] = &(Dq) - _p;
 _slist1[5] = &(cai) - _p;  _dlist1[5] = &(Dcai) - _p;
 _slist1[6] = &(r) - _p;  _dlist1[6] = &(Dr) - _p;
_first = 0;
}

#if defined(__cplusplus)
} /* extern "C" */
#endif
