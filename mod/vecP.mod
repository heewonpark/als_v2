

VERBATIM
extern int ifarg(int iarg);
extern double* vector_vec(void* vv);
extern int vector_capacity(void* vv);
extern void* vector_arg(int iarg);
ENDVERBATIM

NEURON {
    POINTER vecP
}

PARAMETER {
    vecP=0
}

PROCEDURE setVec() {
    VERBATIM
    if(ifarg(1)){
	Object *o = *hoc_objgetarg(1);
	check_obj_type(o, "Vector");
	printf("setVec.size=%d\n",vector_capacity(o->u.this_pointer));
	_p_vecP=vector_vec(o->u.this_pointer);
	printf("_p_vecP=%f\n",*_p_vecP);
    }
    ENDVERBATIM
}