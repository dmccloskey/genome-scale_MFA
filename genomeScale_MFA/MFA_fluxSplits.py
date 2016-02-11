
class isotopomer_fluxSplits():
    def __init__(self):
        self.isotopomer_splits = {};
        self.isotopomer_splits = self.define_fluxSplits();
    def define_fluxSplits(self):
        isotopomer_splits = {};
        isotopomer_splits['g6p_2_f6p_or_6pgc']=['PGI','G6PDH2r'];
        isotopomer_splits['6pgc_2_2ddg6p_or_ru5p-D']=['EDD','GND'];
        isotopomer_splits['pep_2_oaa_or_pyr']=['PPC','PYK','GLCptspp'];
        isotopomer_splits['accoa_2_ac_or_cit']=['PTAr','CS'];
        isotopomer_splits['icit_2_akg_or_glx']=['ICDHyr','ICL'];
        isotopomer_splits['glc-D_2_g6p']=['HEX1','GLCptspp'];
        isotopomer_splits['mal-L_2_oaa_or_pyr']=['ME1','ME2','MDH'];
        return isotopomer_splits