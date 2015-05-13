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
#define del _p[0]
#define dur _p[1]
#define Imax _p[2]
#define tau_rise _p[3]
#define t0 _p[4]
#define tau_fall _p[5]
#define interval _p[6]
#define Imax2 _p[7]
#define stdev _p[8]
#define average _p[9]
#define forseed _p[10]
#define sigma_o _p[11]
#define i _p[12]
#define cnt _p[13]
#define flg _p[14]
#define j _p[15]
#define k _p[16]
#define nStim _p[17]
#define temp _p[18]
#define i1 _p[19]
#define a _p[20]
#define v1 _p[21]
#define v2 _p[22]
#define s _p[23]
#define counter _p[24]
#define _g _p[25]
#define _nd_area  *_ppvar[0]._pval
#define area	*_ppvar[2]._pval
 
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
 /* declaration of user functions */
 static double _hoc_stim1();
 static int _mechtype;
extern void _nrn_cacheloop_reg(int, int);
extern void hoc_register_prop_size(int, int, int);
extern void hoc_register_limits(int, HocParmLimits*);
extern void hoc_register_units(int, HocParmUnits*);
extern void nrn_promote(Prop*, int, int);
extern Memb_func* memb_func;
 extern Prop* nrn_point_prop_;
 static int _pointtype;
 static void* _hoc_create_pnt(_ho) Object* _ho; { void* create_point_process();
 return create_point_process(_pointtype, _ho);
}
 static void _hoc_destroy_pnt();
 static double _hoc_loc_pnt(_vptr) void* _vptr; {double loc_point_process();
 return loc_point_process(_pointtype, _vptr);
}
 static double _hoc_has_loc(_vptr) void* _vptr; {double has_loc_point();
 return has_loc_point(_vptr);
}
 static double _hoc_get_loc_pnt(_vptr)void* _vptr; {
 double get_loc_point_process(); return (get_loc_point_process(_vptr));
}
 extern void _nrn_setdata_reg(int, void(*)(Prop*));
 static void _setdata(Prop* _prop) {
 _p = _prop->param; _ppvar = _prop->dparam;
 }
 static void _hoc_setdata(void* _vptr) { Prop* _prop;
 _prop = ((Point_process*)_vptr)->_prop;
   _setdata(_prop);
 }
 /* connect user functions to hoc names */
 static VoidFunc hoc_intfunc[] = {
 0,0
};
 static Member_func _member_func[] = {
 "loc", _hoc_loc_pnt,
 "has_loc", _hoc_has_loc,
 "get_loc", _hoc_get_loc_pnt,
 "stim1", _hoc_stim1,
 0, 0
};
#define stim1 stim1_intermitStimGaus
 extern double stim1( double );
 /* declare global and static user variables */
#define amp amp_intermitStimGaus
 double amp = 0;
 /* some parameters have upper and lower limits */
 static HocParmLimits _hoc_parm_limits[] = {
 "dur", 0, 1e+09,
 0,0,0
};
 static HocParmUnits _hoc_parm_units[] = {
 "amp_intermitStimGaus", "nA",
 "del", "ms",
 "dur", "ms",
 "Imax", "nA/cm2",
 "tau_rise", "ms",
 "t0", "ms",
 "tau_fall", "ms",
 "interval", "ms",
 "Imax2", "nA/cm2",
 "i", "nA",
 0,0
};
 static double v = 0;
 /* connect global user variables to hoc */
 static DoubScal hoc_scdoub[] = {
 "amp_intermitStimGaus", &amp_intermitStimGaus,
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
 static void _hoc_destroy_pnt(_vptr) void* _vptr; {
   destroy_point_process(_vptr);
}
 /* connect range variables in _p that hoc is supposed to know about */
 static const char *_mechanism[] = {
 "6.2.0",
"intermitStimGaus",
 "del",
 "dur",
 "Imax",
 "tau_rise",
 "t0",
 "tau_fall",
 "interval",
 "Imax2",
 "stdev",
 "average",
 "forseed",
 "sigma_o",
 0,
 "i",
 "cnt",
 "flg",
 "j",
 "k",
 "nStim",
 "temp",
 0,
 0,
 0};
 extern Node* nrn_alloc_node_;
 
extern Prop* need_memb(Symbol*);

static void nrn_alloc(Prop* _prop) {
	Prop *prop_ion;
	double *_p; Datum *_ppvar;
  if (nrn_point_prop_) {
	_prop->_alloc_seq = nrn_point_prop_->_alloc_seq;
	_p = nrn_point_prop_->param;
	_ppvar = nrn_point_prop_->dparam;
 }else{
 	_p = nrn_prop_data_alloc(_mechtype, 26, _prop);
 	/*initialize range parameters*/
 	del = 0;
 	dur = 0;
 	Imax = 15000;
 	tau_rise = 5;
 	t0 = 50;
 	tau_fall = 4000;
 	interval = 300;
 	Imax2 = 15000;
 	stdev = 1;
 	average = 0;
 	forseed = 0;
 	sigma_o = 0.09;
  }
 	_prop->param = _p;
 	_prop->param_size = 26;
  if (!nrn_point_prop_) {
 	_ppvar = nrn_prop_datum_alloc(_mechtype, 3, _prop);
  }
 	_prop->dparam = _ppvar;
 	/*connect ionic variables to this model*/
 	_ppvar[2]._pval = &nrn_alloc_node_->_area; /* diam */
 
}
 static void _initlists();
 extern Symbol* hoc_lookup(const char*);
extern void _nrn_thread_reg(int, int, void(*f)(Datum*));
extern void _nrn_thread_table_reg(int, void(*)(double*, Datum*, Datum*, _NrnThread*, int));
extern void hoc_register_tolerance(int, HocStateTolerance*, Symbol***);
extern void _cvode_abstol( Symbol**, double*, int);

 void _intermittent_stim_gaus_reg() {
	int _vectorized = 0;
  _initlists();
 	_pointtype = point_register_mech(_mechanism,
	 nrn_alloc,nrn_cur, nrn_jacob, nrn_state, nrn_init,
	 hoc_nrnpointerindex, 0,
	 _hoc_create_pnt, _hoc_destroy_pnt, _member_func);
 _mechtype = nrn_get_mechtype(_mechanism[1]);
     _nrn_setdata_reg(_mechtype, _setdata);
  hoc_register_dparam_size(_mechtype, 3);
 	hoc_register_var(hoc_scdoub, hoc_vdoub, hoc_intfunc);
 	ivoc_help("help ?1 intermitStimGaus /home/park/code/neuron/al_V2/mod/x86_64/intermittent_stim_gaus.mod\n");
 hoc_register_limits(_mechtype, _hoc_parm_limits);
 hoc_register_units(_mechtype, _hoc_parm_units);
 }
static int _reset;
static char *modelname = "";

static int error;
static int _ninits = 0;
static int _match_recurse=1;
static void _modl_cleanup(){ _match_recurse=1;}
 
double stim1 (  double _lt ) {
   double _lstim1;
 a = pow( 10.0 , - 8.0 ) * area ;
   _lstim1 = Imax * ( 1.0 - exp ( - ( _lt ) / tau_rise ) ) * a ;
   
return _lstim1;
 }
 
static double _hoc_stim1(void* _vptr) {
 double _r;
    _hoc_setdata(_vptr);
 _r =  stim1 (  *getarg(1) );
 return(_r);
}

static void initmodel() {
  int _i; double _save;_ninits++;
{
 {
   i = 0.0 ;
   cnt = 0.0 ;
   j = 0.0 ;
   k = 0.0 ;
   flg = 0.0 ;
   counter = 0.0 ;
   
/*VERBATIM*/
    /*printf("forseed is %lf\n",forseed);*/
    srand((unsigned)time(NULL)+forseed);
    /*srand(25525);*/
 }

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
#if EXTRACELLULAR
 _nd = _ml->_nodelist[_iml];
 if (_nd->_extnode) {
    _v = NODEV(_nd) +_nd->_extnode->_v[0];
 }else
#endif
 {
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 }
 v = _v;
 initmodel();
}}

static double _nrn_current(double _v){double _current=0.;v=_v;{ {
   at_time ( nrn_threads, del ) ;
   at_time ( nrn_threads, del + dur ) ;
   
/*VERBATIM*/
	/*printf("%lf\t",t);*/
 if ( k  == nStim ) {
     Imax = Imax2 ;
     }
   if ( counter  == 50.0 ) {
     
/*VERBATIM*/
	    do {
		v1 =  2 * ((double) rand() / RAND_MAX) - 1;
		v2 =  2 * ((double) rand() / RAND_MAX) - 1;
		s = v1 * v1 + v2 * v2;
	    } while (s >= 1 || s == 0);
	    
	    s = sqrt( (-2 * log(s)) / s );
	    
	    temp = v1 * s;
	    temp = (stdev * temp) + average;
	    /*printf("%lf",temp);*/
 counter = 0.0 ;
     }
   if ( t < del + t0 + interval * j  && t >= del + interval * j ) {
     i1 = stim1 ( _threadargscomma_ t - del - interval * j ) ;
     i = i1 * ( 1.0 + sigma_o * temp ) ;
     cnt = 0.0 ;
     k = j ;
     }
   else if ( t >= del + t0 + interval * k ) {
     i1 = stim1 ( _threadargscomma_ t0 ) * exp ( - ( t - t0 - del - interval * k ) / tau_fall ) ;
     i = i1 * ( 1.0 + sigma_o * temp ) ;
     cnt = cnt + 1.0 ;
     if ( cnt  == 1.0 ) {
       flg = 1.0 ;
       }
     }
   else {
     i = 0.0 ;
     }
   counter = counter + 1.0 ;
   if ( flg  == 1.0 ) {
     j = j + 1.0 ;
     flg = 0.0 ;
     }
   }
 _current += i;

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
#if EXTRACELLULAR
 _nd = _ml->_nodelist[_iml];
 if (_nd->_extnode) {
    _v = NODEV(_nd) +_nd->_extnode->_v[0];
 }else
#endif
 {
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 }
 _g = _nrn_current(_v + .001);
 	{ _rhs = _nrn_current(_v);
 	}
 _g = (_g - _rhs)/.001;
 _g *=  1.e2/(_nd_area);
 _rhs *= 1.e2/(_nd_area);
#if CACHEVEC
  if (use_cachevec) {
	VEC_RHS(_ni[_iml]) += _rhs;
  }else
#endif
  {
	NODERHS(_nd) += _rhs;
  }
#if EXTRACELLULAR
 if (_nd->_extnode) {
   *_nd->_extnode->_rhs[0] += _rhs;
 }
#endif
 
}}

static void nrn_jacob(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml];
 _nd = _ml->_nodelist[_iml];
#if CACHEVEC
  if (use_cachevec) {
	VEC_D(_ni[_iml]) -= _g;
  }else
#endif
  {
	NODED(_nd) -= _g;
  }
#if EXTRACELLULAR
 if (_nd->_extnode) {
   *_nd->_extnode->_d[0] += _g;
 }
#endif
 
}}

static void nrn_state(_NrnThread* _nt, _Memb_list* _ml, int _type){

}

static void terminal(){}

static void _initlists() {
 int _i; static int _first = 1;
  if (!_first) return;
_first = 0;
}
