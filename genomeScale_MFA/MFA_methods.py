#System
from math import sqrt
#3rd party
import numpy as np
#Dependencies
from python_statistics.calculate_interface import calculate_interface
class MFA_methods():
    def calculate_totalFluxPrecision(self,flux_average_1,flux_stdev_1,flux_lb_1,flux_ub_1):
        '''calculate the total flux precision'''
        total_observable_stdev = 0.0;
        total_stdev = 0.0;
        for flux_cnt,flux_stdev in enumerate(flux_stdev_1):
            observable_1 = self.check_observableNetFlux(flux_average_1[flux_cnt],flux_lb_1[flux_cnt],flux_ub_1[flux_cnt])
            if observable_1 and flux_stdev:
                total_observable_stdev += flux_stdev;
            if flux_stdev:
                total_stdev += flux_stdev;
        return total_stdev,total_observable_stdev;
    def calculate_relativeNObservableNetFluxes(self,flux_average_1,flux_lb_1,flux_ub_1):
        '''calculate the number of unresolved fluxes'''
        cnt = 0;
        for flux_cnt,flux in enumerate(flux_average_1):
            observable_1 = self.check_observableNetFlux(flux_average_1[flux_cnt],flux_lb_1[flux_cnt],flux_ub_1[flux_cnt])
            if observable_1:
                cnt+=1;
        total_fluxes = len(flux_average_1);
        observable_fluxes = cnt;
        relative_n_observable_fluxes = float(cnt)/float(len(flux_average_1))
        return total_fluxes,observable_fluxes,relative_n_observable_fluxes;
    def calculate_averageNetFluxPrecision(self,flux_average_1,flux_stdev_1,flux_lb_1,flux_ub_1):
        '''calculate the average flux precision per reaction'''
        observable_total_stdev = 0.0;
        observable_cnt = 0;
        total_stdev = 0.0;
        cnt = 0;
        for flux_cnt,flux_stdev in enumerate(flux_stdev_1):
            observable_1 = self.check_observableNetFlux(flux_average_1[flux_cnt],flux_lb_1[flux_cnt],flux_ub_1[flux_cnt])
            if observable_1 and flux_stdev:
                observable_total_stdev += flux_stdev;
                observable_cnt+=1;
            if flux_stdev:
                total_stdev += flux_stdev;
                cnt+=1;
        average_observable_flux_precision = observable_total_stdev/float(observable_cnt);
        average_flux_precision = total_stdev/float(cnt);
        return average_flux_precision,average_observable_flux_precision;
    def calculate_relativeNObservableFluxes(self,flux_average_1,flux_lb_1,flux_ub_1):
        '''calculate the number of unresolved fluxes'''
        cnt = 0;
        for flux_cnt,flux in enumerate(flux_average_1):
            observable_1 = self.check_observableFlux(flux_average_1[flux_cnt],flux_lb_1[flux_cnt],flux_ub_1[flux_cnt])
            if observable_1:
                cnt+=1;
        total_fluxes = len(flux_average_1);
        observable_fluxes = cnt;
        relative_n_observable_fluxes = float(cnt)/float(len(flux_average_1))
        return total_fluxes,observable_fluxes,relative_n_observable_fluxes;
    def calculate_averageFluxPrecision(self,flux_average_1,flux_stdev_1,flux_lb_1,flux_ub_1):
        '''calculate the average flux precision per reaction'''
        observable_total_stdev = 0.0;
        observable_cnt = 0;
        total_stdev = 0.0;
        cnt = 0;
        for flux_cnt,flux_stdev in enumerate(flux_stdev_1):
            observable_1 = self.check_observableFlux(flux_average_1[flux_cnt],flux_lb_1[flux_cnt],flux_ub_1[flux_cnt])
            if observable_1 and flux_stdev:
                observable_total_stdev += flux_stdev;
                observable_cnt+=1;
            if flux_stdev:
                total_stdev += flux_stdev;
                cnt+=1;
        if observable_cnt > 0:
            average_observable_flux_precision = observable_total_stdev/float(observable_cnt);
        else:
            average_observable_flux_precision = None;
        average_flux_precision = total_stdev/float(cnt);
        return average_flux_precision,average_observable_flux_precision;
    def check_fluxRange(self,flux_I,flux_lb_I,flux_ub_I):
        '''Check the flux range'''
        flux_span = flux_ub_I-flux_lb_I;
        if flux_I==0.0 and flux_lb_I==0.0 and flux_ub_I==0.0:
            observable = False;
        elif flux_span > 4*flux_I:
            observable = False;
        else:
            observable = True;
        return observable;
    def check_observableNetFlux(self,flux_I,flux_lb_I,flux_ub_I):
        '''Determine if a flux is observable
        based on the criteria in doi:10.1016/j.ymben.2010.11.006'''
        if not flux_I:
            flux_I = 0.0;
        flux_span = max([flux_ub_I,flux_lb_I])-min([flux_ub_I,flux_lb_I]);
        if flux_I==0.0 and flux_lb_I==0.0 and flux_ub_I==0.0:
            observable = False;
        elif abs(flux_span) > 4*abs(flux_I):
            observable = False;
        else:
            observable = True;
        return observable;
    def check_observableFlux(self,flux_I,flux_lb_I,flux_ub_I):
        '''Determine if a flux is observable
        based on the criteria in doi:10.1016/j.ymben.2010.11.006'''
        flux_span = flux_ub_I-flux_lb_I;
        if flux_I==0.0 and flux_lb_I==0.0 and flux_ub_I==0.0:
            observable = False;
        elif flux_span > 4*flux_I and flux_lb_I == 0:
            observable = False;
        else:
            observable = True;
        return observable;
    def check_fluxLBAndUBBounds(self,flux_I,lower_bound_I,upper_bound_I):
        '''check that the flux is within the lower and upper bounds
        Output:
        within_bounds_O = boolean'''
        within_bounds_O = True;
        flux = flux_I;
        if flux < lower_bound_I:
            within_bounds_O = False;
        elif flux > upper_bound_I:
            within_bounds_O = False;
        return within_bounds_O;
    def calculate_fluxStdevFromLBAndUB(self,flux_lb_I,flux_ub_I):
        '''Calculate the standard deviation based off of the 95% confidence intervals
        described in doi:0.1016/j.ymben.2013.08.006'''
        flux_stdev = 0.0;
        try:
            flux_lb,flux_ub = self.correct_fluxLBAndUBDirection(flux_lb_I,flux_ub_I);
            flux_stdev = (flux_ub - flux_lb)/4;
        except TypeError as te:
            print(te);
        return flux_stdev;
    def calculate_fluxAverageFromLBAndUB(self,flux_I,flux_lb_I,flux_ub_I):
        '''correct the flux average if it is not within the lb/ub'''
        flux_average = flux_I;
        if flux_average and (flux_average < flux_lb_I or flux_average > flux_ub_I):
            flux_average = np.mean([flux_lb_I,flux_ub_I]);
        return flux_average;
    def substitute_zeroFluxForNone(self,flux_I):
        '''substitute 0.0 for None'''
        flux_average = flux_I;
        if flux_average == 0.0:
            flux_average = None;
        return flux_average;
    def calculate_fluxLBAndUBFromStdev(self,flux_I,flux_stdev_I):
        '''Calculate the flux lb and ub using the stdev'''
        
        flux_lb,flux_ub = None,None;
        if flux_I:
            flux_lb = flux_I - flux_stdev_I;
            flux_ub = flux_I + flux_stdev_I;
        elif flux_I==0.0:
            flux_lb = 0.0;
            flux_ub = 0.0;
        return flux_lb,flux_ub
    def calculate_fluxAverageFromLBAndUB(self,flux_lb_I,flux_ub_I):
        '''correct the flux average from the lb/ub'''

        flux_average = None
        flux_lb=flux_lb_I;
        flux_ub=flux_ub_I;
        if flux_lb and flux_ub:
            flux_average = np.mean([flux_lb,flux_ub]);
        return flux_average;
    def _calculate_netFlux_v1(self,flux_1,flux_stdev_1,flux_lb_1,flux_ub_1,flux_units_1,
                          flux_2,flux_stdev_2,flux_lb_2,flux_ub_2,flux_units_2,
                          lower_bound_I=-1000.0,upper_bound_I=1000.0,tolerance_I=1e-4):
        '''Calculate the net flux through a reaction,
        using the formula: vnet = v1-v2
        where "1" denotes the forward flux, and "2" denotes the reverse flux'''

        # determine if the fluxes are observable
        observable_1 = self.check_observableFlux(flux_1,flux_lb_1,flux_ub_1)
        observable_2 = self.check_observableFlux(flux_2,flux_lb_2,flux_ub_2)
        # calculate the net flux
        flux_average = flux_1-flux_2
        flux_stdev = sqrt(abs(flux_stdev_1*flux_stdev_1-flux_stdev_2*flux_stdev_2))
        # check the bounds of the fluxes
        flux_lb_1=self.adjust_fluxToRange(flux_lb_1,0.0,upper_bound_I);
        flux_lb_2=self.adjust_fluxToRange(flux_lb_2,0.0,upper_bound_I);
        flux_ub_1=self.adjust_fluxToRange(flux_ub_1,0.0,upper_bound_I);
        flux_ub_2=self.adjust_fluxToRange(flux_ub_2,0.0,upper_bound_I);
        #if flux_units_1=='' or not flux_units_2=='':
        #    print('PGI');
        # flux 1 and 2 are observable
        if observable_1 and observable_2:
            # note that both fluxes cannot be unbounded
            if flux_1 > upper_bound_I-upper_bound_I*tolerance_I and flux_2 > upper_bound_I-upper_bound_I*tolerance_I:
                print('both fluxes are unbounded')
                flux_average = None;
                flux_lb = lower_bound_I;
                flux_ub = upper_bound_I;
                #flux_lb = flux_lb_1-flux_lb_2
                #flux_ub = flux_ub_1-flux_ub_2
            elif flux_1 > upper_bound_I-upper_bound_I*tolerance_I: # flux 1 is unbounded
                flux_lb = flux_lb_1-flux_2
                flux_ub = flux_ub_1-0.0
            elif flux_2 > upper_bound_I-upper_bound_I*tolerance_I: # flux 2 is unbounded
                flux_lb = flux_1-flux_lb_2
                flux_ub = 0.0-flux_ub_2
            else:
                flux_lb = flux_lb_1-flux_lb_2
                flux_ub = flux_ub_1-flux_ub_2
            flux_units = flux_units_1;
        # flux 1 is observable, flux 2 is not observable, and flux 2 exists
        elif observable_1 and not observable_2 and flux_units_2!='':
            #flux_lb = flux_lb_1-flux_2
            #flux_ub = flux_ub_1-0.0
            flux_units = flux_units_1;
        # flux 2 is observable, flux 1 is not observable, and flux 1 exists
        elif observable_2 and not observable_1 and flux_units_1!='':
            flux_lb = flux_1-flux_lb_2
            flux_ub = 0.0-flux_ub_2
            flux_units = flux_units_2;
        # flux 1 is observable, flux 2 is not observable, and there is no flux 2
        elif observable_1 and not observable_2 and flux_units_2=='':
            flux_lb = flux_lb_1
            flux_ub = flux_ub_1
            flux_units = flux_units_1;
        # flux 2 is observable, flux 1 is not observable,, and there is no flux 1
        elif observable_2 and not observable_1 and flux_units_1=='':
            flux_lb = -flux_lb_2
            flux_ub = -flux_ub_2
            flux_units = flux_units_2;
        # flux 1 is not observable, and there is no flux 2
        elif not observable_1 and flux_units_2=='':
            flux_lb = flux_lb_1
            flux_ub = flux_ub_1
            flux_units = flux_units_1;
        # flux 2 is not observable,  and there is no flux 1
        elif not observable_2 and flux_units_1=='':
            flux_lb = -flux_ub_2
            flux_ub = -flux_lb_2
            flux_units = flux_units_2;
        # flux 1 is not observable, flux 2 is not observable, and flux 2 exists
        elif not observable_1 and not observable_2 and flux_units_2!='':
            flux_lb = lower_bound_I
            flux_ub = upper_bound_I
            flux_units = flux_units_1;
        # flux 2 is not observable, flux 1 is not observable, and flux 1 exists
        elif not observable_2 and not observable_1 and flux_units_1!='':
            flux_lb = lower_bound_I
            flux_ub = upper_bound_I
            flux_units = flux_units_2;
        # flux 1 is not observable and there is no flux 2
        elif not observable_1 and flux_units_2=='':
            #flux_lb = flux_lb_1
            #flux_ub = flux_ub_1
            flux_average = None;
            flux_lb = 0.0
            flux_ub = upper_bound_I
            flux_units = flux_units_1;
        # flux 2 is not observable and there is no flux 1
        elif not observable_2 and flux_units_1=='':
            #flux_lb = -flux_ub_2
            #flux_ub = -flux_lb_2
            flux_average = None;
            flux_lb = lower_bound_I
            flux_ub = 0.0
            flux_units = flux_units_2;
        ##elif not observable_1 and not flux_units_1 and not flux_units_2:
        ##    flux_average = None;
        ##    flux_lb = 0.0
        ##    flux_ub = upper_bound_I
        ##    flux_units = flux_units_1;
        ##elif not observable_2 and not flux_units_2:
        ##    flux_average = None;
        ##    flux_lb = lower_bound_I
        ##    flux_ub = 0.0
        ##    flux_units = flux_units_2;
        else:
            flux_average = None;
            #flux_average = 0.0;
            flux_lb = lower_bound_I
            flux_ub = upper_bound_I
            flux_units = 'mmol*gDCW-1*hr-1';
        # check the direction of the lower/upper bounds
        flux_lb,flux_ub = self.correct_fluxLBAndUBDirection(flux_lb,flux_ub);
        # check the bounds of the lb/ub
        flux_lb,flux_ub = self.correct_fluxLBAndUBBounds(flux_lb,flux_ub,lower_bound_I,upper_bound_I);
        # check the flux
        ## substitute 0.0 for None or change the flux average if it is not within the lb/ub
        #if flux_average == 0.0:
        #    flux_average = None;
        #elif flux_average and (flux_average < flux_lb or flux_average > flux_ub):
        #    flux_average = np.mean([flux_lb,flux_ub]);
        return flux_average,flux_stdev,flux_lb,flux_ub,flux_units
    def _calculate_netFlux_v2(self,flux_1,flux_stdev_1,flux_lb_1,flux_ub_1,flux_units_1,
                          flux_2,flux_stdev_2,flux_lb_2,flux_ub_2,flux_units_2,
                          lower_bound_I=-1000.0,upper_bound_I=1000.0,tolerance_I=1e-4):
        '''Calculate the net flux through a reaction,
        using the formula: vnet = v1-v2
        where "1" denotes the forward flux, and "2" denotes the reverse flux'''

        # determine if the fluxes are observable
        observable_1 = self.check_observableFlux(flux_1,flux_lb_1,flux_ub_1)
        observable_2 = self.check_observableFlux(flux_2,flux_lb_2,flux_ub_2)
        # calculate the net flux
        flux_average = flux_1-flux_2
        flux_stdev = sqrt(abs(flux_stdev_1*flux_stdev_1-flux_stdev_2*flux_stdev_2))
        # check the bounds of the fluxes
        flux_lb_1=self.adjust_fluxToRange(flux_lb_1,0.0,upper_bound_I);
        flux_lb_2=self.adjust_fluxToRange(flux_lb_2,0.0,upper_bound_I);
        flux_ub_1=self.adjust_fluxToRange(flux_ub_1,0.0,upper_bound_I);
        flux_ub_2=self.adjust_fluxToRange(flux_ub_2,0.0,upper_bound_I);
        #if flux_units_1=='' or not flux_units_2=='':
        #    print('PGI');
        # flux 1 and 2 are observable
        if observable_1 and observable_2:
            # note that both fluxes cannot be unbounded
            if flux_1 > upper_bound_I-upper_bound_I*tolerance_I and flux_2 > upper_bound_I-upper_bound_I*tolerance_I:
                print('both fluxes are unbounded')
                #flux_average = None;
                flux_average = 0.0;
                flux_lb = lower_bound_I;
                flux_ub = upper_bound_I;
                #flux_lb = flux_lb_1-flux_lb_2
                #flux_ub = flux_ub_1-flux_ub_2
            #elif flux_1 > upper_bound_I-upper_bound_I*tolerance_I: # flux 1 is unbounded
            #    flux_lb = flux_lb_1-flux_2
            #    flux_ub = flux_ub_1-0.0
            #elif flux_2 > upper_bound_I-upper_bound_I*tolerance_I: # flux 2 is unbounded
            #    flux_lb = flux_1-flux_lb_2
            #    flux_ub = 0.0-flux_ub_2
            else:
                flux_lb = flux_lb_1-flux_lb_2
                flux_ub = flux_ub_1-flux_ub_2
            flux_units = flux_units_1;
        # flux 1 is observable, flux 2 is not observable, and flux 2 exists
        elif observable_1 and not observable_2 and flux_units_2!='':
            #flux_lb = flux_lb_1-flux_2
            #flux_ub = flux_ub_1-0.0
            flux_lb = flux_lb_1-flux_lb_2
            flux_ub = flux_ub_1-flux_ub_2
            flux_units = flux_units_1;
        # flux 2 is observable, flux 1 is not observable, and flux 1 exists
        elif observable_2 and not observable_1 and flux_units_1!='':
            #flux_lb = flux_1-flux_lb_2
            #flux_ub = 0.0-flux_ub_2
            flux_lb = flux_lb_1-flux_lb_2
            flux_ub = flux_ub_1-flux_ub_2
            flux_units = flux_units_2;
        # flux 1 is observable, flux 2 is not observable, and there is no flux 2
        elif observable_1 and not observable_2 and flux_units_2=='':
            flux_lb = flux_lb_1
            flux_ub = flux_ub_1
            flux_units = flux_units_1;
        # flux 2 is observable, flux 1 is not observable,, and there is no flux 1
        elif observable_2 and not observable_1 and flux_units_1=='':
            flux_lb = -flux_lb_2
            flux_ub = -flux_ub_2
            flux_units = flux_units_2;
        # flux 1 is not observable, and there is no flux 2
        elif not observable_1 and flux_units_2=='':
            flux_lb = flux_lb_1
            flux_ub = flux_ub_1
            flux_units = flux_units_1;
        # flux 2 is not observable,  and there is no flux 1
        elif not observable_2 and flux_units_1=='':
            flux_lb = -flux_ub_2
            flux_ub = -flux_lb_2
            flux_units = flux_units_2;
        # flux 1 is not observable, flux 2 is not observable, and flux 2 exists
        elif not observable_1 and not observable_2 and flux_units_2!='':
            #flux_lb = lower_bound_I
            #flux_ub = upper_bound_I
            flux_lb = flux_lb_1-flux_lb_2
            flux_ub = flux_ub_1-flux_ub_2
            flux_units = flux_units_1;
        # flux 2 is not observable, flux 1 is not observable, and flux 1 exists
        elif not observable_2 and not observable_1 and flux_units_1!='':
            #flux_lb = lower_bound_I
            #flux_ub = upper_bound_I
            flux_lb = flux_lb_1-flux_lb_2
            flux_ub = flux_ub_1-flux_ub_2
            flux_units = flux_units_2;
        # flux 1 is not observable and there is no flux 2
        elif not observable_1 and flux_units_2=='':
            flux_lb = flux_lb_1
            flux_ub = flux_ub_1
            #flux_average = None;
            #flux_lb = 0.0
            #flux_ub = upper_bound_I
            flux_units = flux_units_1;
        # flux 2 is not observable and there is no flux 1
        elif not observable_2 and flux_units_1=='':
            flux_lb = -flux_ub_2
            flux_ub = -flux_lb_2
            #flux_average = None;
            #flux_lb = lower_bound_I
            #flux_ub = 0.0
            flux_units = flux_units_2;
        ##elif not observable_1 and not flux_units_1 and not flux_units_2:
        ##    flux_average = None;
        ##    flux_lb = 0.0
        ##    flux_ub = upper_bound_I
        ##    flux_units = flux_units_1;
        ##elif not observable_2 and not flux_units_2:
        ##    flux_average = None;
        ##    flux_lb = lower_bound_I
        ##    flux_ub = 0.0
        ##    flux_units = flux_units_2;
        else:
            #flux_average = None;
            flux_average = 0.0;
            flux_lb = lower_bound_I
            flux_ub = upper_bound_I
            flux_units = 'mmol*gDCW-1*hr-1';
        # check the direction of the lower/upper bounds
        flux_lb,flux_ub = self.correct_fluxLBAndUBDirection(flux_lb,flux_ub);
        # check the bounds of the lb/ub
        flux_lb,flux_ub = self.replace_zeroLBAndUBBounds(flux_lb,flux_ub,lower_bound_I,upper_bound_I);
        # check the flux
        ## substitute 0.0 for None or change the flux average if it is not within the lb/ub
        #if flux_average == 0.0:
        #    flux_average = None;
        #elif flux_average and (flux_average < flux_lb or flux_average > flux_ub):
        #    flux_average = np.mean([flux_lb,flux_ub]);
        return flux_average,flux_stdev,flux_lb,flux_ub,flux_units
    def _calculate_netFlux_v3(self,flux_1,flux_stdev_1,flux_lb_1,flux_ub_1,flux_units_1,
                          flux_2,flux_stdev_2,flux_lb_2,flux_ub_2,flux_units_2,
                          lower_bound_I=-1000.0,upper_bound_I=1000.0,tolerance_I=1e-4):
        '''Calculate the net flux through a reaction,
        using the formula: vnet = v1-v2
        where "1" denotes the forward flux, and "2" denotes the reverse flux'''

        ## determine if the fluxes are observable
        #observable_1 = self.check_observableFlux(flux_1,flux_lb_1,flux_ub_1)
        #observable_2 = self.check_observableFlux(flux_2,flux_lb_2,flux_ub_2)
        # ensure all fluxes have a value
        if flux_1 is None: flux_1 = 0.0;
        if flux_stdev_1 is None: flux_stdev_1 = 0.0;
        if flux_lb_1 is None: flux_lb_1 = 0.0;
        if flux_ub_1 is None: flux_ub_1 = 0.0;
        if flux_units_1 is None: flux_units_1 = '';
        if flux_2 is None: flux_2 = 0.0;
        if flux_stdev_2 is None: flux_stdev_2 = 0.0;
        if flux_lb_2 is None: flux_lb_2 = 0.0;
        if flux_ub_2 is None: flux_ub_2 = 0.0;
        if flux_units_2 is None: flux_units_2 = '';
        # initialize the output
        flux_average = 0.0;
        flux_stdev = 0.0;
        flux_lb = lower_bound_I;
        flux_ub = upper_bound_I;
        flux_units = '';
        # get the units
        if flux_units_1 !='': flux_units = flux_units_1;
        elif flux_units_2 !='': flux_units = flux_units_2;
        else: flux_units = '';
        # calculate the net flux
        flux_average = flux_1-flux_2
        flux_stdev = sqrt(abs(flux_stdev_1*flux_stdev_1-flux_stdev_2*flux_stdev_2))
        # check the bounds of the fluxes
        flux_lb_1=self.adjust_fluxToRange(flux_lb_1,0.0,upper_bound_I);
        flux_lb_2=self.adjust_fluxToRange(flux_lb_2,0.0,upper_bound_I);
        flux_ub_1=self.adjust_fluxToRange(flux_ub_1,0.0,upper_bound_I);
        flux_ub_2=self.adjust_fluxToRange(flux_ub_2,0.0,upper_bound_I);
        # calculate the lb/ub of the net flux
        flux_lb = flux_lb_1-flux_lb_2;
        flux_ub = flux_ub_1-flux_ub_2;
        # check the direction of the lower/upper bounds
        flux_lb,flux_ub = self.correct_fluxLBAndUBDirection(flux_lb,flux_ub);
        ## check the bounds of the lb/ub
        #check_bounds = self.check_fluxLBAndUBBounds(flux_average,flux_lb,flux_ub);
        #if not check_bounds:
        #    print('flux is not within the lower/upper bounds');
        #    statement = ('flux: %f, flux_lb: %f, flux_ub: %f' %(flux_average,flux_lb,flux_ub));
        #    print(statement);
        #    flux_lb,flux_ub = self.correct_fluxLBAndUBBounds(flux_average,flux_lb,flux_ub,lower_bound_I,upper_bound_I);

        return flux_average,flux_stdev,flux_lb,flux_ub,flux_units
    def calculate_netFlux(self,flux_1,flux_stdev_1,flux_lb_1,flux_ub_1,flux_units_1,
                          flux_2,flux_stdev_2,flux_lb_2,flux_ub_2,flux_units_2,
                          lower_bound_I=-1000.0,upper_bound_I=1000.0,tolerance_I=1e-4):
        '''Calculate the net flux through a reaction,
        using the formula: vnet = v1-v2
        where "1" denotes the forward flux, and "2" denotes the reverse flux'''

        ## determine if the fluxes are observable
        #observable_1 = self.check_observableFlux(flux_1,flux_lb_1,flux_ub_1)
        #observable_2 = self.check_observableFlux(flux_2,flux_lb_2,flux_ub_2)
        # ensure all fluxes have a value
        if flux_1 is None: flux_1 = 0.0;
        if flux_stdev_1 is None: flux_stdev_1 = 0.0;
        if flux_lb_1 is None: flux_lb_1 = 0.0;
        if flux_ub_1 is None: flux_ub_1 = 0.0;
        if flux_units_1 is None: flux_units_1 = '';
        if flux_2 is None: flux_2 = 0.0;
        #elif flux_2:
        #    print('check');
        if flux_stdev_2 is None: flux_stdev_2 = 0.0;
        if flux_lb_2 is None: flux_lb_2 = 0.0;
        if flux_ub_2 is None: flux_ub_2 = 0.0;
        if flux_units_2 is None: flux_units_2 = '';
        # initialize the output
        flux_average = 0.0;
        flux_stdev = 0.0;
        flux_lb = lower_bound_I;
        flux_ub = upper_bound_I;
        flux_units = '';
        # get the units
        if flux_units_1 !='': flux_units = flux_units_1;
        elif flux_units_2 !='': flux_units = flux_units_2;
        else: flux_units = '';
        # calculate the net flux
        flux_average = flux_1-flux_2
        flux_stdev = sqrt(abs(flux_stdev_1*flux_stdev_1-flux_stdev_2*flux_stdev_2))
        # calculate the lb/ub of the net flux
        flux_lb = max([flux_average-flux_stdev_1,flux_1-flux_stdev_1,flux_lb_1])-max([flux_average-flux_stdev_2,flux_2-flux_stdev_2,flux_lb_2]);
        flux_ub = min([flux_average+flux_stdev_1,flux_1+flux_stdev_1,flux_ub_1])-min([flux_average+flux_stdev_2,flux_2+flux_stdev_2,flux_ub_2]);
        # check the direction of the lower/upper bounds
        flux_lb,flux_ub = self.correct_fluxLBAndUBDirection(flux_lb,flux_ub);
        ## check the bounds of the lb/ub
        #check_bounds = self.check_fluxLBAndUBBounds(flux_average,flux_lb,flux_ub);
        #if not check_bounds:
        #    print('flux is not within the lower/upper bounds');
        #    statement = ('flux: %f, flux_lb: %f, flux_ub: %f' %(flux_average,flux_lb,flux_ub));
        #    print(statement);
        #    flux_lb,flux_ub = self.correct_fluxLBAndUBBounds(flux_average,flux_lb,flux_ub,lower_bound_I,upper_bound_I);

        return flux_average,flux_stdev,flux_lb,flux_ub,flux_units
    def correct_fluxLBAndUBDirection(self,flux_lb_I,flux_ub_I):
        '''correct the lb/ub directions'''
        flux_lb,flux_ub=flux_lb_I,flux_ub_I
        if flux_lb>flux_ub:
            flux_lb_tmp,flux_ub_tmp = flux_lb,flux_ub;
            flux_lb = flux_ub_tmp;
            flux_ub = flux_lb_tmp;
        return flux_lb,flux_ub;
    def adjust_fluxToRange(self,flux_I,lower_bound_I,upper_bound_I):
        '''correct the bounds
        if the flux is less than the lower bounds, the flux will be set at the lower bounds
        else if the flux is greater than the upper bounds, the flux will be set at the upper bounds'''
        flux = flux_I;
        if flux < lower_bound_I:
            flux = lower_bound_I;
        elif flux > upper_bound_I:
            flux = upper_bound_I;
        return flux;
    def replace_zeroLBAndUBBounds(self,flux_lb_I,flux_ub_I,lower_bound_I,upper_bound_I):
        '''replace lb/ub==0.0 with lower_bound_I and upper_bound_I'''
        flux_lb,flux_ub=flux_lb_I,flux_ub_I
        if flux_lb==0.0 and flux_ub==0.0:
            flux_lb = lower_bound_I;
            flux_ub = upper_bound_I;
        #if flux_lb<lower_bound_I:
        #    flux_lb = lower_bound_I;
        #if flux_ub>upper_bound_I:
        #    flux_ub = lower_bound_I;
        return flux_lb,flux_ub;
    def correct_fluxLBAndUBBounds_manuscripts(self,flux_I,flux_lb_I,flux_ub_I,lower_bound_I,upper_bound_I):
        '''correct the lb/ub bounds 
        case 1: when lb/ub==0.0 and flux!=0.0
        case 2: when flux < lb/ub and flux!=0.0
        case 3: when flux > lb/ub and flux!=0.0'''
        flux_lb,flux_ub = self.correct_fluxLBAndUBDirection(flux_lb_I,flux_ub_I);
        #flux_lb,flux_ub=flux_lb_I,flux_ub_I;
        if flux_I != 0.0 and flux_lb_I == 0.0 and flux_ub_I == 0.0:
            # case: flux_1 = 10.0, flux_2 = 0.0, flux_lb_1/2 = 0.0, flux_ub_1/2 = 1000.0
            if flux_I > 0.0:
                flux_lb = 0.0;
                flux_ub = upper_bound_I;
            else:
                flux_lb = lower_bound_I;
                flux_ub = 0.0;
        elif flux_I != 0.0 and flux_I<flux_lb_I and flux_I<flux_ub_I:
            # case: flux_1 = 10.0, flux_2 = 0.0, flux_lb_1 = 5, flux_lb_2 = 0, flux_ub_1/2 = 1000.0
            flux_lb = lower_bound_I;
            flux_ub = flux_lb_I;
        elif flux_I != 0.0 and flux_I>flux_lb_I and flux_I>flux_ub_I:
            # case: flux_1 = 10.0, flux_2 = 0.0, flux_lb_1 = 5, flux_lb_2 = 0, flux_ub_1/2 = 1000.0
            flux_lb = flux_ub_I;
            flux_ub = upper_bound_I;
        #else:
        #    print('case not supported');
        return flux_lb,flux_ub;
    def correct_fluxLBAndUBBounds(self,flux_I,flux_lb_I,flux_ub_I,lower_bound_I,upper_bound_I):
        '''correct the lb/ub bounds 
        case 1: when lb/ub==0.0 and flux!=0.0
        case 2: when flux < lb/ub and flux!=0.0
        case 3: when flux > lb/ub and flux!=0.0'''
        #flux_lb,flux_ub = self.correct_fluxLBAndUBDirection(flux_lb_I,flux_ub_I);
        flux_lb,flux_ub=flux_lb_I,flux_ub_I;
        # correct for lb/ub==0.0 and flux!=0.0
        if flux_I != 0.0 and flux_lb_I == 0.0 and flux_ub_I == 0.0:
            # case: flux_1 = 10.0, flux_2 = 0.0, flux_lb_1/2 = 0.0, flux_ub_1/2 = 1000.0
            if flux_I > 0.0:
                flux_lb = 0.0;
                flux_ub = upper_bound_I;
            else:
                flux_lb = lower_bound_I;
                flux_ub = 0.0;
            return flux_lb,flux_ub;
        # correct the lb and ub
        if flux_I != 0.0 and flux_I<flux_lb_I:
            flux_lb = lower_bound_I;
        if flux_I != 0.0 and flux_I>flux_ub_I:
            flux_ub = upper_bound_I;
        return flux_lb,flux_ub;
    def correct_fluxLBAndUBBounds_zeroLBAndUBonly(self,flux_I,flux_lb_I,flux_ub_I,lower_bound_I,upper_bound_I):
        '''correct the lb/ub bounds 
        case 1: when lb/ub==0.0 and flux!=0.0'''
        flux_lb,flux_ub=flux_lb_I,flux_ub_I;
        if flux_I != 0.0 and flux_lb_I == 0.0 and flux_ub_I == 0.0:
            # case: flux_1 = 10.0, flux_2 = 0.0, flux_lb_1/2 = 0.0, flux_ub_1/2 = 1000.0
            if flux_I > 0.0:
                flux_lb = 0.0;
                flux_ub = upper_bound_I;
            else:
                flux_lb = lower_bound_I;
                flux_ub = 0.0;
        return flux_lb,flux_ub;
    def correct_fluxLBAndUBBounds_greedy(self,flux_I,flux_lb_I,flux_ub_I,lower_bound_I,upper_bound_I,flux_stdev_I=None):
        '''correct the lb/ub bounds 
        case 1: when lb/ub==0.0 and flux!=0.0
        case 2: when flux < lb/ub and flux!=0.0
        case 3: when flux > lb/ub and flux!=0.0'''
        flux_lb,flux_ub=flux_lb_I,flux_ub_I;
        if flux_stdev_I is None:
            flux_stdev = self.calculate_fluxStdevFromLBAndUB(flux_lb_I,flux_ub_I);
        else:
            flux_stdev = flux_stdev_I;
        # correct for lb/ub==0.0 and flux!=0.0
        if flux_I != 0.0 and flux_lb_I == 0.0 and flux_ub_I == 0.0:
            # case: flux_1 = 10.0, flux_2 = 0.0, flux_lb_1/2 = 0.0, flux_ub_1/2 = 1000.0
            if flux_I > 0.0:
                flux_lb = 0.0;
                flux_ub = upper_bound_I;
            else:
                flux_lb = lower_bound_I;
                flux_ub = 0.0;
            return flux_lb,flux_ub;
        # correct the lb and ub
        if flux_I != 0.0 and flux_I<flux_lb_I:
            flux_lb = flux_I-flux_stdev;
        if flux_I != 0.0 and flux_I>flux_ub_I:
            flux_ub = flux_I+flux_stdev;
        return flux_lb,flux_ub;
    def calculate_fluxRatio(self,flux_1,flux_stdev_1,flux_lb_1,flux_ub_1,flux_units_1,
                          flux_2,flux_stdev_2,flux_lb_2,flux_ub_2,flux_units_2):
        '''Calculate the flux ratio between two reactions'''

        ratio,ratio_stdev,ratio_lb,ratio_ub,ratio_units=None,None,None,None,'';

        # check that the direction of the fluxes are the same
        #TODO

        if flux_1 and flux_2:
            ratio=flux_1/flux_2
            if flux_lb_1==0:
                flux_lb_numerator = flux_1-flux_stdev_1;
            else:
                flux_lb_numerator = flux_lb_1;
            if flux_lb_2==0:
                flux_lb_denominator = flux_2-flux_stdev_2;
            else:
                flux_lb_denominator = flux_lb_2;
            if flux_ub_1==0:
                flux_ub_numerator = flux_1+flux_stdev_1;
            else:
                flux_ub_numerator = flux_ub_1;
            if flux_ub_2==0:
                flux_ub_denominator = flux_2+flux_stdev_2;
            else:
                flux_ub_denominator = flux_ub_2;
            ratio_lb=min([flux_lb_numerator/flux_lb_denominator,flux_ub_numerator/flux_ub_denominator])
            ratio_ub=max([flux_lb_numerator/flux_lb_denominator,flux_ub_numerator/flux_ub_denominator])
            ratio_stdev=self.calculate_fluxStdevFromLBAndUB(ratio_lb,ratio_ub);
            ratio_units=flux_units_1+'/'+flux_units_2;
        else:
            print('invalid flux_1 or flux_2')

        return ratio,ratio_stdev,ratio_lb,ratio_ub,ratio_units
    def calculate_fluxSplit(self,flux_1,flux_stdev_1,flux_lb_1,flux_ub_1,flux_units_1,
                                    criteria_I = 'flux_lb/flux_ub'):
        '''Calculate the split % between two or more reactions
        INPUT:
        criteria_I = string, flux_lb/flux_ub: use flux_lb and flux_ub to determine the confidence intervals (default)
                             flux_mean/flux_stdev: use the flux_mean and flux_stdev to determine the confidence intervals        
        '''

        split,split_stdev,split_lb,split_ub,split_units=[],[],[],[],[];

        # check that the direction of the fluxes are the same
        #TODO
        flux_1_I = [];
        flux_lb_1_I = [];
        flux_ub_1_I = [];
        flux_cv_I = [];
        for flux_cnt,flux in enumerate(flux_1):
            if flux:
                flux_1_I.append(abs(flux));
                #if self.check_fluxRange(flux,flux_lb_1[flux_cnt],flux_ub_1[flux_cnt]):
                #    flux_lb_1_I.append(abs(flux_lb_1[flux_cnt]));
                #    flux_ub_1_I.append(abs(flux_ub_1[flux_cnt]));
                #else:
                #    flux_lb_1_I.append(None);
                #    flux_ub_1_I.append(None);
                flux_lb_1_I.append(abs(flux_lb_1[flux_cnt]));
                flux_ub_1_I.append(abs(flux_ub_1[flux_cnt]));
                if flux==0:
                    flux_cv_I.append(0.0);
                else:
                    flux_cv_I.append(flux_stdev_1[flux_cnt]/flux);
            else:
                flux_1_I.append(None);
                flux_lb_1_I.append(None);
                flux_ub_1_I.append(None);
                flux_cv_I.append(None);

        #calculate the total flux
        split_total = 0.0;
        for flux in flux_1_I:
            if flux:
                split_total+=flux;
        split_lb_total = 0.0;
        for flux in flux_lb_1_I:
            if flux:
                split_lb_total+=flux;
        split_ub_total = 0.0;
        for flux in flux_ub_1_I:
            if flux:
                split_ub_total+=flux;

        #calculate the flux percentage
        ##Method1:
        #for cnt,flux in enumerate(flux_1_I):
        #    if flux:
        #        if flux!=0:
        #            split_tmp = flux/split_total
        #            split.append(split_tmp);
        #            split_stdev_tmp=flux_stdev_1[cnt]/flux*split_tmp;
        #            split_stdev.append(split_stdev_tmp);
        #            if split_tmp-split_stdev_tmp<0.0:
        #                split_lb.append(0.0);
        #            else:
        #                split_lb.append(split_tmp-split_stdev_tmp);
        #            if split_tmp+split_stdev_tmp>1.0:
        #                split_ub.append(1.0);
        #            else:
        #                split_ub.append(split_tmp+split_stdev_tmp);
        #            split_units.append('split_fraction');
        #        elif flux==0:
        #            split_tmp = flux/split_total
        #            split.append(split_tmp);
        #            split_stdev.append(0.0);
        #            split_lb.append(0.0);
        #            split_ub.append(0.0);
        #            split_units.append('split_fraction');
        #    else:
        #        split.append(0.0);
        #        split_stdev.append(0.0);
        #        split_lb.append(0.0);
        #        split_ub.append(0.0);
        #        split_units.append('split_fraction');
        # Method 2:
        for cnt,flux in enumerate(flux_1_I):
            if flux and criteria_I == 'flux_lb/flux_ub':
                split_tmp = flux/split_total
                split.append(split_tmp);
                if not flux_lb_1_I[cnt] or split_lb_total==0.0:
                    split_lb_tmp=0.0;
                else:
                    split_lb_tmp=flux_lb_1_I[cnt]/split_lb_total;
                if not flux_ub_1_I[cnt] or split_ub_total==0.0:
                    split_ub_tmp=0.0;
                else:
                    split_ub_tmp=flux_ub_1_I[cnt]/split_ub_total;
                split_lb.append(min([split_lb_tmp,split_ub_tmp]))
                split_ub.append(max([split_lb_tmp,split_ub_tmp]))
                split_stdev_tmp = flux_cv_I[cnt]*split_tmp
                split_stdev.append(split_stdev_tmp);
                #split_stdev.append(self.calculate_fluxStdevFromLBAndUB(min([split_lb_tmp,split_ub_tmp]),max([split_lb_tmp,split_ub_tmp])));
                split_units.append('split_fraction');
            elif flux and criteria_I == 'flux_mean/flux_stdev':
                split_tmp = flux/split_total
                split.append(split_tmp);
                split_lb_tmp = split_tmp-flux_cv_I[cnt]*split_tmp;
                split_ub_tmp = split_tmp+flux_cv_I[cnt]*split_tmp;
                split_lb.append(min([split_lb_tmp,split_ub_tmp]))
                split_ub.append(max([split_lb_tmp,split_ub_tmp]))
                split_stdev_tmp = flux_cv_I[cnt]*split_tmp;
                split_stdev.append(split_stdev_tmp);
                split_units.append('split_fraction');
            else:
                split.append(0.0);
                split_stdev.append(0.0);
                split_lb.append(0.0);
                split_ub.append(0.0);
                split_units.append('split_fraction');

        for cnt,s in enumerate(split):
            # check the bounds of the fluxes
            split_lb[cnt]=self.adjust_fluxToRange(split_lb[cnt],0.0,1.0);
            split_ub[cnt]=self.adjust_fluxToRange(split_ub[cnt],0.0,1.0);

        return split,split_stdev,split_lb,split_ub,split_units
    def check_criteria(self,flux_1,flux_stdev_1,flux_lb_1,flux_ub_1,criteria_I):
        """check if all the data is present to determine significance based on the criteria"""
        criteria_check = False;
        if criteria_I == 'flux_lb/flux_ub':
            if flux_lb_1 and flux_ub_1: 
                criteria_check = True;
        elif criteria_I == 'flux_mean/flux_stdev':
            if flux_1 and flux_stdev_1: 
                criteria_check = True;
        else:
            print('criteria not recognized!');
        return criteria_check;
    def determine_fluxDifferenceSignificance(self,flux_lb_1,flux_ub_1,flux_lb_2,flux_ub_2):
        """determine whether the difference between two fluxes is signifcant based on the lb and ub"""
        significant = False;
        if flux_lb_1 < flux_lb_2 and flux_ub_1 < flux_lb_2:
            significant = True;
        elif flux_lb_1 > flux_ub_2 and flux_ub_1 > flux_ub_2:
            significant = True;
        else:
            significant = False;
        return significant;
    def calculate_fluxDifference(self,flux_1,flux_stdev_1,flux_lb_1,flux_ub_1,flux_units_1,
                                                                            flux_2,flux_stdev_2,flux_lb_2,flux_ub_2,flux_units_2,
                                                                            criteria_I = 'flux_lb/flux_ub'):
        """Calculate flux differences and deterimine if the differences are significant
        Input:
        flux_1 = data for flux 1 to be compared
        ...
        flux_2 = data for flux 2 to be compared
        ... 
        criteria_I = string, flux_lb/flux_ub: use flux_lb and flux_ub to determine significance (default)
                             flux_mean/flux_stdev: use the flux_mean and flux_stdev to determine significance

        Output:
        flux_diff = relative flux difference, float
        flux_distance = geometric difference, (i.e., distance)
        fold_change = geometric fold change
        significant = boolean
    
        """
        calc = calculate_interface();
        flux_diff = 0.0;
        flux_distance = 0.0;
        significant = False;
        fold_change = 0.0;
        if criteria_I == 'flux_lb/flux_ub':
            flux_mean_1 = np.mean([flux_lb_1,flux_ub_1]);
            flux_mean_2 = np.mean([flux_lb_2,flux_ub_2]);
            flux_diff = calc.calculate_difference(flux_mean_1,flux_mean_2,type_I='relative');
            flux_distance = calc.calculate_difference(flux_mean_1,flux_mean_2,type_I='geometric');
            fold_change = calc.calculate_foldChange(flux_mean_1,flux_mean_2,type_I='geometric');
            significant = self.determine_fluxDifferenceSignificance(flux_lb_1,flux_ub_1,flux_lb_2,flux_ub_2);
        elif criteria_I == 'flux_mean/flux_stdev':
            flux_diff = calc.calculate_difference(flux_1,flux_2,type_I='relative');
            flux_distance = calc.calculate_difference(flux_1,flux_2,type_I='geometric');
            fold_change = calc.calculate_foldChange(flux_1,flux_2,type_I='geometric');
            flux_lb_1 = flux_1 - flux_stdev_1;
            flux_lb_2 = flux_2 - flux_stdev_2;
            flux_ub_1 = flux_1 + flux_stdev_1;
            flux_ub_2 = flux_2 + flux_stdev_2;
            significant = self.determine_fluxDifferenceSignificance(flux_lb_1,flux_ub_1,flux_lb_2,flux_ub_2);
        else:
            print('criteria not recognized!');
        return flux_diff,flux_distance,fold_change,significant;
    def calculate_exchangeFlux(self,flux_1,flux_stdev_1,flux_lb_1,flux_ub_1,flux_units_1,
                          flux_2,flux_stdev_2,flux_lb_2,flux_ub_2,flux_units_2,
                          flux_net,flux_stdev_net,flux_lb_net,flux_ub_net,flux_units_net,
                          lower_bound_I=0.0,upper_bound_I=1000.0,tolerance_I=1e-4):
        '''Calculate the exchange flux of a net reaction,
        using the following formulas:
            vexch = min(v1,v2);
            vexch_norm = vexch/(|vnet| + vexch)*100%
        where "1" denotes the forward flux, and "2" denotes the reverse flux
        INPUT:
        flux_1 ...
        flux_2 ...
        flux_net = calculated net flux
        flux_stdev_net = calculated net flux standard deviation
        flux_lb_net =  calculated net flux lower bound
        flux_ub_net = calculated net flux upper bound
        flux_units_net = calculated net flux units

        '''

        #initialize all output variables
        flux_exchange = 0.0;
        flux_exchange_stdev = 0.0;
        flux_exchange_lb = 0.0;
        flux_exchange_ub = 0.0;
        flux_exchange_units = '';
        flux_exchange_norm = 0.0;
        flux_exchange_norm_stdev = 0.0;
        flux_exchange_norm_lb = 0.0;
        flux_exchange_norm_ub = 0.0;
        flux_exchange_norm_units = 'netFlux_normalized';

        #if flux_units_1=='' or not flux_units_2=='':
        #    print('check');

        ## determine if the fluxes are observable
        #observable_1 = self.check_observableFlux(flux_1,flux_lb_1,flux_ub_1)
        #observable_2 = self.check_observableFlux(flux_2,flux_lb_2,flux_ub_2)
        # calculate and identify the exchange flux
        #flux_exchange = np.min([flux_1,flux_2]);
        if flux_1 == 0.0 and flux_units_1 == '' and flux_2 == 0.0 and flux_units_2 == '':
            # there is no forward or reverse fluxes
            return flux_exchange,flux_exchange_stdev,flux_exchange_lb,flux_exchange_ub,flux_exchange_units,flux_exchange_norm,flux_exchange_norm_stdev,flux_exchange_norm_lb,flux_exchange_norm_ub,flux_exchange_norm_units;
        elif flux_1 == 0.0 and flux_units_1 == '':
            # there is no forward flux
            flux_exchange_units = flux_units_2;
            return flux_exchange,flux_exchange_stdev,flux_exchange_lb,flux_exchange_ub,flux_exchange_units,flux_exchange_norm,flux_exchange_norm_stdev,flux_exchange_norm_lb,flux_exchange_norm_ub,flux_exchange_norm_units;
        elif flux_2 == 0.0 and flux_units_2 == '':
            # there is no reverse flux
            flux_exchange_units = flux_units_1;
            return flux_exchange,flux_exchange_stdev,flux_exchange_lb,flux_exchange_ub,flux_exchange_units,flux_exchange_norm,flux_exchange_norm_stdev,flux_exchange_norm_lb,flux_exchange_norm_ub,flux_exchange_norm_units;
        elif flux_1>flux_2:
            flux_exchange = flux_2
            flux_exchange_stdev = flux_stdev_2
            flux_exchange_lb = flux_lb_2
            flux_exchange_ub = flux_ub_2
            flux_exchange_units = flux_units_2
        else:
            flux_exchange = flux_1
            flux_exchange_stdev = flux_stdev_1
            flux_exchange_lb = flux_lb_1
            flux_exchange_ub = flux_ub_1
            flux_exchange_units = flux_units_1
        ## check the bounds of the fluxes
        #flux_exchange_lb=self.adjust_fluxToRange(flux_exchange_lb,lower_bound_I,upper_bound_I);
        #flux_exchange_ub=self.adjust_fluxToRange(flux_exchange_ub,lower_bound_I,upper_bound_I);
        # calculate the normalized exchange flux
        if flux_net!=0.0: flux_exchange_norm = flux_exchange/(abs(flux_net)+flux_exchange);
        # calculate the lower and upper bounds of the normalized exchange flux
        ##method 1:
        #if flux_lb_net!=0.0: flux_exchange_norm_lb = flux_exchange_lb/(abs(flux_lb_net)+flux_exchange_lb);
        #if flux_ub_net!=0.0: flux_exchange_norm_ub = flux_exchange_ub/(abs(flux_ub_net)+flux_exchange_ub);
        #method 2: (does not account for the error in the net flux)
        if flux_net!=0.0: flux_exchange_norm_lb = flux_exchange_lb/(abs(flux_net)+flux_exchange_lb);
        if flux_net!=0.0: flux_exchange_norm_ub = flux_exchange_ub/(abs(flux_net)+flux_exchange_ub);
        # check the bounds of the fluxes
        flux_exchange_norm_lb=self.adjust_fluxToRange(flux_exchange_norm_lb,0.0,1.0);
        flux_exchange_norm_ub=self.adjust_fluxToRange(flux_exchange_norm_ub,0.0,1.0);
        # check the direction of the lower/upper bounds
        flux_exchange_norm_lb,flux_exchange_norm_ub = self.correct_fluxLBAndUBDirection(flux_exchange_norm_lb,flux_exchange_norm_ub);
        # check the bounds of the lb/ub
        flux_exchange_norm_lb,flux_exchange_norm_ub = self.replace_zeroLBAndUBBounds(flux_exchange_norm_lb,flux_exchange_norm_ub,0.0,1.0);
        # calculate the std dev from the lb/ub
        flux_exchange_norm_stdev = self.calculate_fluxStdevFromLBAndUB(flux_exchange_norm_lb,flux_exchange_norm_ub);

        return flux_exchange,flux_exchange_stdev,flux_exchange_lb,flux_exchange_ub,flux_exchange_units,flux_exchange_norm,flux_exchange_norm_stdev,flux_exchange_norm_lb,flux_exchange_norm_ub,flux_exchange_norm_units;
    def normalize_flux(self,rxn_id_norm,flux_norm,flux_stdev_norm,flux_lb_norm,flux_ub_norm,flux_1,flux_stdev_1,flux_lb_1,flux_ub_1):
        '''Normalize a flux to a given flux'''

        flux_O = None
        flux_stdev_O = None
        flux_lb_O = None
        flux_ub_O = None
        flux_units_O = '';

        if flux_1 != 0.0:
            flux_O = flux_1/flux_norm
            flux_stdev_O = flux_stdev_1/flux_1*flux_O #recompute the new stdev from the %RSD of the orginal measurement
            flux_lb_O = flux_lb_1/flux_norm
            flux_ub_O = flux_ub_1/flux_norm
        elif flux_1 == 0.0:
            flux_O = flux_1/flux_norm
            flux_stdev_O = flux_stdev_1 #transfer the original stdDev
            flux_lb_O = flux_lb_1/flux_norm
            flux_ub_O = flux_ub_1/flux_norm
        else:
            print("reaction does not have a flux!")
            return flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O

        flux_units_O = rxn_id_norm + '_normalized'
        return flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O