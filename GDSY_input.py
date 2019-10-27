def GDSY_input(db_file, log_data):

    import pyodbc
    
    proj, hole, depth, descr, samples, gw = log_data
    
    #you have to make sure this driver is installed on the PC, be careful as
    #this might not work if the driver is 32-bit and the Python version is
    #64-bit. Can check if driver is on PC by searching for 'ODBC Data Sources'.
    #Can download 64-bit driver from microsoft.
    odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;'\
                    %(db_file)
    conn = pyodbc.connect(odbc_conn_str)

    cursor = conn.cursor()

    for i in range(0, len(depth)):
        
    #This statement is in SQL and is the one that makes stuff happen.
        sql_select_statement = "insert into GEOL (PROJ_ID, HOLE_ID, GEOL_TOP, \
GEO_DESC) values ('%s', '%s', '%s', '%s')" %(proj, hole, depth[i], descr[i])

        cursor.execute(sql_select_statement)
        cursor.commit()

    check_statement = "select PROJ_ID from PROJ where PROJ_ID='%s'" %(proj)
    cursor.execute(check_statement)
    proj_check = cursor.fetchall()
    cursor.commit()

    if proj_check == []:
        proj_statement = "insert into PROJ (PROJ_ID) values ('%s')" %(proj)
        cursor.execute(proj_statement)
        cursor.commit()

    if len(samples) > 1:
        
        d_count = 0
        b_count = 0
        u_count = 0
        es_count = 0
        ew_count = 0
        sample_ref = ''
        
        for sample_depth, sample_type in samples.items():

            if sample_type == 'D':
                d_count += 1
                sample_ref = 'D' + str(d_count)

            elif sample_type == 'B':
                b_count += 1
                sample_ref = 'B' + str(b_count)

            elif sample_type == 'U':
                u_count += 1
                sample_ref = 'U' + str(u_count)

            elif sample_type == 'ES':
                es_count += 1
                sample_ref = 'ES' + str(es_count)

            elif sample_type == 'EW':
                ew_count += 1
                sample_ref = 'EW' + str(ew_count)

            sample_statement = "insert into SAMP (PROJ_ID, HOLE_ID, SAMP_TOP, \
SAMP_REF, SAMP_TYPE) values ('%s', '%s', '%s', '%s', '%s')" %(proj, hole, \
            sample_depth, sample_ref, sample_type)
            cursor.execute(sample_statement)
            cursor.commit()

    if len(gw) > 0:
        for i in range(len(gw)):
            gw_statement = "insert into GWATER (PROJ_ID, HOLE_ID, SRUCK) values \
('%s', '%s', '%s')" %(proj, hole, gw[i])
            cursor.execute(gw_statement)
            cursor.commit()
        
    cursor.close()
    conn.close()


