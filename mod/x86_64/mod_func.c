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
extern void _pGPeA_k_reg(void);
extern void _stim_reg(void);

void modl_reg(){
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");

    fprintf(stderr," GABAa.mod");
    fprintf(stderr," IAHP.mod");
    fprintf(stderr," IAHP2.mod");
    fprintf(stderr," IAHP2_0403.mod");
    fprintf(stderr," ICA.mod");
    fprintf(stderr," MsLN.mod");
    fprintf(stderr," MsLN_0403.mod");
    fprintf(stderr," cad.mod");
    fprintf(stderr," cad_0403.mod");
    fprintf(stderr," expsid.mod");
    fprintf(stderr," gabaa.mod");
    fprintf(stderr," gamma.mod");
    fprintf(stderr," intermittent_stim.mod");
    fprintf(stderr," intermittent_stim_gaus.mod");
    fprintf(stderr," intermittent_stim_withNoise.mod");
    fprintf(stderr," normrand_test.mod");
    fprintf(stderr," pGPeA_fukuda.mod");
    fprintf(stderr," pGPeA_k.mod");
    fprintf(stderr," stim.mod");
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
  _pGPeA_k_reg();
  _stim_reg();
}
