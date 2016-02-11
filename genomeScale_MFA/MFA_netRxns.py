
class isotopomer_netRxns():
    def __init__(self):
        self.isotopomer_rxns_net = {};
        self.isotopomer_rxns_net = self.define_netRxns();
    def define_netRxns(self):
        isotopomer_rxns_net = {};
        isotopomer_rxns_net.update(self.define_netRxns_iDM2014_reversible());
        #isotopomer_rxns_net.update(self.define_netRxns_RL2013_reversible());
        return isotopomer_rxns_net
    def define_netRxns_iDM2014_reversible(self):
        isotopomer_rxns_net = {
        'ptrc_to_4abut_1':{'reactions':['PTRCTA','ABUTD'],
                           'stoichiometry':[1,1]},
        'ptrc_to_4abut_2':{'reactions':['GGPTRCS','GGPTRCO','GGGABADr','GGGABAH'],
                           'stoichiometry':[1,1,1,1]},
        'glu_DASH_L_to_acg5p':{'reactions':['ACGS','ACGK'],
                           'stoichiometry':[1,1]},
        '2obut_and_pyr_to_3mop':{'reactions':['ACHBS','KARA2','DHAD2'],
                           'stoichiometry':[1,1,1]},
        'pyr_to_23dhmb':{'reactions':['ACLS','KARA1'],
                           'stoichiometry':[1,-1]},
        #'met_DASH_L_and_ptrc_to_spmd_and_5mta':{'reactions':['METAT','ADMDC','SPMS'],
        #                   'stoichiometry':[1,1,1]}, #cannot be lumped
        'chor_and_prpp_to_3ig3p':{'reactions':['ANS','ANPRT','PRAIi','IGPS'],
                           'stoichiometry':[1,1,1,1]},
        'hom_DASH_L_and_cyst_DASH_L_to_pyr_hcys_DASH_L':{'reactions':['HSST','SHSL1','CYSTL'],
                           'stoichiometry':[1,1,1]},
        'e4p_and_pep_to_3dhq':{'reactions':['DDPA','DHQS'],
                           'stoichiometry':[1,1]},
        'aspsa_to_sl2a6o':{'reactions':['DHDPS','DHDPRy','THDPS'],
                           'stoichiometry':[1,1,1]},
        'glu_DASH_L_to_glu5sa':{'reactions':['GLU5K','G5SD'],
                           'stoichiometry':[1,1]},
        'g1p_to_glycogen':{'reactions':['GLGC','GLCS1'],
                           'stoichiometry':[1,1]},
        'thr_DASH_L_to_gly':{'reactions':['THRD','GLYAT'],
                           'stoichiometry':[1,-1]}, #need to remove deadend mets: athr-L: ATHRDHr, ATHRDHr_reverse; aact: AACTOOR, AOBUTDs
        'dhap_to_lac_DASH_D':{'reactions':['MGSA','LGTHL','GLYOX'],
                           'stoichiometry':[1,1,1]},
        'hom_DASH_L_to_thr_DASH_L':{'reactions':['HSK','THRS'],
                           'stoichiometry':[1,1]},
        '3pg_to_ser_DASH_L':{'reactions':['PGCD','PSERT','PSP_L'],
                           'stoichiometry':[1,1,1]},
        'prpp_to_his_DASH_L':{'reactions':['ATPPRT','PRATPP','PRAMPC','PRMICI','IG3PS','IGPDH','HSTPT','HISTP','HISTD'],
                           'stoichiometry':[1,1,1,1,1,1,1,1,1]},
        'UMPSYN_aerobic':{'reactions':['ASPCT','DHORTS','DHORD2','ORPT','OMPDC'],
                           'stoichiometry':[1,-1,1,-1,1]},
        #'UMPSYN_anaerobic':{'reactions':['ASPCT','DHORTS','DHORD5','ORPT','OMPDC'],
        #                   'stoichiometry':[1,-1,1,-1,1]},
        'IMPSYN_1':{'reactions':['GLUPRT','PRAGSr','PRFGS','PRAIS'],
                           'stoichiometry':[1,1,1,1]},
        'IMPSYN_2':{'reactions':['AIRC2','AIRC3','PRASCSi','ADSL2r'],
                           'stoichiometry':[1,-1,1,1]},
        'IMPSYN_3':{'reactions':['AICART','IMPC'],
                           'stoichiometry':[1,-1]},
        'imp_to_gmp':{'reactions':['IMPD','GMPS2'],
                           'stoichiometry':[1,1]},
        'imp_to_amp':{'reactions':['ADSS','ADSL1r'],
                           'stoichiometry':[1,1]},
        #'utp_to_dump_anaerobic':{'reactions':['RNTR4c2','DUTPDP'],
        #                   'stoichiometry':[1,1]},
        'udp_to_dump_aerobic':{'reactions':['RNDR4','NDPK6','DUTPDP'],
                           'stoichiometry':[1,1,1]},
        #'dtmp_to_dttp':{'reactions':['DTMPK','NDPK4'],
        #                   'stoichiometry':[1,1]}, #cannot be lumped
        'COASYN':{'reactions':['ASP1DC','MOHMT','DPR','PANTS','PNTK','PPNCL2','PPCDC','PTPATi','DPCOAK'],
                           'stoichiometry':[1,1,1,1,1,1,1,1,1]},
        'FADSYN_1':{'reactions':['GTPCII2','DHPPDA2','APRAUR','PMDPHT','RBFSb'],
                           'stoichiometry':[1,1,1,1,1]},
        'FADSYN_2':{'reactions':['RBFSa','DB4PS'],
                           'stoichiometry':[1,1]},
        'FADSYN_3':{'reactions':['RBFK','FMNAT'],
                           'stoichiometry':[1,1]},
        'NADSYN_aerobic':{'reactions':['ASPO6','QULNS','NNDPR','NNATr','NADS1','NADK'],
                           'stoichiometry':[1,1,1,1,1,1]},
        'NADSYN_anaerobic':{'reactions':['ASPO5','QULNS','NNDPR','NNATr','NADS1','NADK'],
                           'stoichiometry':[1,1,1,1,1,1]},
        #'NADSALVAGE':{'reactions':['NADPPPS','NADN','NNAM','NAMNPP','NMNN','NMNDA','NMNAT','NADDP','ADPRDP'],
        #                   'stoichiometry':[1,1,1,1,1,1,1,1,1]}, #cannot be lumped
        'THFSYN':{'reactions':['GTPCI','DNTPPA','DNMPPA','DHNPA2r','HPPK2','ADCS','ADCL','DHPS2','DHFS'],
                           'stoichiometry':[1,1,1,1,1,1,1,1,1]},
        'GTHSYN':{'reactions':['GLUCYS','GTHS'],
                           'stoichiometry':[1,1]},
        'GLYCPHOSPHOLIPID_1':{'reactions':['DASYN181','AGPAT181','G3PAT181'],'stoichiometry':[1,1,1]},
        'GLYCPHOSPHOLIPID_2':{'reactions':['PSSA181','PSD181'],'stoichiometry':[1,1]},
        'GLYCPHOSPHOLIPID_3':{'reactions':['PGSA160','PGPP160'],'stoichiometry':[1,1]},
        'GLYCPHOSPHOLIPID_4':{'reactions':['DASYN161','AGPAT161','G3PAT161'],'stoichiometry':[1,1,1]},
        'GLYCPHOSPHOLIPID_5':{'reactions':['PGSA181','PGPP181'],'stoichiometry':[1,1]},
        'GLYCPHOSPHOLIPID_6':{'reactions':['PSD161','PSSA161'],'stoichiometry':[1,1]},
        'GLYCPHOSPHOLIPID_7':{'reactions':['PSSA160','PSD160'],'stoichiometry':[1,1]},
        'GLYCPHOSPHOLIPID_8':{'reactions':['DASYN160','AGPAT160','G3PAT160'],'stoichiometry':[1,1,1]},
        'GLYCPHOSPHOLIPID_9':{'reactions':['PGSA161','PGPP161'],'stoichiometry':[1,1]},
        'MOLYBDOPTERIN_1':{'reactions':['MPTAT','MPTS','CPMPS'],'stoichiometry':[1,1,1]},
        'MOLYBDOPTERIN_2':{'reactions':['MOCDS','MOGDS'],'stoichiometry':[1,1]},
        'MOLYBDOPTERIN_3':{'reactions':['MOADSUx','MPTSS'],'stoichiometry':[1,1]},
        'COFACTOR_1':{'reactions':['GLUTRR','G1SAT','GLUTRS'],'stoichiometry':[1,1,1]},
        'COFACTOR_2':{'reactions':['DHNAOT4','UPPDC1','DHNCOAT','DHNCOAS','SEPHCHCS','SUCBZS','SUCBZL','PPPGO3','FCLT','CPPPGO','SHCHCS3'],'stoichiometry':[1,1,1,1,1,1,1,1,1,1,1]},
        'COFACTOR_3':{'reactions':['TYRL','AMMQLT8','HEMEOS','UPP3MT','SHCHD2','SHCHF','ENTCS','CBLAT'],'stoichiometry':[1,1,1,1,1,1,1,1]},
        'VITB6':{'reactions':['E4PD','PERD','OHPBAT','PDX5PS','PDX5PO2'],'stoichiometry':[1,1,1,1,1]},
        #'THIAMIN':{'reactions':['AMPMS2','PMPK','THZPSN3','TMPPP','TMPK'],'stoichiometry':[1,1,1,1,1]}, # original pathway without correction
        'THIAMIN':{'reactions':['AMPMS3','PMPK','THZPSN3','TMPPP','TMPK'],'stoichiometry':[1,1,1,1,1]},
        'COFACTOR_4':{'reactions':['I4FE4ST','I4FE4SR','I2FE2SS2'],'stoichiometry':[1,1,1]},
        'COFACTOR_5':{'reactions':['BMOGDS1','BMOGDS2','BMOCOS'],'stoichiometry':[1,1,1]},
        'COFACTOR_6':{'reactions':['DMPPS','GRTT','DMATT'],'stoichiometry':[1,1,1]},
        'COFACTOR_7':{'reactions':['MECDPS','DXPRIi','MEPCT','CDPMEK','MECDPDH5'],'stoichiometry':[1,1,1,1,1]},
        'COFACTOR_8':{'reactions':['LIPOS','LIPOCT'],'stoichiometry':[1,1]},
        'COFACTOR_9':{'reactions':['OMMBLHX','OMPHHX','OPHHX','HBZOPT','DMQMT','CHRPL','OMBZLM','OPHBDC','OHPHM'],'stoichiometry':[1,1,1,1,1,1,1,1,1]},
        'COFACTOR_10':{'reactions':['SERASr','DHBD','UPP3S','HMBS','ICHORT','DHBS'],'stoichiometry':[1,1,1,1,1,1]},
        'COFACTOR_11':{'reactions':['PMEACPE','EGMEACPR','DBTS','AOXSr2','I2FE2SR','OPMEACPD','MALCOAMT','AMAOTr','OPMEACPS','OPMEACPR','OGMEACPD','OGMEACPR','OGMEACPS','EPMEACPR','BTS5'],'stoichiometry':[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]},
        'CELLENV_1':{'reactions':['UAMAGS','UAPGR','UAGPT3','PAPPT3','GLUR','UAGCVT','UAMAS','UDCPDP','UGMDDS','UAAGDS'],'stoichiometry':[1,1,1,1,-1,1,1,1,1,1]},
        'CELLENV_2':{'reactions':['3HAD181','3OAR181','3OAS181','EAR181x'],'stoichiometry':[1,1,1,1]},
        'CELLENV_3':{'reactions':['3HAD160','3OAR160','EAR160x','3OAS160'],'stoichiometry':[1,1,1,1]},
        'CELLENV_4':{'reactions':['EAR120x','3OAR120','3HAD120','3OAS120','EAR100x'],'stoichiometry':[1,1,1,1,1]},
        'CELLENV_5':{'reactions':['G1PACT','UAGDP','PGAMT','GF6PTA'],'stoichiometry':[1,1,-1,1]},
        'CELLENV_6':{'reactions':['3OAR40','EAR40x','3OAS60','3OAR60','3HAD80','3OAS80','3OAR80','EAR60x','3HAD60','EAR80x','3HAD40'],'stoichiometry':[1,1,1,1,1,1,1,1,1,1,1]},
        'CELLENV_7':{'reactions':['3HAD161','EAR161x','3OAS161','3OAR161','3OAS141','3HAD141','3OAR121','EAR121x','3HAD121','EAR141x','T2DECAI','3OAR141','3OAS121'],'stoichiometry':[1,1,1,1,1,1,1,1,1,1,1,1,1]},
        'CELLENV_8':{'reactions':['TDPGDH','TDPDRR','TDPDRE','G1PTT'],'stoichiometry':[1,1,1,1]},
        'CELLENV_9':{'reactions':['3OAS140','3OAR140'],'stoichiometry':[1,1]},
        'CELLENV_10':{'reactions':['3HAD140','EAR140x'],'stoichiometry':[1,1]},
        'CELLENV_11':{'reactions':['3OAR100','3HAD100','3OAS100'],'stoichiometry':[1,1,1]},
        'LIPOPOLYSACCHARIDE_1':{'reactions':['COLIPAabcpp','COLIPAabctex','EDTXS1','EDTXS2','GALT1','GLCTR1','GLCTR2','GLCTR3','HEPK1','HEPK2','HEPT1','HEPT2','HEPT3','HEPT4','LPADSS','MOAT','MOAT2','MOAT3C','RHAT1','TDSK','USHD'],'stoichiometry':[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]},
        'LIPOPOLYSACCHARIDE_2':{'reactions':['AGMHE','GMHEPAT','GMHEPK','GMHEPPA','S7PI'],'stoichiometry':[1,1,1,1,1]},
        'LIPOPOLYSACCHARIDE_3':{'reactions':['U23GAAT','UHGADA','UAGAAT'],'stoichiometry':[1,1,1]},
        'LIPOPOLYSACCHARIDE_4':{'reactions':['KDOPP','KDOCT2','KDOPS'],'stoichiometry':[1,1,1]},
        'ASTPathway':{'reactions':['AST','SADH','SGDS','SGSAD','SOTA'],'stoichiometry':[1,1,1,1,1]}
        };
        return isotopomer_rxns_net
    def define_netRxns_RL2013_reversible(self):
        isotopomer_rxns_net = {
        'PTAr_ACKr_ACS':{'reactions':['PTAr','ACKr','ACS'],
                           'stoichiometry':[1,-1,-1]}, #acetate secretion
        'ACONTa_ACONTb':{'reactions':['ACONTa','ACONTb'],
                           'stoichiometry':[1,1]},
        'G6PDH2r_PGL':{'reactions':['G6PDH2r','PGL'],
                           'stoichiometry':[1,1]},
        'GAPD_PGK':{'reactions':['GAPD','PGK'], #glycolysis
                           'stoichiometry':[1,-1]},
        'PGM':{'reactions':['PGM','ENO'], #glycolysis
                           'stoichiometry':[-1,1]},
        'SUCCOAS':{'reactions':['SUCOAS'], #mispelling
                           'stoichiometry':[1]}
        #TODO: amino acid synthesis reactions
        };
        return isotopomer_rxns_net;
    def convert_netRxn2IndividualRxns(self,net_rxn_I,flux_I,flux_stdev_I,flux_lb_I,flux_ub_I,flux_units_I):
        '''Convert a net rxn into individual rxns,
        and update the direction of the flux for each individual reactions
        accordingly
        Input:
           net_rxn_I = string, rxn_id
           flux_I = flux, float
        Output:
           rxns_O = list, rxn_ids
           fluxes_O = list, floats
           fluxes_O_dict = dict, rxn_id:flux
        '''

        rxns_O = [];
        fluxes_O = [];
        fluxes_stdev_O,fluxes_lb_O,fluxes_ub_O,fluxes_units_O = [],[],[],[];

        if flux_I is None:
            #print('reaction has no flux');
            return rxns_O,fluxes_O,fluxes_stdev_O,fluxes_lb_O,fluxes_ub_O,fluxes_units_O;
        elif net_rxn_I in list(self.isotopomer_rxns_net.keys()):
            rxns_O = self.isotopomer_rxns_net[net_rxn_I]['reactions'];
            stoichiometry = self.isotopomer_rxns_net[net_rxn_I]['stoichiometry'];
            # change the direction of the fluxes according to the stoichiometry of the reactions
            fluxes_O = [s*flux_I for s in stoichiometry];
            fluxes_stdev_O = [flux_stdev_I for s in range(len(rxns_O))];
            fluxes_lb_O = [s*flux_lb_I for s in stoichiometry];
            fluxes_ub_O = [s*flux_ub_I for s in stoichiometry];
            fluxes_units_O = [flux_units_I for s in range(len(rxns_O))];
        else:
            #print('net reaction not found');
            return rxns_O,fluxes_O,fluxes_stdev_O,fluxes_lb_O,fluxes_ub_O,fluxes_units_O;

        return rxns_O,fluxes_O,fluxes_stdev_O,fluxes_lb_O,fluxes_ub_O,fluxes_units_O;