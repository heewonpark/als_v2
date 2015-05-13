#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;

extern void _expsid_reg(void);
extern void _intermittent_stim_reg(void);
extern void _intermittent_stim_gaus_reg(void);
extern void _intermittent_stim_withNoise_reg(void);

void modl_reg(){
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");

    fprintf(stderr," expsid.mod");
    fprintf(stderr," intermittent_stim.mod");
    fprintf(stderr," intermittent_stim_gaus.mod");
    fprintf(stderr," intermittent_stim_withNoise.mod");
    fprintf(stderr, "\n");
  }
  _expsid_reg();
  _intermittent_stim_reg();
  _intermittent_stim_gaus_reg();
  _intermittent_stim_withNoise_reg();
}
