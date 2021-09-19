def execute_inversion(iterations, *args, **kwargs):
    print(f"This is where we would have a translation or wrapper of inver.f \
            {kwargs['ambient_field']}")

    
    # Line 159 inver.f
    for i in range(0, kwargs["nstat"]):
        k = stat*1
        for j in range(0, kwargs["npoly"]):
            sgn = 1
            sgm = 1
            
            if(densty[j] < 0.0):
                sgn = -1.0
            if(suscp[j] < 0.0):
                sgm = -1.0
            
            nd = nden[j]
            ns = nsus[j]

            if(nd != 0):
                a1[i, nd] = a1[i, nd] + gte[j,i]*sgn
            if(ns != 0):
                a1[k, ns] = a1[k, ns] + mte[j, i]*sgm
            
            mtot[i] = mtot[i] + mte[j,i]*suscp[j]
            gtot[i] = gtot[i] + gte[j, i]*densty[j]*ct

            gtr = gtot[nbase] - grav[nbase]
            mtr = mtot[nbase] - mag[nbase]

            ssrm = 0.0
            ssr = 0.0

            for i in range(0, nstat):
                gtot[i] = gtot[i] - gtr
                gdif[i] = grav[i] - gtot[i]
                difsq = gdif[i]**2
                ssr = ssr + difsq
                ssrm = ssrm + difsq
                chisq = (ssr/vg)+(ssrm/vm)
    
    print(f"The new parameters are {iiw}")




