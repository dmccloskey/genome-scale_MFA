class MFA_utilities():
    def convert_fragmentAndElements2PositionAndElements(self,fragment_I,element_I):
        '''convert boolean fragment array representation of tracked atom positions to a numerical array representation'''
        positions_O = [];
        elements_O = [];
        cmap_cnt = 0;
        for i,f in enumerate(fragment_I):
            if f: 
                positions_O.append(cmap_cnt);
                elements_O.append(element_I[i]);
            cmap_cnt += 1;
        return positions_O,elements_O;