#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;

extern void _GABAa_reg(void);
extern void _IAHP_reg(void);
extern void _IAHP2_reg(void);
extern void _IAHP2_0403_reg(void);
extern void _ICA_reg(void);
extern void _MsLN_reg(void);
extern void _MsLN_0403_reg(void);
extern void _cad_reg(void);
extern void _cad_0403_reg(void);
extern void _expsid_reg(void);
extern void _gabaa_reg(void);
extern void _gamma_reg(void);
extern void _intermittent_stim_reg(void);
extern void _intermittent_stim_gaus_reg(void);
extern void _intermittent_stim_withNoise_reg(void);
extern void _normrand_test_reg(void);
extern void _pGPeA_fukuda_reg(void);
extern void _stim_reg(void);

void modl_reg(){
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");

    fprintf(stderr," ./mod//GABAa.mod");
    fprintf(stderr," ./mod//IAHP.mod");
    fprintf(stderr," ./mod//IAHP2.mod");
    fprintf(stderr," ./mod//IAHP2_0403.mod");
    fprintf(stderr," ./mod//ICA.mod");
    fprintf(stderr," ./mod//MsLN.mod");
    fprintf(stderr," ./mod//MsLN_0403.mod");
    fprintf(stderr," ./mod//cad.mod");
    fprintf(stderr," ./mod//cad_0403.mod");
    fprintf(stderr," ./mod//expsid.mod");
    fprintf(stderr," ./mod//gabaa.mod");
    fprintf(stderr," ./mod//gamma.mod");
    fprintf(stderr," ./mod//intermittent_stim.mod");
    fprintf(stderr," ./mod//intermittent_stim_gaus.mod");
    fprintf(stderr," ./mod//intermittent_stim_withNoise.mod");
    fprintf(stderr," ./mod//normrand_test.mod");
    fprintf(stderr," ./mod//pGPeA_fukuda.mod");
    fprintf(stderr," ./mod//stim.mod");
    fprintf(stderr, "\n");
  }
  _GABAa_reg();
  _IAHP_reg();
  _IAHP2_reg();
  _IAHP2_0403_reg();
  _ICA_reg();
  _MsLN_reg();
  _MsLN_0403_reg();
  _cad_reg();
  _cad_0403_reg();
  _expsid_reg();
  _gabaa_reg();
  _gamma_reg();
  _intermittent_stim_reg();
  _intermittent_stim_gaus_reg();
  _intermittent_stim_withNoise_reg();
  _normrand_test_reg();
  _pGPeA_fukuda_reg();
  _stim_reg();
}
