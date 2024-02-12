# -------------------------------------------------------------------------|--
# -------------------------------------------------------------------------|--

import csv
import os
import os.path
import py_compile
import math 
import pickle
import networkx as nx
import numpy as np
import datetime
import spatialite
import sqlite3
import json
from zipfile import ZIP_DEFLATED, ZipFile

# -------------------------------------------------------------------------|--

#
# ### KN3INIT
#

# -------------------------------------------------------------------------|--

def kn3init(imW, style_dir):
    '''
    Inicializacija za potrebe Modela KN3.

    '''
    answ = dict()
    #
    # datoteka_projekta 'G:\\00eimv\\kn3\\data\\ecelje\\bocc\\kantri.qgz'
    # head              'G:\\00eimv\\kn3\\data\\ecelje\\bocc'
    # tail              'kantri.qgz'
    # osnovni_dir       'G:\\00eimv\\kn3\\data\\ecelje\\bocc'
    # model_dir         'G:\\00eimv\\kn3\\data\\ecelje\\bocc\\model'
    #
    QPi = QgsProject.instance()
    #
    datoteka_projekta = QPi.fileName()
    head, tail = os.path.split(datoteka_projekta)
    #
    osnovni_dir = head
    answ['osnovni_dir'] = osnovni_dir
    #
    model_dir = os.path.join(osnovni_dir, 'MODELX')
    if not os.path.isdir(model_dir):
        os.mkdir(model_dir)
    answ['model_dir'] = model_dir
    #
    crs_3794 = QgsCoordinateReferenceSystem.fromEpsgId(3794)
    answ['crs_3794'] = crs_3794
    #
    spe = {}
    spe['FiGOV'] = 0.80
    spe['FpOOV'] = 0.80
    spe['Fpnesk'] = 0.2222 # faktor prekrivanja
    spe['Vmin'] = 0.075    # dopustni padec napetosti
    spe['GOIkW'] = 10.0    # 1 GOI == 10.0 kW
    spe['sw_tocr'] = True
    spe['tocr'] = 0.5
    answ['spe'] = spe
    #
    answ['TR'] =  'St {:.1f} kVA, uk {:.2f} %, Pcu {:.3f} kW, vez {:}'
    answ['ETIS'] = '\nElapsed time is {:.1f} seconds.'
    answ['U230'] = 400 / math.sqrt(3)
    #
    # kw_1x25 = 25 * (400 / sqrt(3)) * 1 / 1000                    #  5.8 kW
    # kw_3x20 = 20 * (400 / sqrt(3)) * 3 / 1000                    # 13.9 kW
    # kw_3x25 = 25 * (400 / sqrt(3)) * 3 / 1000                    # 17.3 kW
    #
    answ['kw_1x25'] =  5.5                                              # kW
    answ['kw_3x20'] = 13.5                                              # kW
    answ['kw_3x25'] = 17.5                                              # kW
    #
    vozliscadef = {
            'ID': 'INTEGER',
            'jd': 'TEXT',
            'tip': 'TEXT',
            'nGOI_0': 'INTEGER',
            'Pvel_0': 'REAL',
            'P_0': 'REAL',
            'Pdod_0': 'REAL',
            'Pele_0': 'REAL',
            'nGOI':  'INTEGER',
            'Pvel': 'REAL',
            'P': 'REAL',
            'W_kWh': 'REAL',
            'W_0_kWh': 'REAL',
            'T0_h':  'INTEGER',
            'Tizg_h':  'INTEGER',
            'Pdod': 'REAL',
            'Pele': 'REAL',
            'UTP': 'REAL',
            'U': 'REAL',
            'dUrel': 'REAL',
            'dUelerel': 'REAL',
            'distTP': 'REAL',
            'resisTP': 'REAL',
            'conducTP': 'REAL',
            'dP': 'REAL',
            'dP_0': 'REAL',
            'dW_kWh': 'REAL',
            'dW_0_kWh': 'REAL',
            'dW_proc': 'REAL',
            'dispod': 'TEXT',
            'nnotp': 'TEXT',
            'izvod': 'TEXT',
            'level': 'INTEGER',
            'original': 'TEXT',
            'naziv': 'TEXT',
            'Zdir': 'REAL',
            'Znic': 'REAL',
            'Zekv': 'REAL',
            'S_SN': 'REAL',
            'exclude': 'INTEGER',
            'opomba': 'TEXT',
            'time': 'TEXT'
    }
    povezavedef = {
            'ID': 'INTEGER',
            'ID1': 'INTEGER',
            'ID2': 'INTEGER',
            'jd1': 'TEXT',
            'jd2': 'TEXT',
            'dolz': 'REAL',
            'dolztop': 'REAL',
            'mat': 'TEXT',
            'presek': 'REAL',
            'Imax': 'REAL',
            'rspec': 'REAL',
            'resis': 'REAL',
            'cspec': 'REAL',
            'conduc': 'REAL',
            'nGOI': 'INTEGER',
            'Pvel': 'REAL',
            'Pdod': 'REAL',
            'P': 'REAL',
            'W_kWh': 'REAL',
            'T0_h': 'INTEGER',
            'Tizg_h': 'INTEGER',
            'Pele': 'REAL',
            'Ib': 'REAL',
            'Irel': 'REAL',
            'Iele': 'REAL',
            'Ielerel': 'REAL',
            'dUrel': 'REAL',
            'dUelerel': 'REAL',
            'dP_0': 'REAL',
            'dP': 'REAL',
            'dW_kWh': 'REAL',
            'dW_0_kWh': 'REAL',
            'dW_proc': 'REAL',
            'dispod': 'TEXT',
            'nnotp': 'TEXT',
            'izvod': 'TEXT',
            'multi': 'INTEGER',
            'level': 'INTEGER',
            'original': 'TEXT',
            'Ik1': 'REAL',
            'Ik3': 'REAL',
            'Ia': 'REAL',
            'Iaa': 'REAL',
            'Iv': 'REAL',
            'opomba': 'TEXT',
            'trafo': 'TEXT',
            'exclude': 'INTEGER',
            'sw_zbiralka': 'INTEGER',
            'time': 'TEXT'
    }
    dodaj_shp_in_inicijaliziraj(vozliscadef)
    dodaj_shp_in_inicijaliziraj(povezavedef)
    #
    answ['vozliscadef'] = vozliscadef
    answ['povezavedef'] = povezavedef
    #
    pth = os.path.join(
            model_dir, 'KANTRIX.sqlite')
    #
    if not os.path.exists(pth):
        create_kantrix_db(pth, vozliscadef, povezavedef)
    #
    _ = pth + '|layername=POVEZAVEX'
    lyrP = QgsVectorLayer(_, 'POVEZAVEX', 'ogr')
    if not lyrP.isValid():
        QMessageBox.critical(imW, 'ku', 'POVEZAVEX neveljavna')
    if 'POVEZAVEX' not in get_present_layers(QPi):
        _ = os.path.join(
                style_dir, 'povezave 00 osnovni.qml')
        lyrP.loadNamedStyle(_)
        QPi.addMapLayer(lyrP)
    lyrP = QPi.mapLayersByName('POVEZAVEX')[0]
    x = QgsLayerTreeLayer(lyrP)
    x.setCustomProperty("showFeatureCount", True)
    #
    answ['lyrP'] = lyrP
    answ['prP'] = lyrP.dataProvider()
    answ['fldsP'] = lyrP
    #
    _ = pth + '|layername=VOZLISCAX'
    lyrV = QgsVectorLayer(_, 'VOZLISCAX', 'ogr')
    if not lyrV.isValid():
        QMessageBox.critical(imW, 'ku', 'VOZLISCAX neveljavna')
    if 'VOZLISCAX' not in get_present_layers(QPi):
        _ = os.path.join(style_dir, 'vozlisca 00 osnovni.qml')
        lyrV.loadNamedStyle(_)
        QPi.addMapLayer(lyrV)
    lyrV = QPi.mapLayersByName('VOZLISCAX')[0]
    #
    answ['lyrV'] = lyrV
    answ['prV'] = lyrV.dataProvider()
    answ['fldsV'] = lyrV.fields()

    return answ

# -------------------------------------------------------------------------|--

def create_kantrix_db(pth, vozliscadef, povezavedef):
    #
    # conn = sqlite3.connect(pth)
    conn = spatialite.connect(pth)
    #
    conn.enable_load_extension(True)
    conn.execute('''SELECT load_extension('mod_spatialite')''')
    conn.execute('''SELECT InitSpatialMetaData(1);''')
    #
    cur = conn.cursor()
    #
    # cur.execute('''
        # DROP TABLE IF EXISTS VOZLISCAX''')
    #
    create_table = 'CREATE TABLE IF NOT EXISTS VOZLISCAX('
    for k, v in vozliscadef.items():
        vv = v[0]
        create_table =  f'{create_table:s}\n        {k:s} {vv:s},'
    create_table = create_table[:-1] + ')'
    cur.execute(create_table)
    #
    cur.execute('''
        SELECT AddGeometryColumn(
            'VOZLISCAX', 'geom', 3794, 'POINT', 'XY')''')
    #
    # cur.execute('''DROP TABLE IF EXISTS POVEZAVEX''')
    #
    create_table = 'CREATE TABLE IF NOT EXISTS POVEZAVEX('
    for k, v in povezavedef.items():
        vv = v[0]
        create_table =  f'{create_table:s}\n        {k:s} {vv:s},'
    create_table = create_table[:-1] + ')'
    cur.execute(create_table)
    #
    cur.execute('''
        SELECT AddGeometryColumn(
            'POVEZAVEX', 'geom', 3794, 'MULTILINESTRING', 'XY')''')
    #
    cur.close()
    #
    conn.commit()
    conn.close()

# -------------------------------------------------------------------------|--

def dodaj_shp_in_inicijaliziraj(sloj):
    for k, v in sloj.items():
        if v == 'INTEGER':
            _ = {'type': 'QVariant.Int', 'len': 12}
            sloj[k] = (v, _, 0)
        elif v == 'REAL':
            _ = {'type': 'QVariant.Double', 'prec': 3, 'len': 12}
            sloj[k] = (v, _, 0.)
        elif v == 'TEXT':
            _ = {'type': 'QVariant.String', 'len': 30}
            sloj[k] = (v, _, '/')
        else:
            print(f'rutina: dodaj_shp_in_inicijaliziraj\nerror: {v}')

# -------------------------------------------------------------------------|--

#
# ### QGIS_TO_NXNX
#

# -------------------------------------------------------------------------|--

def qgis_to_nxnx(lyrV, lyrP, model_dir=None):
    '''
    Prečita VOZLISCA & POVEZAVE (QGIS) v [ nx.DiGraph() ].
    
    '''
    # print('\nQGIS_TO_NXNX')
    #
    vozlisca = lyr_to_list(lyrV, model_dir)
    povezave = lyr_to_list(lyrP, model_dir)
    #
    popravi_editorske_premike(vozlisca, povezave)
    #
    fff = multi_graph(vozlisca, povezave)
    #
    hh = expand(fff)
    #
    return hh

# -------------------------------------------------------------------------|--
# -1-----------------------------------------------------------------------|--
# -------------------------------------------------------------------------|--

def popravi_editorske_premike(vozlisca, povezave):
    """
    Vskladi imena in lokacije vozlišč.
    
    """
    for vozlisce in vozlisca:
        jd = vozlisce['jd']
        vozlisce['point'] = to_point(jd)
    #
    for vozlisce in vozlisca:
        jd = vozlisce['jd']
        point_new = vozlisce['point']
        jd_new = to_jd(point_new) 
        if jd != jd_new:                                  # ni na pravem mestu
            vozlisce['jd'] = jd_new
            for povezava in povezave:                    # še dotične povezave
                jd1 = povezava['jd1']
                jd2 = povezava['jd2']
                if jd == jd1:
                    povezava['jd1'] = jd_new
                elif jd == jd2:
                    povezava['jd2'] = jd_new

# -------------------------------------------------------------------------|--

def multi_graph(vozlisca, povezave):
    '''
    Prečita vozlisca in povezave v nx.MultiGraph().
    
    Ena povezava je ali v fff ali pa v fff.exclude (izključno ali).
    Eno vozlišče je ali v fff ali pa v fff.exclude (izključno ali).
    '''
    vozliscad = {v['jd']: v for v in vozlisca}
    #
    fff = nx.MultiDiGraph()
    fff.exclude = nx.MultiDiGraph()
    #
    JDS = set()
    for v in vozlisca:
        jd = v['jd']
        if v['exclude'] == 0:
            fff.add_node(jd, **v)
            JDS.add(jd)
        else:
            v['level'] = -101                      # od prej zaukazano exclude
            fff.exclude.add_node(jd, **v)
    #
    for p in povezave:
        jd1 = p['jd1']
        jd2 = p['jd2']
        if p['exclude'] == 1:
            p['level'] = -101                      # od prej zaukazano exclude
            fff.exclude.add_edge(jd1, jd2, **p)    #
            fff.exclude.nodes[jd1].update(vozliscad[jd1])
            fff.exclude.nodes[jd2].update(vozliscad[jd2])
        elif not set((jd1, jd2)) <= JDS:
            p['level'] = -102
            p['exclude'] = 1
            fff.exclude.add_edge(jd1, jd2, **p)
            fff.exclude.nodes[jd1].update(vozliscad[jd1])
            fff.exclude.nodes[jd2].update(vozliscad[jd2])
        elif p['exclude'] == 0:
            fff.add_edge(jd1, jd2, **p)
    #
    return fff

# -------------------------------------------------------------------------|--

def expand(fff):
    '''
    Širitev po slojih od TP proti porabnikom.
    
    '''
    # izključene povezave naredimo nevidne
    #
    for jd, q in fff.nodes(data=True):
        q['level'] = -103                         # vozlišča še niso napajana
    #
    for jd1, jd2, q in fff.edges(data=True):
        q['zze'] = False
        q['level'] = -103                       # po povezavah še ne teče moč
    #
    hhh = nx.MultiDiGraph()
    #
    # (1) privzamemo vse TP-je kot singletone, level=0
    #
    level = 0
    for jd, q in fff.nodes(data=True):
        if q['tip'] == 'TP':
            q['cTP'] = jd
            q['level'] = level
            hhh.add_node(jd, **q)
    #
    # (2) širimo omrežje po povezavah
    #         nova povezava level=level
    #         novo vozlišče level=level+1
    #
    znano = list(hhh.nodes())
    while True:
        novo = set()
        for jd1, jd2, qE in fff.edges(data=True):
            if qE['zze']: continue
            if jd1 not in znano and jd2 not in znano: continue
            if jd1 in znano and jd2 in znano:
                qE['level'] = -104                            # povzroča cikel
                qE['zze'] = True
                continue
            if jd2 in znano and jd1 not in znano:
                jd1, jd2 = jd2, jd1
            if jd2 not in novo:
                #
                qE['level'] = level
                hhh.add_edge(jd1, jd2, **qE)
                qE['zze'] = True
                #
                qN = fff.nodes[jd2]
                qN['level'] = level + 1
                hhh.add_node(jd2, **qN)
                #
                novo.add(jd2)
        if novo:
            znano += list(novo)
            level += 1
        else:
            break
    #
    # odstranimo nedosežene (level=-103)
    #
    for jd, q in fff.copy().nodes(data=True):
        if q['level'] == -103:
            q['exclude'] = 1
            fff.exclude.add_node(jd, **q)
    #
    for jd1, jd2, q in fff.copy().edges(data=True):
        if q['level'] == -103:
            q['exclude'] = 1
            fff.exclude.add_edge(jd1, jd2, **q)
            fff.exclude.nodes[jd1].update(fff.nodes[jd1])
            fff.exclude.nodes[jd2].update(fff.nodes[jd2])
    #
    # odstranimo ciklične (level=-104) 
    #
    for jd1, jd2, q in fff.copy().edges(data=True):
        if q['level'] == -104:
            q['exclude'] = 1
            fff.exclude.add_edge(jd1, jd2, **q)
            fff.exclude.nodes[jd1].update(fff.nodes[jd1])
            fff.exclude.nodes[jd2].update(fff.nodes[jd2])
    #
    hh = []
    #
    if 0 < hhh.number_of_nodes():
        #
        # CHOPPING TO INDIVIDUAL LV-NETS
        # hhh = nx.DiGraph() ==> hh = [ h=nx.DiGraph() ]
        #
        ccs = nx.connected_components(
                nx.Graph(hhh))
        #
        for cc in ccs:
            _ = hhh.subgraph(cc)
            h = nx.MultiDiGraph(_)                            # un-freeze-ing
            hh.append(h)
        #
        # NAMEPLATES
        #
        for h in hh:
            h.sw_meritve = False
            h.timeseries = []
            h.cTP = 'non-presente'
            for jd, q in h.nodes(data=True):
                if q['tip'] == 'TP':
                    h.cTP = q['cTP']
                    h.dispod = q['dispod']
                    h.nnotp = q['nnotp']
                    h.S_SN = q['S_SN']
                    h.UTP = q['UTP']
                    h.name = h.dispod.upper() + ' ' + h.nnotp.upper()
                    break
        #
        # grafe, ki ne vsebujejo TP, izključimo iz seznama hh
        #
        #        in jih dodamo med excludirane v fff.exclude
        #
        for h in hh.copy():
            if h.cTP == 'non-presente':
                for jd1, jd2, q in h.edges(data=True):
                    q['level'] = -105
                    q['exclude'] = 1
                    fff.exclude.add_edge(jd1, jd2, **q)
                for jd, q in h.nodes(data=True):
                    q['level'] = -105
                    q['exclude'] = 1
                    fff.exclude.add_node(jd, **q)
                hh.remove(h)
    #
    fff.exclude.name = 'EXCLUDE GRAF'
    hh.append(fff.exclude)
    #
    return hh

# -------------------------------------------------------------------------|--

#
# ### NXNX_TO_QGIS
#

# -------------------------------------------------------------------------|--

def nxnx_to_qgis(hh, HH, lyrV, lyrP,
            sw_geom=1, model_dir=None, zbiralke_mm=[]):
    '''
    Zapiše hh = [ nx.DiGraph() ] v sloja lyrV in lyrP.
    
                              ! ==> lyrV
    hh = [ nx.DiGraph() ] ==> 
                              ! ==> lyrP
    '''
    # print('\nNXNX_TO_QGIS')
    #
    # (1) najprej brisanje vsega v QGIS-u
    #
    prV = lyrV.dataProvider()
    prP = lyrP.dataProvider()
    #
    lyrV.startEditing()
    lyrP.startEditing()
    #
    prV.deleteFeatures(
            [ftr.id() for ftr in lyrV.getFeatures()])
    prP.deleteFeatures(
            [ftr.id() for ftr in lyrP.getFeatures()])
    #
    lyrV.commitChanges(stopEditing=False)
    lyrP.commitChanges(stopEditing=False)
    #
    # (2) na novo risanje seznama hh ali seznama HH
    #
    apoint, alinee = izberi_nacin_risanja(sw_geom)
    #
    fldVs = lyrV.fields()
    fldVnms = [_.name() for _ in fldVs]
    fldPs = lyrP.fields()
    fldPnms = [_.name() for _ in fldPs]
    #
    ftrftrV, ftrftrP = [], []
    #
    mm = hh if sw_geom == 1 else HH
    #
    JDS = set()
    #
    for m in mm[:-1]:
        for jd, q in m.nodes(data=True):
            JDS.add(jd)
            ftr = QgsFeature(fldVs)
            for _ in fldVnms:
                try:
                    ftr.setAttribute(_, q[_])
                except KeyError:
                    continue
            x, y = q[apoint][0], q[apoint][1]
            q = QgsPointXY(x, y)
            geom = QgsGeometry.fromPointXY(q)
            ftr.setGeometry(geom)
            ftrftrV.append(ftr)
        for jd1, jd2, q in m.edges(data=True):
            ftr = QgsFeature(fldPs)
            for _ in fldPnms:
                try:
                    ftr.setAttribute(_, q[_])
                except KeyError:
                    continue
            lineeXY = []
            for point in q[alinee]:
                pointXY = QgsPointXY(point[0], point[1])
                lineeXY.append(pointXY)
            geom = QgsGeometry.fromPolylineXY(lineeXY)
            ftr.setGeometry(geom)
            ftrftrP.append(ftr)
    #
    m = mm[-1]
    for jd, q in m.nodes(data=True):
        if jd not in JDS:
            ftr = QgsFeature(fldVs)
            for _ in fldVnms:
                try:
                    ftr.setAttribute(_, q[_])
                except KeyError:
                    continue
            x, y = q[apoint][0], q[apoint][1]
            q = QgsPointXY(x, y)
            geom = QgsGeometry.fromPointXY(q)
            ftr.setGeometry(geom)
            ftrftrV.append(ftr)
    for jd1, jd2, q in m.edges(data=True):
        ftr = QgsFeature(fldPs)
        for _ in fldPnms:
            try:
                ftr.setAttribute(_, q[_])
            except KeyError:
                continue
        lineeXY = []
        for point in q[alinee]:
            pointXY = QgsPointXY(point[0], point[1])
            lineeXY.append(pointXY)
        geom = QgsGeometry.fromPolylineXY(lineeXY)
        ftr.setGeometry(geom)
        ftrftrP.append(ftr)
    if sw_geom in (3, 4):
        if   sw_geom == 3: polje = 'zbir2avec'
        elif sw_geom == 4: polje = 'zbir3avec'
        for zbiralke in zbiralke_mm:
            for zb in zbiralke[polje]:
                ftr = QgsFeature(fldPs)
                ftr.setAttribute('sw_zbiralka', 1)
                x0, y0 = zb[0]
                x1, y1 = zb[1]
                lineeXY = [QgsPointXY(x0, y0), QgsPointXY(x1, y1)]
                geom = QgsGeometry.fromPolylineXY(lineeXY)
                ftr.setGeometry(geom)
                ftrftrP.append(ftr)
    #
    write_to_disk(ftrftrV, prV, lyrV, model_dir=model_dir)
    write_to_disk(ftrftrP, prP, lyrP, model_dir=model_dir)
    #
    lyrV.commitChanges(stopEditing=False)
    lyrP.commitChanges(stopEditing=False)
    #
    znova_postavi_selected(hh[:-1], lyrV, lyrP)
    #
    lyrV.commitChanges(stopEditing=False)
    lyrP.commitChanges(stopEditing=False)

def izberi_nacin_risanja(sw_geom):
    if sw_geom == 1:
        point, linee = 'point', 'linee'
    elif sw_geom == 2:
        point, linee = 'point', 'line'
    elif sw_geom == 3:
        point, linee = 'espoint', 'eslinee'
    elif sw_geom == 4:
        point, linee = 'esrpoint', 'esrlinee'
    elif sw_geom == 5:
        point, linee = 'metlapoint', 'metlalinee'
    elif sw_geom == 6:
        point, linee = 'resismetlapoint', 'resismetlalinee'
    else:
        point, linee = 'point', 'linee'
    return point, linee

def write_to_disk(ftrftr, pr, lyr, model_dir=None):
    #
    pr.addFeatures(ftrftr)
    lyr_to_list(lyr, model_dir)

def znova_postavi_selected(hh, lyrV, lyrP):
    #
    selectedVjds = set()
    selectedPjdjds = set()
    for h in hh:
        for jd, q in h.nodes(data=True):
            if q['is_selected']:
                selectedVjds.add(jd)
        for jd1, jd2, q in h.edges(data=True):
            if q['is_selected']:
                selectedPjdjds.add((jd1, jd2))
                selectedPjdjds.add((jd2, jd1))
    #
    selectedVids = []
    selectedPids = []
    for ftr in lyrV.getFeatures():
        fid = ftr.id()
        jd = ftr['jd']
        if jd in selectedVjds:
            selectedVids.append(fid)
    for ftr in lyrP.getFeatures():
        fid = ftr.id()
        jd1 = ftr['jd1']
        jd2 = ftr['jd2']
        if (jd1, jd2) in selectedPjdjds:
            selectedPids.append(fid)
    #
    lyrV.selectByIds(selectedVids)
    lyrP.selectByIds(selectedPids)




# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# samo zaradi [SP] simulate panda vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

# def nx_to_qgis(h, lyrV, lyrP, sw_geom,
            # sw_commit=True,
            # modmodV={}, geomgeomV={}, ftrftrV=[],
                    # fldnameV_i={}, fldVs=QgsFields, fldVnms=[],
            # modmodP={}, geomgeomP={}, ftrftrP=[],
                    # fldnameP_i={}, fldPs=QgsFields, fldPnms=[]):
    # '''
    # Zapiše h=nx.DiGraph() v sloja lyrV in lyrP.
    
                       # / ==> lyrV
    # h=nx.DiGraph() ==> 
                       # \ ==> lyrP
    # '''
    # if sw_commit:
        # swgeom = sw_geom[1]
        # fldnameV_i = get_fields_numbering(lyrV)
        # fldVs = lyrV.fields()
        # fldVnms = [_.name() for _ in fldVs]
        # fldnameP_i = get_fields_numbering(lyrP)
        # fldPs = lyrP.fields()
        # fldPnms = [_.name() for _ in fldPs]
    # else:
        # swgeom = sw_geom
    # apoint, alinee = izberi_nacin_risanja(swgeom)
    # #
    # for jd in h.nodes():
        # try:
            # fid = h.nodes[jd]['fid']
            # mod = {}
            # for fldname, i in fldnameV_i.items():
                # try:
                    # mod[i] = h.nodes[jd][fldname]
                # except KeyError:
                    # continue
            # modmodV[fid] = mod
            # x = h.nodes[jd][apoint][0]
            # y = h.nodes[jd][apoint][1]
            # q = QgsPointXY(x, y)
            # geom = QgsGeometry.fromPointXY(q)
            # geomgeomV[fid] = geom
        # except KeyError:
            # ftr = QgsFeature(fldVs)
            # for _ in fldVnms:
                # try:
                    # ftr.setAttribute(_, h.nodes[jd][_])
                # except:
                    # continue
            # x, y = h.nodes[jd][apoint][0], h.nodes[jd][apoint][1]
            # q = QgsPointXY(x, y)
            # geom = QgsGeometry.fromPointXY(q)
            # ftr.setGeometry(geom)
            # ftrftrV.append(ftr)
    # #
    # for jd1, jd2 in h.edges():
        # try:
            # fid = h.edges[jd1, jd2]['fid']
            # mod = {}
            # for fldname, i in fldnameP_i.items():
                # try:
                    # mod[i] = h.edges[jd1, jd2][fldname]
                # except KeyError:
                    # continue
            # modmodP[fid] = mod
            # lineeXY = []
            # for point in h.edges[jd1, jd2][alinee]:
                # pointXY = QgsPointXY(point[0], point[1])
                # lineeXY.append(pointXY)
            # geom = QgsGeometry.fromPolylineXY(lineeXY)
            # geomgeomP[fid] = geom
        # except KeyError:
            # ftr = QgsFeature(fldPs)
            # for _ in fldPnms:
                # try:
                    # ftr.setAttribute(_, h.edges[jd1, jd2][_])
                # except:
                    # continue
            # lineeXY = []
            # for point in h.edges[jd1, jd2][alinee]:
                # pointXY = QgsPointXY(point[0], point[1])
                # lineeXY.append(pointXY)
            # geom = QgsGeometry.fromPolylineXY(lineeXY)
            # ftr.setGeometry(geom)
            # ftrftrP.append(ftr)
    # #
    # if sw_commit:
        # modify_add(modmodV, geomgeomV, ftrftrV, lyrV)
        # modify_add(modmodP, geomgeomP, ftrftrP, lyrP)
        # sw_geom[0] = swgeom
        # sw_geom[1] = 1

# def get_fields_numbering(lyr):
    # fldname_i = {}
    # flds = lyr.fields()
    # for fld in flds:
        # fldname = fld.name()
        # i = flds.indexOf(fldname)
        # fldname_i[fldname] = i
    # return fldname_i

# def modify_add(modmod, geomgeom, ftrftr, lyr):
    # pr = lyr.dataProvider()
    # pr.changeAttributeValues(modmod)
    # pr.changeGeometryValues(geomgeom)
    # pr.addFeatures(ftrftr)
    # lyr.commitChanges(stopEditing=False)
    # lyr.triggerRepaint()

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# samo zaradi [SP] simulate panda ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




#
# ### TRANSFORMATOR: IZGUBE V BAKRU
#

def izgube_v_bakru(Sn):
    '''
    Določi primerni komercialni transfomator za navjdezno moč Sn.
    
    '''
    X = (0,  50,  100,  160,   250,   315,   400,  500,  630,
            800, 1000, 1250,  1600,  2000,  2500)                       # kVA
    Y = (0, 750, 1250, 1700,  2350,  2800,  3250, 3900, 4600,
           6000, 7600, 9500, 12000, 15000, 18500)                         # W
    if Sn > X[-1]:                   # Pcu je klasa A zelo učinkovitih transf.
        St, Pcu = Sn, 397.6 + 7.2 * Sn         # linearna aproksimacija po MNK
    else:
        for (i, x) in enumerate(X):
            if Sn < x:
                St, Pcu = x, Y[i]
                break
    uk = 4. if St < 700 else 6.
    Pcu *= 1.4                       # klasa C starih manj učinkovitih transf.
    vezava = 'Yz' if St < 200 else 'Dy'
    return 1000 * St, Pcu, uk, vezava

#
# ### READING SHP FILES
#

# def shp_point(podr, vfile, vjd, shp='.shp'):
    # '''
    # Prečita SHP datoteko tipa point.
    
    # podr   'c:/kn3/data/egorenjska'  lokacija na disku
    # vfile  'nodes'                   'nodes.shp' datoteka
    # vjd    {'jd1', 'jd2'}            množica! obveznih polj
    # '''
    # vozlisca = []
    # #
    # pth = os.path.join(podr, vfile + shp)
    # if not os.path.exists(pth):
        # print('shp_point', podr, vfile.upper() + shp.upper() + ' ne obstaja')
        # return vozlisca
    # #
    # lyr = QgsVectorLayer(pth, providerLib='ogr')
    # if not lyr.isValid():
        # print('shp_point', podr, vfile.upper() + shp.upper() + ' ni veljavna')
        # return vozlisca
    # #
    # # fields = [_ for _ in lyr.fields()]
    # fieldnames = [_.name().lower() for _ in lyr.fields()]
    # for ftr in lyr.getFeatures():
        # v = {}
        # # for fieldname, field in zip(fieldnames, fields):
        # for fieldname in fieldnames:
            # _ = ftr[fieldname]
            # if isinstance(_, QVariant): continue
            # # if field.type() == QVariant.Int:
            # v[fieldname] = _
        # _ = ftr.geometry().asPoint()
        # v['point'] = (round(_.x(), 4), round(_.y(), 4))
        # vozlisca.append(v)
    # #
    # vozlisca = [v for v in vozlisca if vjd < v.keys()]
    # #
    # return vozlisca

# # -------------------------------------------------------------------------|--

# def shp_line(podr, pfile, pjd1, pjd2):
    # '''
    # Prečita SHP datoteko tipa line.
    
    # podr          'c:/kn3/data/egorenjska'  lokacija na disku
    # pfile         'branches'                'branches.shp'
    # pjd1, pjd2    'jd1, jd2'                obvezni polji, enolična šifra
    # '''
    # #
    # povezave = []
    # #
    # pth = os.path.join(podr, pfile + '.shp')
    # if not os.path.exists(pth):
        # print('shp_line', podr, pfile.upper() + '.SHP ne obstaja')
        # return povezave
    # #
    # lyr = QgsVectorLayer(pth, providerLib='ogr')
    # if not lyr.isValid():
        # print('shp_line', podr, pfile.upper() + '.SHP ni veljavna')
        # return povezave
    # #
    # fields = [_.name().lower() for _ in lyr.fields()]
    # for ftr in lyr.getFeatures():
        # p = {}
        # for field in fields:
            # _ = ftr[field]
            # if isinstance(_, QVariant): continue
            # p[field] = _
        # geom = ftr.geometry()
        # __ = list(geom.vertices())
        # p['linee'] = [(round(_.x(), 4), round(_.y(), 4)) for _ in __]
        # p['lineelen'] = geom.length()
        # povezave.append(p)
    # #
    # povezave = [p for p in povezave if pjd1 in p and pjd2 in p]
    # #
    # return povezave

# # -------------------------------------------------------------------------|--

def csv_to_list(podr, delim=';', model_dir=None):
    '''
    Prečita CSV datoteko v seznam.
    
    podr  'c:/kn3/data/egorenjska/branches.csv'  lokacija na disku
    '''
    if not os.path.exists(podr):
        print('csv_to_list', podr, 'datoteka ne obstaja')
        return []
    #
    _ = 'file:///{}?delimiter={}&crs=epsg:{}&wktField={}'
    uri = _.format(podr, delim, 3794, 'shape')
    #
    head, tail = os.path.split(podr)
    name, extension = os.path.splitext(tail)
    lyr = QgsVectorLayer(uri, name, 'delimitedtext')
    if not lyr.isValid():
        print('csv_to_list', podr, 'datoteka ni veljavna')
        return []
    #
    return lyr_to_list(lyr, model_dir)

# -------------------------------------------------------------------------|--

def shp_to_list(podr, model_dir=None):
    '''
    Prečita SHP datoteko v seznam.
    
    podr  'c:/kn3/data/egorenjska/branches.shp'  lokacija na disku
    '''
    if not os.path.exists(podr):
        print('shp_to_list', podr, 'datoteka ne obstaja')
        return []
    #
    head, tail = os.path.split(podr)
    name, extension = os.path.splitext(tail)
    lyr = QgsVectorLayer(podr, name, providerLib='ogr')
    if not lyr.isValid():
        print('shp_to_list', podr, 'datoteka ni veljavna')
        return []
    #
    return lyr_to_list(lyr, model_dir)

# -------------------------------------------------------------------------|--

def qgis_to_list(lyr, model_dir=None):
    return lyr_to_list(lyr, model_dir)

def lyr_to_list(lyr, model_dir=None):
    '''
    Prečita (obstoječi veljavni) lyr v seznam [ {fieldname: value} ].
    
    '''
    seznam = []
    QPI = QgsProject.instance()
    #
    _ = lyr.geometryType()
    
    # print()
    # print('begin lyr_to_list')
    # print(type(_))
    # print(_)
    # print(QgsWkbTypes.geometryDisplayString(_))
    # print('end lyr_to_list')
    # print()
    
    geom_str = QgsWkbTypes.geometryDisplayString(_)
    fieldnames = [_.name() for _ in lyr.fields()]
    selected_ids = set()
    if QPI:
        __ = QPI.mapLayersByName(
                lyr.sourceName())
        if __:
            _ = __[0]
            selected_ids = set(_.selectedFeatureIds())
    # if selected_ids:
        # print('LYR_TO_LIST', lyr.sourceName(), selected_ids)
    #
    for ftr in lyr.getFeatures():
        if 'sw_zbiralka' in fieldnames:
            if ftr['sw_zbiralka'] == 1:
                continue
        fid = ftr.id()
        s = {}
        s['fid'] = fid
        s['is_selected'] = True if fid in selected_ids else False
        #
        for fieldname in fieldnames:
            _ = ftr[fieldname]
            if isinstance(_, QVariant):               # to avoid the NULL fields
                continue
            elif isinstance(_, QDate):        # to enable the JSON saving format
                s[fieldname] = str(_)
            else:
                s[fieldname] = _
        #
        s['geom_str'] = geom_str
        if geom_str == 'No geometry':
            pass
        elif geom_str == 'Point':
            _ = ftr.geometry().asPoint()
            s['point'] = (round(_.x(), 2), round(_.y(), 2))
        elif geom_str == 'Line':
            geom = ftr.geometry()
            __ = list(geom.vertices())
            s['linee'] = [(round(_.x(), 2), round(_.y(), 2)) for _ in __]
            s['lineelen'] = geom.length()
        else:
            pass
        #
        seznam.append(s)
    #
    # asjson = json.dumps(seznam, indent=4)
    # name = lyr.sourceName()
    # name2 = f'{name}.json'
    # pth = os.path.join(model_dir, name2) if model_dir else name2
    # with open(pth, 'w') as g:
        # g.write(asjson)
    #
    if model_dir:
        asjson = json.dumps(seznam, indent=4)
        with open(os.path.join(
                    model_dir, f'{lyr.sourceName()}.json'), 'w') as g:
            g.write(asjson)
    #
    return seznam

# -------------------------------------------------------------------------|--

#
# ### READING CSV MERITVE
#

def csv_mer(podr, model_dir=None):
    '''
    Čitanje CSV datotek z merilnimi podatki.
    
    '''
    mer = []
    nap = []
    #
    TS = '%Y-%m-%dT%H:%M:%SZ'
    #
    pth = os.path.join(podr, 'obremenitve.csv')
    if os.path.exists(pth):
        with open(pth, 'r', newline='', encoding='utf-8',
                errors='ignore') as f:
            reader = csv.reader(f, delimiter=';')
            next(reader)
            for row in reader:
                try:
                    timestamp = datetime.datetime.strptime(row[1], TS)
                except ValueError:
                    continue
                m = {'NODE_ID': int(row[0]),
                     'Timestamp': str(timestamp),
                     'Pb_sum': float(row[2].replace(',', '.')),
                     'Pg_sum': float(row[3].replace(',', '.')),
                     'P_sum': float(row[4].replace(',', '.'))}
                mer.append(m)
        asjson = json.dumps(mer, indent=4)
        name = 'obremenitve.json'
        pth = os.path.join(model_dir, name) if model_dir else name
        with open(pth, 'w') as g:
            g.write(asjson)
    #
    pth = os.path.join(podr, 'napetosti.csv')
    if os.path.exists(pth):
        with open(pth, 'r', newline='', encoding='utf-8',
                    errors='ignore') as f:
            reader = csv.reader(f, delimiter=';')
            next(reader)
            for row in reader:
                timestamp = datetime.datetime.strptime(row[1], TS)
                n = {'NODE_ID': int(row[0]),
                     'Timestamp': str(timestamp),
                     'U': float(row[2].replace(',', '.'))}
                nap.append(n)
        asjson = json.dumps(nap, indent=4)
        name = 'napetosti.json'
        pth = os.path.join(model_dir, name) if model_dir else name
        with open(pth, 'w') as g:
            g.write(asjson)
    #
    return mer, nap

#
# ### APROKSIMATIVNE FUNKCIJE ZA MAKSIMALNI TOK IN SPECIFIČNO UPORNOST
#

def set_internal_tp_branch(h, jd1, jd2, St=-1):
    S, d, mat = 2400., 0., 'Cu'
    rspec = rspec_func(S, mat)
    resis = d * rspec / 1000.
    cspec = cspec_func(S, mat)
    conduc = conduc_func(resis)
    Imax = imax_func(2, S, mat, St=St)
    h.edges[jd1, jd2]['presek'] = S
    h.edges[jd1, jd2]['dolz'] = d
    h.edges[jd1, jd2]['mat'] = mat
    h.edges[jd1, jd2]['rspec'] = rspec
    h.edges[jd1, jd2]['resis'] = resis
    h.edges[jd1, jd2]['cspec'] = cspec
    h.edges[jd1, jd2]['conduc'] = conduc
    # h.edges[jd1, jd2]['Imax'] = round(Imax / 1000, 1)
    h.edges[jd1, jd2]['Imax'] = Imax / 1000

# -------------------------------------------------------------------------|--

def evaluiraj_izvod_navzdol(h, jd1):
    '''
    Skupno gospodinjstev in velikega odjema navzdol po omrežju. 
    
    '''
    ngoi1 = h.nodes[jd1]['nGOI_0']
    pvel1 = h.nodes[jd1]['Pvel_0']
    for jd2 in list(h.successors(jd1)):
        # if h.edges[jd1, jd2]['exclude']:                                 # !!!
            # continue
        ngoi2, pvel2 = evaluiraj_izvod_navzdol(h, jd2)
        ngoi1 += ngoi2
        pvel1 += pvel2
    return ngoi1, pvel1

# -------------------------------------------------------------------------|--

def binomial(spe, nGOI, kWfix):
    GOIkW = spe['GOIkW']
    FiGOV = spe['FiGOV']                # == 80 % od seštevka konstantnih kW
    FpOOV = spe['FpOOV']                # == 80 % od seštevka konstantnih kW
    F_GOV_OOV = (FiGOV + FpOOV) / 2
    nGOI_Fp = faktor_prekrivanja(spe, nGOI)
    gospodinjstva = nGOI_Fp * GOIkW
    veliko_odjem = F_GOV_OOV * kWfix
    skupno = gospodinjstva + veliko_odjem
    return skupno

# -------------------------------------------------------------------------|--

def faktor_prekrivanja(spe, i):
    '''
    Funkcija za izračun faktorja prekrivanja za primer i gospodinjstev.

    Input:
        spe['Fpnesk']               == 0.2222 konstanta faktorja prekrivanja
    '''
    Fpnesk = spe['Fpnesk']
    if i <= 0:
        return 0
    elif i <= 100:
        return i * (Fpnesk + (1 - Fpnesk) / math.sqrt(i))
    else:
        return i * 0.3

# -------------------------------------------------------------------------|--

def rspec_func(S, mat='Al'):
    '''
    Specifična upornost kabla (Ohm/km).
    
    '''
    if S > 0.001:
        rspec = 35.0 / S
        if mat == 'Cu':
            rspec *= 0.60
    else: 
        rspec = 0.0
    #
    # return round(rspec, 3)
    return rspec

# -------------------------------------------------------------------------|--

def cspec_func(S, mat='Al'):
    '''
    Specifična prevodnost kabla (Siemens/km).
    
    '''
    rspec = rspec_func(S, mat)
    #
    if S > 0.001:
        cspec = 1. / rspec
    else:
        cspec = 999999.9
    #
    return cspec

# -------------------------------------------------------------------------|--

def conduc_func(resis):
    '''
    Konduktivnost G kot inverz rezistence R (Siemens).
    
    '''
    if resis < 0.0001:
        conduc = 999999.9
    else:
        conduc = 1. / resis
    #
    return conduc

# -------------------------------------------------------------------------|--

def imax_func(i, S, mat='Al', St=-1):
    '''
    Maksimalni tok, korenska in linearna aproksimacija (A).
    
    '''
    if St > 0:                                    # Transformator
        imax = St / (0.4 * math.sqrt(3))
    elif S > 0.001:
        if   i == 1:                              # Mejni tok za načrt.omr.
            imax =  10.4 * math.sqrt(S) + 0.16 * S
        elif i == 2:                              # Termični, f.polag. 0,75
            imax =  14.2 * math.sqrt(S) + 0.22 * S
        elif i == 3:                              # Podatki proizvajalcev
            imax =  19.0 * math.sqrt(S) + 0.30 * S
        if mat == 'Cu': imax *= 1.29
    else:
        imax = 9999999.9
    #
    # return round(imax, 1)
    return imax

# -------------------------------------------------------------------------|--

def imax_func_korenska(i, S):
    '''
    Maksimalni tok, modificirana korenska aproksimacija (A).
    
    '''
    if   i == 0 or S < 0.001:            # Neskončni tok
        return 9999999.9
    elif i == 1:                         # Mejni tok za načrtovanje omrežja
        return  8. * S ** (1. / 1.70) 
    elif i == 2:                         # Termični tok s f. polaganja 0,75
        return 12. * S ** (1. / 1.75) 
    elif i == 3:                         # Termični tok po podatkih proizv.
        return 18. * S ** (1. / 1.83) 
    else:
        print('imax_func, neznani i =', i)

# -------------------------------------------------------------------------|--

def to_jd(point):
    '''
    Preračuna poljubno lokacijo 'point' v vozliščni jd = jd.
    
    point:  (500123.459, 100567.899)
    return: '500k123m46c100k567m90c'
    '''
    FMT = '{:03d}k{:03d}m{:02d}c{:03d}k{:03d}m{:02d}c'
    #
    x = round(point[0], 2)
    y = round(point[1], 2)
    #
    ix1 = int(x / 1000)
    ix2 = int(x - 1000 * ix1)
    ix3 = int(round(100 * (x - 1000 * ix1 - ix2)))
    #
    iy1 = int(y / 1000)
    iy2 = int(y - 1000 * iy1)
    iy3 = int(round(100 * (y - 1000 * iy1 - iy2)))
    #
    st = FMT.format(ix1, ix2, ix3, iy1, iy2, iy3)
    #
    return st

def to_point(jd):
    '''
    Preračuna vozliščno šifro jd v lokacijo.
    
    jd:     '500k123m46c100k567m90c'
    return: (500123.46, 100567.90)
    '''
    ix1 = int(jd[:3])
    ix2 = int(jd[4:7])
    ix3 = int(jd[8:10])
    #
    iy1 = int(jd[11:14])
    iy2 = int(jd[15:18])
    iy3 = int(jd[19:21])
    #
    x = 1000. * ix1 + ix2 + ix3 / 100.
    y = 1000. * iy1 + iy2 + iy3 / 100.
    #
    point = (x, y)
    #
    return point

# -------------------------------------------------------------------------|--

def razdalja2(point1, point2):
    '''
    Razdalja dveh točk računana s pomočjo QgsDistanceArea.
    
    point1 = (1, 1)
    point2 = (3, 2)
    
    dolz = sqrt(5)
    '''
    if not isinstance(point1, QgsPointXY):
        pointXY1 = QgsPointXY(point1[0], point1[1])
    #
    if not isinstance(point2, QgsPointXY):
        pointXY2 = QgsPointXY(point2[0], point2[1])
    #
    # # # # # pointXY1 = QgsPointXY(point1[0], point1[1])
    # # # # # pointXY2 = QgsPointXY(point1[0], point1[1])
    #
    lineXY = [pointXY1, pointXY2]
    #
    dolz = QgsDistanceArea().measureLine(lineXY)
    #
    return dolz

# -------------------------------------------------------------------------|--

def razdalja(point1, point2):
    
    return razdalja2(point1, point2)

def dolzina_poligonske_crte(linee):
    '''
    Dolzina seznama točk.
    
    linee = [(1, 1), (3, 2), (4, 3)]
    
    dolztop = sqrt(5) + sqrt(2)
    '''
    lineeXY = []
    for point in linee:
        pointXY = QgsPointXY(point[0], point[1])
        lineeXY.append(pointXY)
    dolztop = QgsDistanceArea().measureLine(lineeXY)
    #
    return dolztop

# -----------------------------------------------------------------------|--

#
# ### SIMULACIJA SIM
#

# -0---------------------------------------------------------------------|--

def kriteriji(hh, spe, sw_iter=False, model_dir=None,
        vozliscadef=None, povezavedef=None):
    '''
    Simulacija NN omrežja v skladu s Kriteriji EIMV #2400.
    
    '''
    resetiraj_exclude(hh[-1], vozliscadef, povezavedef)
    #
    # jedro, izračun, simulacije modela KN3
    #
    v230 = 1000 * 0.4 / math.sqrt(3)
    #
    zbiralke = []
    #
    HH = []
    #
    for i, h in enumerate(hh[:-1]):
        #
        H = many_to_one(h)
        #
        print('{0:3d} sim kriteriji {1} {2}'.format(
                i+1, H.dispod, H.nnotp, flush=True))
        #
        prim = H.cTP
        sek_ = list(H.successors(prim))
        #
        if sek_:
            sek = sek_[0]
            if abs(H.nodes[sek]['UTP']) > 0.001:
                v230 = H.nodes[sek]['UTP']
            #
            SIMmodule_SIM(H, v230, spe, sw_iter)
        #
        izpolni_preostala_polja(H)
        #
        _ = enopolna_shema(H)
        zbiralke.append(_)
        #
        varovalke(H, model_dir)
        #
        one_to_many(H, h)
        #
        HH.append(H)
    #
    # HH.append(hh[-1])
    #
    pth = os.path.join(model_dir, 'GOIkW.json')
    with open(pth, 'w') as g:
        g.write(json.dumps(spe['GOIkW'], indent=4))
    #
    return zbiralke, HH

# -----------------------------------------------------------------------|--
# -1---------------------------------------------------------------------|--

def resetiraj_exclude(fffexclude, vozliscadef, povezavedef):
    #
    ESENCIALNI = set(('jd', 'tip', 'nGOI_0', 'Pvel_0', 'Pele_0', 'dispod',
            'label', 'exclude', 'opomba'))
    for jd, q in fffexclude.nodes(data=True):
        for k, v in vozliscadef.items():
            if k in ESENCIALNI:
                continue
            vv = v[2]
            q[k] = vv                                          # resetiranje
    #
    ESENCIALNI = set(('jd1', 'jd2', 'dolz', 'dolztop', 'mat', 'presek',
            'dispod', 'label', 'exclude', 'trafo', 'opomba', 'original'))
    for jd1, jd2, q in fffexclude.edges(data=True):
        for k, v in povezavedef.items():
            if k in ESENCIALNI:
                continue
            vv = v[2]
            q[k] = vv                                          # resetiranje

# -----------------------------------------------------------------------|--

def many_to_one(h):
    #
    H = nx.DiGraph()
    #
    H.cTP = h.cTP
    H.name = h.name
    H.dispod = h.dispod
    H.nnotp = h.nnotp
    H.S_SN = h.S_SN
    H.UTP = h.UTP
    #
    # vsa vozlišča skupaj z vsemi atributi
    #
    H.add_nodes_from(h.nodes(data=True))
    #
    # pri vzporednih povezavah
    #     celotna taprva (vsi atributi)
    #     nato prištevamo S in dolz
    #
    for jd1, jd2, q in h.edges(data=True):
        #
        if (jd1, jd2) not in H.edges():
            H.add_edge(jd1, jd2, **q)
        else:
            S = q['presek']
            dolz = q['dolz']
            H.edges[jd1, jd2]['presek'] += S
            H.edges[jd1, jd2]['dolz'] += dolz
    #
    # povprečenje dolžine
    #
    for jd1, jd2 in set(h.edges()):
        n = h.number_of_edges(jd1, jd2)
        H.edges[jd1, jd2]['dolz'] /= n
    #
    # poračun glede na novi spremenljivki S in dolz
    #
    for jd1, jd2, q in H.edges(data=True):
        #
        level = q['level']
        S = q['presek']
        mat = q['mat']
        dolz = q['dolz']
        rspec = rspec_func(S, mat)
        cspec = cspec_func(S, mat)
        resis = dolz * rspec / 1000.
        conduc = conduc_func(resis)
        if level == 0:
            trafo = q['trafo']
            ST = float(trafo.split(',')[0].split()[1])
            imax = imax_func(2, S, mat, St=ST)
        else:
            imax = imax_func(2, S, mat)
        q['rspec'] = rspec
        q['resis'] = resis
        q['cspec'] = cspec
        q['conduc'] = conduc
        q['Imax'] = imax
    #
    return H

# -----------------------------------------------------------------------|--

def SIMmodule_SIM(H, uTP, spe, sw_iter):
    '''
    Simulacija NN omrežja v skladu s Kriteriji načrtovanja #2400.
    
    '''
    def letna_energija(n, Pv, Pd): 
        '''
        Letna energija iz n=nGOI, Pv=Pvel in Pd=Pdod.
        
        '''
        return GOIkW * n * GOIoh + F_GOV_OOV * Pv * VELoh + Pd * DODoh
    #
    if spe['sw_tocr']:
        for c, q in H.nodes(data=True):
            samooskrba = q['nGOI_0'] > 0 and q['Pele_0'] > 0.
            q['Pdod_0'] = spe['tocr'] * q['Pele_0'] if samooskrba else 0.
    else:
        for c, q in H.nodes(data=True):
            q['Pdod_0'] = 0.
    #
    cTP = initialize_fields(H, uTP)
    #
    propagate_binomial(H, cTP)
    #
    evaluate_binomial(spe, H, cTP)
    #
    for i in range(10):                # maksimalno 10 iteracij
        #
        delta = pretoki_moci(H, uTP)
        #
        if sw_iter:
            print('%3d max delta U = %7.3f V' % (i + 1, delta))
            if delta < 0.1:
                break
        else:
            break
    #
    H.nodes[cTP]['dP'] = NNizgube(H, cTP)
    #
    GOIoh = 1000.                          # GOI na polno moč v urah na leto
    VELoh = 8760 / 3                       # VEL na polno moč 8 ur na dan
    DODoh = 1000.                          # DOD == FV == 1000 ur na leto
    #
    GOIkW = spe['GOIkW']
    FiGOV = spe['FiGOV']                    # 80% od seštevka konstantnih kW
    FpOOV = spe['FpOOV']
    F_GOV_OOV = (FiGOV + FpOOV) / 2
    #
    for c, q in H.nodes(data=True):
        #
        nGOI_0, nGOI = q['nGOI_0'], q['nGOI']
        Pvel_0, Pvel = q['Pvel_0'], q['Pvel']
        Pdod_0, Pdod = q['Pdod_0'], q['Pdod']
        dP_0, dP, P = q['dP_0'], q['dP'], q['P']
        #
        W_0 = letna_energija(nGOI_0, Pvel_0, Pdod_0)
        W = letna_energija(nGOI, Pvel, Pdod)
        try:
            T0 = int(W / P)
        except ZeroDivisionError:
            T0 = 0
        Tizg = letne_izgubne_ure(T0)
        dW = dP * Tizg
        dW_0 = dP_0 * Tizg
        try:
            dWrel = 100 * dW / W 
        except ZeroDivisionError:
            dWrel  = 0.
        #
        q['W_0_kWh'], q['W_kWh'] = W_0, W
        q['T0_h'], q['Tizg_h'] = T0, Tizg
        q['dW_0_kWh'], q['dW_kWh'] = dW_0, dW
        q['dW_proc'] = dWrel
    #
    for c, d, q in H.edges(data=True):
        P = q['P']
        nGOI = q['nGOI']
        Pvel = q['Pvel']
        Pdod = q['Pdod']
        W = letna_energija(nGOI, Pvel, Pdod)
        try:
            T0 = int(W / P)
        except ZeroDivisionError:
            T0 = 0

        q['T0_h'] = T0
        Tizg = letne_izgubne_ure(T0)
        q['Tizg_h'] = Tizg
        dP = q['dP']
        q['dW_kWh'] = dP * Tizg
        dP_0 = q['dP_0']
        q['dW_0_kWh'] = dP_0 * Tizg
        dW = q['dW_kWh']
        q['W_kWh'] = W
        try:
            q['dW_proc'] = 100 * dW / W
        except ZeroDivisionError:
            q['dW_proc'] = 0.
    #
    metla(H)

# -----------------------------------------------------------------------|--

def izpolni_preostala_polja(h): 
    for jd, q in h.nodes(data=True):
        q['cTP'] = h.cTP
        q['dispod'] = h.dispod
        q['nnotp'] = h.nnotp
        q['S_SN'] = h.S_SN
        q['UTP'] = h.UTP
    for jd1, jd2, q in h.edges(data=True):
        q['cTP'] = h.cTP
        q['dispod'] = h.dispod
        q['nnotp'] = h.nnotp
        q['dolztop'] = q['lineelen']
        q['rspec'] = rspec_func(q['presek'], q['mat'])
        q['resis'] = q['dolz'] * q['rspec'] / 1000.
        q['cspec'] = cspec_func(q['presek'], q['mat'])
        q['conduc'] = conduc_func(q['resis'])
    distance_resistance_conductance_TP(h)
    izraccunaj_izvode(h)

# -----------------------------------------------------------------------|--

def one_to_many(H, h):
    '''
    Rezultate iz H=nx.DiGraph() distribuiramo na h=nx.MultiDiGraph().
    
    '''
    # vozlišča v celoti prepišemo, razen tačudnih geometrij
    #
    GEOM_POINT = ('espoint', 'esrpoint', 'metlapoint', 'resismetlapoint')
    #
    for jd, q in H.nodes(data=True):
        for k, v in q.items():
            if k in GEOM_POINT:
                continue
            h.nodes[jd][k] = v
    #
    # povezave
    #
    GEOM_LINE = ('eslinee', 'esrlinee', 'metlalinee', 'resismetlalinee')
    #
    for jd1, jd2 in set(h.edges()):
        Q = H.edges[jd1, jd2]
        n = h.number_of_edges(jd1, jd2)
        q = h.edges[jd1, jd2, 0]
        for K, V in Q.items():
            if K not in GEOM_LINE:
                q[K] = V
    #
    DISTRIBUIRAJ = ('nGOI', 'Pvel', 'Pdod', 'Pele', 'P', 'dP', 'dP_0',
            'W_kWh', 'dW_kWh', 'dW_0_kWh', 'Ib', 'Iele')
    #
    for jd1, jd2 in set(h.edges()):
        n = h.number_of_edges(jd1, jd2)
        if n > 1:
            Q = H.edges[jd1, jd2]
            R = Q['conduc']
            for i in range(n):
                q = h.edges[jd1, jd2, i]
                rriR = q['conduc'] / R
                for polje in DISTRIBUIRAJ:
                    _ = rriR * Q[polje]
                    if 'polje' == 'nGOI':
                        _ = int(round(_))
                    q[polje] = _

# -----------------------------------------------------------------------|--
# -2---------------------------------------------------------------------|--

def initialize_fields(H, uTP):
    #
    for c in H.nodes():
        H.nodes[c]['U'] = uTP
        H.nodes[c]['dU'] = 0.
        H.nodes[c]['dUele'] = 0.
        H.nodes[c]['Uele'] = uTP
        H.nodes[c]['dUrel'] = 0.
        H.nodes[c]['dUelerel'] = 0.
    #
    return H.cTP 

# -----------------------------------------------------------------------|--

def propagate_binomial(H, c):
    '''
    (nGOI_0, kWfix_0) razširimo po vsem omrežju
    
    '''
    H.nodes[c]['nGOI'] = H.nodes[c]['nGOI_0']
    H.nodes[c]['Pvel'] = H.nodes[c]['Pvel_0']
    H.nodes[c]['Pdod'] = H.nodes[c]['Pdod_0']
    H.nodes[c]['Pele'] = H.nodes[c]['Pele_0']

    for ot in list(H.successors(c)):

        # if H.edges[c, ot]['exclude']:                                  # !!!
            # continue

        propagate_binomial(H, ot)

        ot_nGOI = H.nodes[ot]['nGOI']
        ot_kWfix = H.nodes[ot]['Pvel']
        ot_kWdod = H.nodes[ot]['Pdod']
        ot_kWele = H.nodes[ot]['Pele']

        H.edges[c, ot]['nGOI'] = ot_nGOI
        H.edges[c, ot]['Pvel'] = ot_kWfix
        H.edges[c, ot]['Pdod'] = ot_kWdod
        H.edges[c, ot]['Pele'] = ot_kWele

        H.nodes[c]['nGOI'] += ot_nGOI
        H.nodes[c]['Pvel'] += ot_kWfix
        H.nodes[c]['Pdod'] += ot_kWdod
        H.nodes[c]['Pele'] += ot_kWele

# -----------------------------------------------------------------------|--

def evaluate_binomial(spe, H, c):

    nGOI_0 = H.nodes[c]['nGOI_0']
    kWfix_0 = H.nodes[c]['Pvel_0']
    kWdod_0 = H.nodes[c]['Pdod_0']
    H.nodes[c]['P_0'] = binomial(spe, nGOI_0, kWfix_0) + kWdod_0

    nGOI = H.nodes[c]['nGOI']
    kWfix = H.nodes[c]['Pvel']
    kWdod = H.nodes[c]['Pdod']
    H.nodes[c]['P'] = binomial(spe, nGOI, kWfix) + kWdod

    for ot in list(H.successors(c)):

        # if H.edges[c, ot]['exclude']:                                  # !!!
            # continue

        evaluate_binomial(spe, H, ot)

        H.edges[c, ot]['P'] = H.nodes[ot]['P']

# -----------------------------------------------------------------------|--

def pretoki_moci(H, uTP):

    G = H.copy()

    padci_dvigi_napetosti_vodov(H)

    korekcija_vozlicnih_napetosti(H, uTP, H.cTP)

    delta = 0.
    for c in H.nodes():
        dif = G.nodes[c]['U'] - H.nodes[c]['U']
        dif = abs(dif)
        if dif > delta:
            delta = dif

    return delta

# -----------------------------------------------------------------------|--

def NNizgube(H, c):
    '''
    Izračun izgub moči po vozliščih glede na znane izgube kablov.
    
    '''
    #
    r, q = 0., 0.
    #
    for d in H.successors(c):
        #
        # if H.edges[c, d]['exclude']:                                   # !!!
            # continue
        #
        H.edges[c, d]['dP'] = H.edges[c, d]['dP_0'] + NNizgube(H, d)
        #
        r += H.edges[c, d]['dP']
        q += H.edges[c, d]['dP_0']
    #
    H.nodes[c]['dP'] = r
    H.nodes[c]['dP_0'] = q
    #
    return r

# -----------------------------------------------------------------------|--

def letne_izgubne_ure(T0):
    '''
    Odvisnost izgubnih ur od letnih obratovalnih ur.
    
    '''
    return 0.17 * T0 + 0.83 * T0 ** 2 / 8760

# -----------------------------------------------------------------------|--

def metla(h):
    '''
    Definicija metlastih grafov.
    
    '''
    for c in h.nodes():
        x = h.nodes[c]['distTP']
        y1 = h.nodes[c]['dUrel']
        y2 = h.nodes[c]['dUelerel']
        h.nodes[c]['nppoint'] = (x, y1, y2)

# Priprava za risanje grafov na način da večji pretoki moči po vodih
#     bodo prikazani z debelejšo črto

    # for u, v in H.edges():
        # H.edges[u,v]['lineW'] = (10 / 100.) * H.edges[u,v]['P']

# Označimo vozlišča, kjer je dobra napetost in kjer je slaba napetost
#    zato da jih potem lahko rišemo,
#    recimo z rdečo barvo če ima porabnik slabo napetost

    # goodvoltage = []
    # for n in H.notTPs:
        # print(n, H.nodes[n])
        # if (400. / sqrt(3)) * (1 - Vmin) <= H.nodes[n]['U']:
            # goodvoltage.append(n)
    # H.goodvoltage = goodvoltage
    # H.lowvoltage = list(set(H.notTPs) - set(goodvoltage))

# Za risanje metlastih grafov:
#       grafi napetosti vozlišč v odvisnosti od razdalje od TP
    # posmetla = {}
    # for c in H.nodes():
        # posmetla[c] = (H.nodes[c]['distTP'], H.nodes[c]['U'])
    # H.posmetla = posmetla

# -----------------------------------------------------------------------|--

def distance_resistance_conductance_TP(h):
    '''
    Izračuna razdalje, upornosti in prevodnosti od vozlišč do TP.
    
    '''
    WHAT = {'dolz': 'distTP', 'resis': 'resisTP'}
    #
    prim = h.cTP
    for k, v in WHAT.items():
        #
        h.nodes[prim][v] = 0.
        #
        distance_resistance_TP_rek(h, prim, k, v)
    #
    for jd, q in h.nodes(data=True):
        q['conducTP'] = conduc_func(q['resisTP'])
    #
    # for jd, q in h.nodes(data=True):
        # print(jd)
        # for k, v in q.items():
            # print('    ', k, v)
    # print()
    # for jd1, jd2, q in h.edges(data=True):
        # print(jd1, jd2)
        # for k, v in q.items():
            # print('    ', k, v)

def distance_resistance_conductance_TP_b(h):
    '''
    Izračuna razdalje, upornosti in prevodnosti od vozlišč do TP.
    
    '''
    WHAT = {'dolz': 'distTP', 'resis': 'resisTP'}
    #
    prim = h.cTP
    for k, v in WHAT.items():
        #
        h.nodes[prim][v] = 0.
        #
        distance_resistance_TP_b_rek(h, prim, k, v)
    #
    for jd, q in h.nodes(data=True):
        q['conducTP'] = conduc_func(q['resisTP'])
    #
    # for jd, q in h.nodes(data=True):
        # print(jd)
        # for k, v in q.items():
            # print('    ', k, v)
    # print()
    # for jd1, jd2, q in h.edges(data=True):
        # print(jd1, jd2)
        # for k, v in q.items():
            # print('    ', k, v)

# -----------------------------------------------------------------------|--

def izraccunaj_izvode(h):
    '''
    Propagira izvode na podlagi povezav levela L1.
    
    '''
    C = '-'
    prim = h.cTP
    h.nodes[prim]['izvod'] = C
    for sek in h.successors(prim):

        h.edges[prim, sek]['izvod'] = C
        h.nodes[sek]['izvod'] = C
        for i, ter in enumerate(h.successors(sek)):
            ii = i + 1
            izvod = h.edges[sek, ter]['izvod']
            izvod = izvod.strip()
            if len(izvod) < 5 or izvod[:5] != 'IZV-R':
                izvod = f'IZV-R{ii:02d} {izvod:s}'
            izraccunaj_izvode_rek(h, izvod, sek, ter)

# -----------------------------------------------------------------------|--
# -3---------------------------------------------------------------------|--

def padci_dvigi_napetosti_vodov(H):
    '''
    Preračun kW pretokov moči po vodih v tokove in napetosti (po vodih).

    Input:
        H.edges[u,v]['P']                       pravkar izračunano, kW po vodih
        H.edges[u,v]['resis']                    upornost vodov v Ohmih

    Output:
        H.edges[u,v]['Ib']                tok A
        H.edges[u,v]['dU']                 padec napetosti v absolutnih voltih V
        H.edges[u,v]['dUrel']             padec napetosti v relativnih voltih %
    '''
    K = 3 + (1 / 3) ** 2                               # I_null = I_faze / 3
    cTP = H.cTP
    uTP = H.nodes[cTP]['U']
    

    for (u, v) in H.edges():

        Upovp = (H.nodes[u]['U'] + H.nodes[v]['U']) / 2

        H.edges[u, v]['Upovp'] = Upovp

        tok = 1000 * H.edges[u, v]['P'] / (3 * Upovp)
        H.edges[u, v]['Ib'] = tok
        H.edges[u, v]['Irel'] = 100 * tok / H.edges[u, v]['Imax']

        H.edges[u, v]['dU'] = tok * H.edges[u, v]['resis']
        H.edges[u, v]['dUrel'] = 100 * H.edges[u, v]['dU'] / uTP

        H.edges[u, v]['dP_0'] = K * tok**2 * H.edges[u, v]['resis'] / 1000

        tokele = 1000 * H.edges[u, v]['Pele'] / (3 * Upovp)
        H.edges[u, v]['Iele'] = tokele
        H.edges[u, v]['Ielerel'] = 100 * tokele / H.edges[u, v]['Imax']
        H.edges[u, v]['dUele'] = tokele * H.edges[u, v]['resis']

        H.edges[u, v]['dUelerel'] = 100 * H.edges[u, v]['dUele'] / uTP

# -----------------------------------------------------------------------|--

def korekcija_vozlicnih_napetosti(H, uTP, c):

    for ot in list(H.successors(c)):

        # if H.edges[c, ot]['exclude']:                                  # !!!
            # continue

        cU = H.nodes[c]['U']

        # faktor 0.7 preprečuje prehitro konvergenco
        H.nodes[ot]['U'] = max(cU - H.edges[c, ot]['dU'], 0.7 * cU )
        H.nodes[ot]['Uele'] = H.nodes[c]['Uele'] + H.edges[c, ot]['dUele']

        H.nodes[ot]['dU']    = uTP - H.nodes[ot]['U']
        H.nodes[ot]['dUele'] = H.nodes[ot]['Uele'] - uTP

        H.nodes[ot]['dUrel']    = 100 * H.nodes[ot]['dU']    / uTP
        H.nodes[ot]['dUelerel'] = 100 * H.nodes[ot]['dUele'] / uTP

        korekcija_vozlicnih_napetosti(H, uTP, ot)

# -----------------------------------------------------------------------|--

def distance_resistance_TP_rek(H, c, _, _TP):
    for d in list(H.successors(c)):
        H.nodes[d][_TP] = H.nodes[c][_TP] + H.edges[c, d][_]
        distance_resistance_TP_rek(H, d, _, _TP)

def distance_resistance_TP_b_rek(H, c, _, _TP):
    for d in list(H.successors(c)):
        povprecje = 0.
        n = H.number_of_edges(c, d)
        for i in range(n):
            qq = H.edges[c, d, i]
            povprecje += qq[_]
        povprecje /= n
        H.nodes[d][_TP] = H.nodes[c][_TP] + povprecje
        distance_resistance_TP_b_rek(H, d, _, _TP)

# -----------------------------------------------------------------------|--

def izraccunaj_izvode_rek(h, izvod, c, d):
    h.nodes[d]['izvod'] = izvod
    for e in h.successors(d):
        h.edges[d, e]['izvod'] = izvod
        izraccunaj_izvode_rek(h, izvod, d, e)

# -----------------------------------------------------------------------|--

#
# ### ENOPOLNA SHEMA
#

# -0-----------------------------------------------------------------------|--

def enopolna_shema(h, dx=30., dy=30., alpha=1.):
    '''
    Glede na h = nx.DiGraph() znova kreira enopolne sheme.
    
    Input
    
    Output: h.nodes[_]['respoint']                   relativna enopolna shema
    
    Output: h.nodes[_]['espoint']                              enopolna shema
    Output: h.edges[_, _]['eslinee']                           enopolna shema

    Output: h.edges[_, _]['line']                                     daljice
    '''
    #
    # daljice med vozlisci:
    for jd1, jd2 in h.edges():
        linee = h.edges[jd1, jd2]['linee']
        h.edges[jd1, jd2]['line'] = [linee[0], linee[-1]]
    #
    # število potomcev 'nsucc' h.nodes[jd]['nsucc']
    nsucc = calculate_number_of_successors(h, h.cTP)
    #
    # relativne matematične pozicije vozlišč h.nodes[jd]['respoint']
    zbir1 = enopolna1(h)
    #
    # topološke poz.vozlišč h.nodes[jd]['espoint']
    #                       h.edges[jd1, jd2]['eslinee']
    zbir2 = enopolna2(h, dx, dy, alpha)
    #
    # enopolna shema z realnimi dolžinami kablov
    zbir3 = enopolna3(h)
    #
    # for zb in zbir1: print(zb)
    # print()
    # for zb in zbir2: print(zb)
    # print()
    # for zb in zbir3: print(zb)
    #
    napetostni_profil(h, dx)
    #
    profil_upornosti(h, dx)
    #
    zbiralke = dict()
    zbiralke['zbir1'] = zbir1
    zbiralke['zbir2'] = zbir2
    zbiralke['zbir3'] = zbir3
    zbiralke['zbir2avec'] = avec_serif(dx, dy, zbir2)
    zbiralke['zbir3avec'] = avec_serif(dx, dy, zbir3)
    #
    return zbiralke

def avec_serif(dx, dy, zbir):
    avec = []
    for zb in zbir:
        x0, y0 = zb[0]
        x1, y1 = zb[1]
        xx0, xx1 = x0 - dx / 5, x1 + dx / 5
        zb2 = [(xx0, y0), (xx1, y1)]
        avec.append(zb2)
    return avec

# -1-----------------------------------------------------------------------|--

def calculate_number_of_successors(h, c):
    '''
    Izračuna število napajanih vozlišč (vključujoč prazna vozl.).
    
    Napajana vozlišča == otroci
    
    Input:  h = nx.DiGraph()
    Output: nsucc                # število napajanih vozlišč
            h.nodes[.]['nsucc']  # isto
    '''
    # Alternativna nova rešitev
      # če je vozlišče brez otrok, je nsucc = 0
      # vendar tako vozlišče upoštevamo kot 1, v primeru ko je samo otrok

    nsucc = 0
    otroci = list(h.successors(c))
    for ot in otroci:
        nsucc_ = calculate_number_of_successors(h, ot)
        nsucc_ = nsucc_ if nsucc_ != 0 else 1
        nsucc += nsucc_
    h.nodes[c]['nsucc'] = nsucc
    # print('c = {}, nsucc = {}'.format(c, nsucc))
    return nsucc

# -------------------------------------------------------------------------|--

def enopolna1(h):
    '''
    Definicija relativnih pozicij točk v enopolni shemi.
    
    Input:  h = nx.DiGraph()
            h.nodes[_]['nsucc']
    
    Output: h = nx.DiGraph()
            h.nodes[_]['respoint']    # relative-es-point
    '''
    i, j = 0, 0
    c = h.cTP
    h.nodes[c]['respoint'] = (j + (h.nodes[c]['nsucc'] - 1) / 2, -i)

    roditelji = [(c, j)]

    while roditelji:
        otroci = []
        i += 1
        for c, j in roditelji:
            c_otroci = list(h.successors(c))
            T1 = h.nodes[c]['point']
            kot_otroci = []
            for o in c_otroci:
                T2 = h.nodes[o]['point']
                theta = kot(T1, T2)
                kot_otroci.append((theta, o))
            kot_otroci.sort()
            c_otroci = [_[1] for _ in kot_otroci]
            for ot in c_otroci:
                ot_sirina = max(1, h.nodes[ot]['nsucc'])
                otroci.append((ot, j))
                h.nodes[ot]['respoint'] = (j + (ot_sirina - 1) / 2, -i)
                j += ot_sirina
        roditelji = otroci

    xshift = h.nodes[h.cTP]['respoint'][0]

    zbiralke = []
    for jd in h.nodes():
        # if jd == h.cTP:
            # continue
        x, y = h.nodes[jd]['respoint']

        h.nodes[jd]['respoint'] = (x - xshift, y)
        a = h.nodes[jd]['respoint'][0]
        b = h.nodes[jd]['respoint'][1]
        # print(a, b, type(a), type(b))
        otroci = list(h.successors(jd))
        d = len(otroci)
        rampa = [h.nodes[o]['respoint'][0] - xshift for o in otroci]
        minmax = [(min(rampa), y), (max(rampa), y)] if rampa else []
        # print(f'{jd} = ({a:4.1f}, {b:4.1f}) nsucc = {d:d}', otroci, rampa, minmax)
        if minmax and jd != h.cTP:
            zbiralke.append(minmax)
        # mm = [ for [m1, m2] in minmax]
    # print()
    # print()
    # print(zbiralke)
    return zbiralke

# -----------------------------------------------------------------------|--

def enopolna2(h, dx, dy, alpha):
    '''
    Definicija absolutnih pozicij točk in linij v enopolni shemi.
    
    Input:  dx                         # navpična razdalja (m)
            dy                         # vodoravna razdalja (m)
            alpha                      # 0. < faktor pobešanja rame < 1.
            h = nx.DiGraph()
            h.nodes[h.cTP]['point']    # pozicija TP ostane fiksna
            h.nodes[_]['respoint']     # relative-es-point
    
    Output: h = nx.DiGraph()
            h.nodes[_]['espoint']      # es-point, absolute
            h.edges[_, _]['eslinee']   # es-linee, poligonska črta
    '''
    tp = h.cTP
    tpx, tpy = h.nodes[tp]['point'][0], h.nodes[tp]['point'][1]

    for jd in h.nodes():

        rx, ry = h.nodes[jd]['respoint'][0], h.nodes[jd]['respoint'][1]

        x, y = tpx + dx * rx, tpy + dy * ry
        x, y = round(x, 2), round(y, 2)

        h.nodes[jd]['espoint'] = (x, y)

    for jd1, jd2 in h.edges():

        x1, y1 = h.nodes[jd1]['espoint'][0], h.nodes[jd1]['espoint'][1]
        x2, y2 = h.nodes[jd2]['espoint'][0], h.nodes[jd2]['espoint'][1]

        x12, y12 = x2, y2 + alpha * (y1 - y2)
        x12, y12 = round(x12, 2), round(y12, 2)

        h.edges[jd1, jd2]['eslinee'] = [(x1, y1), (x12, y12), (x2, y2)]

    zbiralke = []
    for jd in h.nodes():
        # if jd == h.cTP:
            # continue
        a, b = h.nodes[jd]['espoint']
        otroci = list(h.successors(jd))
        rampa = [h.nodes[o]['espoint'][0] for o in otroci]
        minmax = [(min(rampa), b), (max(rampa), b)] if rampa else []
        if minmax and jd != h.cTP:
            zbiralke.append(minmax)

    return zbiralke

# -----------------------------------------------------------------------|--

def enopolna3(h):
    '''
    Definicija enopolne sheme z realnimi dolžinami.
    
    Input:  dx                         # navpična razdalja (m)
            dy                         # vodoravna razdalja (m)
            alpha                      # 0. < faktor pobešanja rame < 1.
            h = nx.DiGraph()
            h.nodes[h.cTP]['point']    # pozicija TP ostane fiksna
            h.nodes[_]['respoint']     # relative-es-point
    
    Output: h = nx.DiGraph()
            h.nodes[_]['esrpoint']      # es-r-point, absolute
            h.edges[_, _]['esrlinee']   # es-r-linee, poligonska črta
    '''
    for jd in h.nodes():
        h.nodes[jd]['esrpoint'] = h.nodes[jd]['espoint']
    for jd1, jd2 in h.edges():
        h.edges[jd1, jd2]['esrlinee'] = h.edges[jd1, jd2]['eslinee']
    #
    prim = h.cTP
    #
    h.nodes[prim]['esrpoint'] = h.nodes[prim]['espoint']
    for sek in list(h.successors(prim)):
        h.nodes[sek]['esrpoint'] = h.nodes[sek]['espoint']
        h.edges[prim, sek]['esrlinee'] = h.edges[prim, sek]['eslinee']
        for ter in list(h.successors(sek)):
            h.nodes[ter]['esrpoint'] = h.nodes[ter]['espoint']
            h.edges[sek, ter]['esrlinee'] = h.edges[sek, ter]['eslinee']
            enopolna3_rec(h, ter)

    zbiralke = []
    for jd in h.nodes():
        # if jd == h.cTP:
            # continue
        a, b = h.nodes[jd]['esrpoint']
        otroci = list(h.successors(jd))
        rampa = [h.nodes[o]['esrpoint'][0] for o in otroci]
        minmax = [(min(rampa), b), (max(rampa), b)] if rampa else []
        if minmax and jd != h.cTP:
            zbiralke.append(minmax)

    return zbiralke

def enopolna3_rec(h, jd1):
    #
    dx, dy = h.nodes[jd1]['esrpoint']
    ex, ey = h.nodes[jd1]['espoint']
    ddy = ey - dy
    for jd2 in list(h.successors(jd1)):
        dolz = h.edges[jd1, jd2]['dolz']
        a, b, c = h.edges[jd1, jd2]['esrlinee']
        ax, ay = a
        bx, by = b
        cx, cy = c
        cy = by - dolz
        c = (cx, cy)
        a = ax, ay - ddy
        b = bx, by - ddy
        c = cx, cy - ddy
        h.nodes[jd2]['esrpoint'] = c
        h.edges[jd1, jd2]['esrlinee'] = [a, b, c]
        enopolna3_rec(h, jd2)

# -----------------------------------------------------------------------|--

def napetostni_profil(h, dx):
    '''
    Definicija metlastih grafov.
    
    Input:  dx                         # navpična razdalja (m)
            h = nx.DiGraph()
            h.nodes[h.cTP]['point']    # pozicija TP ostane fiksna
            h.nodes[_]['respoint']     # relative-es-point
    
    Output: h = nx.DiGraph()
            h.nodes[_]['esrpoint']      # es-r-point, absolute
            h.edges[_, _]['esrlinee']   # es-r-linee, poligonska črta
    '''
    cTP = h.cTP
    cTPpoint = h.nodes[cTP]['point']
    sredina = cTPpoint[0]
    #
    for jd in h.nodes():
        px, py = h.nodes[jd]['esrpoint']
        try:
            dUrel = h.nodes[jd]['dUrel']
        except KeyError:
            dUrel = 0.
        try:
            qx = sredina - 3 * dx * dUrel
        except TypeError:
            qx = sredina
        qy = py
        h.nodes[jd]['metlapoint'] = (qx, qy)
    for jd1, jd2 in h.edges():
        q1 = h.nodes[jd1]['metlapoint']
        q2 = h.nodes[jd2]['metlapoint']
        h.edges[jd1, jd2]['metlalinee'] = [q1, q2]

# -----------------------------------------------------------------------|--

def profil_upornosti(h, dx):
    cTP = h.cTP
    cTPpoint = h.nodes[cTP]['point']
    sredina = cTPpoint[0]
    #
    for jd in h.nodes():
        px, py = h.nodes[jd]['esrpoint']
        resisTP = h.nodes[jd]['resisTP']
        try:
            qx = sredina + 100 * dx * resisTP
        except TypeError:
            qx = sredina
        qy = py
        h.nodes[jd]['resismetlapoint'] = (qx, qy)
    for jd1, jd2 in h.edges():
        q1 = h.nodes[jd1]['resismetlapoint']
        q2 = h.nodes[jd2]['resismetlapoint']
        h.edges[jd1, jd2]['resismetlalinee'] = [q1, q2]

#
# ### VAROVALKE
#

# -0-----------------------------------------------------------------------|--

def varovalke(h, model_dir):
    pth = os.path.join(model_dir, 'varovalke.txt')
    with open(pth, 'w') as f:
        varovalke_(h, f)

def varovalke_(h, f):

    varovalke_1(h, f)

    xk, rkm = varovalke_2(f)

    varovalke_3(h, f, xk, rkm)

    varovalke_4(h, f)

# -------------------------------------------------------------------------|--
# -1-----------------------------------------------------------------------|--

def varovalke_1(h, f):
    '''
    Morebitno tanjšanje kablov v smeri porabnikov.

    '''
    sw_denis_duh = True
    prim = h.cTP
    if sw_denis_duh:
        # 1a sw_denis_duh == True: brez tanšanja presekov
        #
        for jd1, jd2 in h.edges():
            h.edges[jd1, jd2]['presek2'] = h.edges[jd1, jd2]['presek']
            h.edges[jd1, jd2]['rspec2'] = h.edges[jd1, jd2]['rspec']
            h.edges[jd1, jd2]['imax2'] = h.edges[jd1, jd2]['Imax']
            h.edges[jd1, jd2]['resis2'] = h.edges[jd1, jd2]['resis']
    else:
        # 1b sw_denis_duh == False: tanšanje presekov
        #
        # presek2 ... presek, ki se kvečjemu tanjša v smeri porabnikov
        # imax2 ..... ustrezni maksimalni tok
        # rspec2 .... ustrezna specifična upornost
        # resis2 .... ustrezni upornost
        # resisTP2 .. ustrezna upornost do TP
        for sek in list(h.successors(prim)):
            h.edges[prim, sek]['presek2'] = h.edges[prim, sek]['presek']
            naredi_presek2(h, prim, sek)
        mat2 = 'Al'
        for jd1, jd2 in h.edges():
            d = h.edges[jd1, jd2]['dolz']
            S2 = h.edges[jd1, jd2]['presek2']
            rspec2 = rspec_func(S2, mat2)
            cspec2 = cspec_func(S2, mat2)
            imax2 = imax_func(2, S2, mat2)
            resis2 = d * rspec2 / 1000.
            conduc2 = conduc_func(resis2)
            h.edges[jd1, jd2]['rspec2'] = rspec2
            h.edges[jd1, jd2]['imax2'] = imax2
            h.edges[jd1, jd2]['resis2'] = resis2
            h.edges[jd1, jd2]['conduc2'] = conduc2
    h.nodes[prim]['resisTP2'] = 0.0
    naredi_resisTP2(h, prim)

# -------------------------------------------------------------------------|--

def varovalke_2(f):
    '''
    Splošni parametri.

    '''
    xk = 0.08     # induktivna upornost kabla (Ohm/km)
    rkm = 0.5e-3  # upornost enega kontaktnega mesta (Ohm)
    print(file=f)
    print('induktivna upornost kablov xk = {:.2f} Ohm/km'
            .format(xk), file=f)
    print('upornost kontaktnega mesta rkm = {:.4f} Ohm'
            .format(rkm), file=f)

    return xk, rkm

# -------------------------------------------------------------------------|--

def varovalke_3(h, f, xk, rkm):
    '''
    Izračun impedanc in kratkostičnih tokov.

    '''
    # poskrbimo da so pravkar izračunana polja
    # definirana za prav vsa vozlišča in prav vse povezave

    for jd in h.nodes():
        h.nodes[jd]['Zdir'] = 0.
        h.nodes[jd]['Znic'] = 0.
        h.nodes[jd]['Zekv'] = 0.
        h.nodes[jd]['Ik1'] = 0.
        h.nodes[jd]['Ik3'] = 0.
    for jd1, jd2 in h.edges():
        h.edges[jd1, jd2]['Ik1'] = 0.
        h.edges[jd1, jd2]['Ik3'] = 0.
        h.edges[jd1, jd2]['Iaa'] = 0.
        h.edges[jd1, jd2]['Ia'] = 0.
        h.edges[jd1, jd2]['Iv'] = 0.

    print(file=f)
    print(file=f)
    print(file=f)
    print('varovalke >>>', h.dispod, h.nnotp, file=f)

    SM = h.S_SN
    SM *= 1.e6
    print(file=f)
    print('moč srednjenapetostne mreže SM = {:.1f} MVA'
            .format(SM / 1e6), file=f)

    # oštevilčimo transformatorje
    # num_tr = 1, 2, ...
    prim = h.cTP
    h.nodes[prim]['num_tr'] = 0
    for j, sek in enumerate(list(h.successors(prim))):
        h.edges[prim, sek]['num_tr'] = 0
        # h.edges[prim, sek]['num_tr'] = j + 1
        h.nodes[sek]['num_tr'] = j + 1
        znano = [sek]
        while znano:
            c = znano.pop()
            dd = list(h.successors(c))
            for d in dd:
                h.edges[c, d]['num_tr'] = j + 1
                h.nodes[d]['num_tr'] = j + 1
            znano.extend(dd)

    for j, sek in enumerate(list(h.successors(prim))):

        opomba = h.edges[prim, sek]['trafo']
        tr = opomba.split(', ')
        ST =  float(tr[0].split()[1]) * 1000
        uk =  float(tr[1].split()[1])
        Pcu = float(tr[2].split()[1]) * 1000
        vezava =    tr[3].split()[1]
        print(file=f)
        print('    transformator #{}  '.format(j + 1), file=f)
        print('    moč transformatorja ST =  {:7.3f} kVA '
                .format(ST / 1000), file=f)
        print('    kratkostična napetost uk =  {:.2f} %'
                .format(uk), file=f)
        print('    izgube moči v bakru Pcu = {:7.3f} kW'
                .format(Pcu / 1000), file=f)
        print('    vezava transformatorja = {}'
                .format(vezava), file=f)

        Rk_0 = h.nodes[sek]['resisTP2']
        l_0 = h.nodes[sek]['distTP']
        nkm_0 = h.nodes[sek]['level']

        for jd in h.nodes():
            if h.nodes[jd]['num_tr'] != j + 1:
                continue

            Rk = h.nodes[jd]['resisTP2'] - Rk_0      # Ohm
            l = (h.nodes[jd]['distTP'] - l_0) / 1000 # km
            nkm = (h.nodes[jd]['level'] - nkm_0) * 3 # 3 kn.mesta/kabel
            print(file=f)
            print(file=f)
            print(file=f)
            print('        vozlišče {}'.format(jd), file=f)
            print('        razdalja (do TP) distTP = {:.1f} m'
                    .format(1000 * l), file=f)
            print('        upornost (do TP) resisTP = {:.3f} Ohm'
                    .format(Rk), file=f)
            print('        kontaktnih mest (do TP) nkm = {}'
                    .format(nkm), file=f)

            # dbg = True if jd == '5574-7281-1535-3695' else False
            dbg = True
            if dbg:
                print(file=f)
                print('Rk =', Rk, file=f)
                print('Rk_0 =', Rk_0, file=f)
                print(file=f)

            Ik1, Ik3, Z, Z0, Ze = okvarnazanka(
                    f, SM, ST, uk, Pcu, vezava, Rk, xk, l, rkm, nkm, dbg)

            h.nodes[jd]['Zdir'] = Z
            h.nodes[jd]['Znic'] = Z0
            h.nodes[jd]['Zekv'] = Ze
            h.nodes[jd]['Ik1'] = Ik1
            h.nodes[jd]['Ik3'] = Ik3

        for jd1, jd2 in h.edges():
            if h.edges[jd1, jd2]['num_tr'] != j + 1:
                continue

            h.edges[jd1, jd2]['Ik1'] = h.nodes[jd2]['Ik1']
            h.edges[jd1, jd2]['Ik3'] = h.nodes[jd2]['Ik3']

            h.edges[jd1, jd2]['Ia'] = min(
                    h.edges[jd1, jd2]['Ik1'] / 2.5,
                    h.edges[jd1, jd2]['imax2'])

# -------------------------------------------------------------------------|--

def varovalke_4(h, f):
    '''
    Zmanjšanje števila varovalk.

    Ia --> Iaa, Iv
    '''
    prim = h.cTP
    for jd1, jd2 in h.edges():
        h.edges[jd1, jd2]['Iaa'] = h.edges[jd1, jd2]['Ia']

    # zmanjševanje števila varovalk v smeri proti TP
    for sek in list(h.successors(prim)):
        for tert in list(h.successors(sek)):
            jd1 = tert
            quart = list(h.successors(jd1))
            if quart:
                jd2 = quart[0]
                petek(h, jd1, jd2)

    # Iaa --> Iv
    primsek = set(h.successors(prim))
    primsek.add(prim)
    for (jd1, jd2) in h.edges():
        if jd1 in primsek:
            h.edges[jd1, jd2]['Iv'] = 0
        else:
            Iaa = h.edges[jd1, jd2]['Iaa']
            h.edges[jd1, jd2]['Iv'] = realna_varovalka(Iaa)

    # preprečiti ponavljanje varovalk navzdol po vertikali
    for sek in list(h.successors(prim)):
        for tert in list(h.successors(sek)):
            jd1 = tert
            quart = list(h.successors(jd1))
            if quart:
                jd2 = quart[0]
                Iv12 = h.edges[jd1, jd2]['Iv']
                cetrtek(h, jd1, jd2, Iv12)

    # preprečiti da bi bila večja varovalka navzdol po vertikali
    for sek in list(h.successors(prim)):
        for tert in list(h.successors(sek)):
            jd1 = tert
            quart = list(h.successors(jd1))
            if quart:
                jd2 = quart[0]
                Iv12 = h.edges[jd1, jd2]['Iv']
                ponedeljek(h, jd1, jd2, Iv12)

# -------------------------------------------------------------------------|--
# -2-----------------------------------------------------------------------|--

def naredi_presek2(h, jd1, jd2):
    '''
    presek2: padajoči (ne naraščajoči) presek v smeri stran od TP

    '''
    fi12ok = h.edges[jd1, jd2]['presek2']

    for jd3 in list(h.successors(jd2)):

        fi23 = h.edges[jd2, jd3]['presek']

        if fi12ok > 0.001:
            h.edges[jd2, jd3]['presek2'] = min(fi12ok, fi23)
        else:
            h.edges[jd2, jd3]['presek2'] = fi23

        naredi_presek2(h, jd2, jd3)

# -------------------------------------------------------------------------|--

def naredi_resisTP2(h, jd1):
    '''
    resisTP2: upornosti do TP glede na ne-naraščujoči presek2

    '''
    for jd2 in list(h.successors(jd1)):

        _ = 'resisTP2'

        h.nodes[jd2][_] = h.nodes[jd1][_] + h.edges[jd1, jd2]['resis2']

        naredi_resisTP2(h, jd2)

# -------------------------------------------------------------------------|--

def okvarnazanka(f, SM, ST, uk, Pcu, stik, Rk, xk, l, rkm, nkm, dbg=True):

    U = 400.0    # napetost NN omrežja
    # k80 = 1.24   # faktor R80/R20
    k80 = 1.00   # faktor R80/R20, že upoštevano v Leonovi teoriji
    Rkm = 0.0005 # Ohm / kontaktno mesto
    ku = 0.80    # faktor zaščite za eksplozijsko ogrožene prostore
    # ku = 0.95    # faktor zaščite za ostale prostore

    cZ, cZT, cZK = direktne(
            f, U, SM, ST, uk, Pcu, Rk, k80, xk, l, rkm, nkm, dbg)

    cZ0 = nicelne(f, stik, cZT, cZK, dbg)

    Ik1, Ik3, Ze = tokovi(f, U, ku, cZ, cZ0, dbg)

    return Ik1, Ik3, abs(cZ), abs(cZ0), Ze

# -------------------------------------------------------------------------|--

def petek(h, jd1, jd2):
    '''
    Ia --> Iaa.

    varovalka Iaa sinov JE potrebna, če
        ima očeta z večjim presekom
        sicer ima očeta z istim presekom, vendar
            pogoj 2 * Ib < Ia ni izpolnjen (pri sinu)

    vrednost Iaa od najmanjše nepotrebne varovalke sinov
      vsilimo kot Iaa očeta

    na koncu za vse nepotrebne varovalke postavimo Iaa = 0.0
    '''
    fi12 = round(h.edges[jd1, jd2]['presek2'], 1)
    xxx_Iaa23 = []

    for jd3 in list(h.successors(jd2)):

        petek(h, jd2, jd3)
        fi23 = round(h.edges[jd2, jd3]['presek2'], 1)

        if fi23 == fi12:
            Ib23 = h.edges[jd2, jd3]['Ib']
            Iaa23 = h.edges[jd2, jd3]['Iaa']
            if 2.0 * Ib23 < Iaa23:
                xxx_Iaa23.append(Iaa23)
                h.edges[jd2, jd3]['Iaa'] = 0.0

        elif fi23 > fi12:                          # Denis Duh
            h.edges[jd2, jd3]['Iaa'] = 0.0

    if xxx_Iaa23:
        h.edges[jd1, jd2]['Iaa'] = min(xxx_Iaa23)

# -----------------------------------------------------------------------|--

def cetrtek(h, jd1, jd2, xxx_Iv12):
    '''
    Postavimo na 0. varovalke potomcem, ki imajo isti presek

    premikamo se v smeri od izvodov TP proti porabnikom

    če je pri istem preseku očeta in sina
        varovalka očeta Iv enaka varovalki sina,
            postavimo varovalko sina Iv na 0.0
            postopek ponavljamo rekurzivno
    '''
    fi12 = round(h.edges[jd1, jd2]['presek2'], 1)

    for jd3 in list(h.successors(jd2)):

        fi23 = round(h.edges[jd2, jd3]['presek2'], 1)
        Iv23 = h.edges[jd2, jd3]['Iv']

        if fi23 == fi12 and Iv23 == xxx_Iv12:
            cetrtek(h, jd2, jd3, xxx_Iv12)
            h.edges[jd2, jd3]['Iv'] = 0.
        else:
            cetrtek(h, jd2, jd3, Iv23)

# -----------------------------------------------------------------------|--

def ponedeljek(h, jd1, jd2, xxx_Iv12):
    '''
    Če naletimo na večjo varovalko, jo postavimo na nič.

    premikamo se v smeri od izvodov TP proti porabnikom
    '''
    for jd3 in list(h.successors(jd2)):

        Iv23 = h.edges[jd2, jd3]['Iv']

        if Iv23 >= xxx_Iv12:
            ponedeljek(h, jd2, jd3, xxx_Iv12)
            h.edges[jd2, jd3]['Iv'] = 0.0
            # h.edges[jd2, jd3]['Iv'] = xxx_Iv12

        elif Iv23 == 0:
            ponedeljek(h, jd2, jd3, xxx_Iv12)

        else:
            ponedeljek(h, jd2, jd3, Iv23)

# -------------------------------------------------------------------------|--

def realna_varovalka(Iaa):
    '''
    Vrne prvo manjšo varovalko, dostopno na trgu

    '''
    if Iaa < 0.001:
        return 0

    Ireal = [0, 2, 4, 6, 10, 16, 20, 25, 32, 35, 40, 50,
            63, 80, 100, 125, 160, 200, 224, 250, 280,
            300, 315, 355, 400, 425, 500, 630, 710,
            800, 900, 1000, 1250]

    Ireal.sort(reverse=True)

    for Iv in Ireal:
        if Iv < Iaa:
            return Iv

# -------------------------------------------------------------------------|--
# -3-----------------------------------------------------------------------|--

def direktne(f, U, SM, ST, uk, Pcu, Rk, k80, xk, l, rkm, nkm, dbg):
    '''
    Izračun direktnih impedanc.

    '''
    # M mreža
    XM = 1.1 * U ** 2 / SM
    RM = 0.1 * XM
    cZM = complex(RM, XM)
    ZM = abs(cZM)
    FM = math.atan2(XM, RM)
    CFM = math.cos(FM)

    # T transformator
    ZT = (uk / 100) * U ** 2 / ST
    RT = Pcu * U ** 2 / ST ** 2
    if ZT < RT:
        ZT = RT
    XT = math.sqrt(ZT ** 2 - RT ** 2)
    cZT = complex(RT, XT)
    FT = math.atan2(XT, RT)
    CFT = math.cos(FT)

    # K kabel
    RK = Rk * k80
    XK = l * xk
    cZK = complex(RK, XK)
    ZK = abs(cZK)
    FK = math.atan2(XK, RK)
    CFK = math.cos(FK)

    if dbg:
        print(file=f)
        print('k80=', k80, file=f)
        print('Rk=', Rk, file=f)
        print('RK=', RK, file=f)
        print('xk=', xk, file=f)
        print('l=', l, file=f)
        print('XK=', XK, file=f)
        print('cZK=', cZK, file=f)
        print('ZK=', ZK, file=f)
        print('FK=', FK, file=f)
        print('CFK=', CFK, file=f)
        # print('=', , file=f)
        # print('=', , file=f)
        print(file=f)

    # KM kontaktna mesta
    RKM = nkm * rkm
    cZKM = complex(RKM, 0)
    ZKM = abs(cZKM)

    # print('ZM = {:.2f} mO, ZT = {:.2f} mO, ZK = {:.2f} mO, ZKM = {:.2f} mO'
            # .format(1000 * ZM, 1000 * ZT, 1000 * ZK, 1000 * ZKM))

    # skupno
    cZ = cZM + cZT + cZK + cZKM
    R = cZ.real
    X = cZ.imag
    Z = abs(cZ)
    F = math.atan2(X, R)
    CF = math.cos(F)

    if dbg:
        pr_direktne(f, RM, XM, ZM, RT, XT, ZT, RK, XK, ZK, RKM, R, X, Z)

    return cZ, cZT, cZK

# -------------------------------------------------------------------------|--

def nicelne(f, stik, cZT, cZK, dbg):
    '''
    Izračun ničelnih impedanc.

    '''
    RT = cZT.real
    XT = cZT.imag
    if stik == 'Dy':
        R0T =          RT
        X0T =   0.95 * XT
    elif stik in ['Dz', 'Yz']:
        R0T =   0.4  * RT
        X0T =   0.1  * XT
    elif stik == 'Yy':
        R0T =          RT
        X0T = 100.0  * XT
    cZ0T = complex(R0T, X0T)
    Z0T = abs(cZ0T)
    F0T = math.atan2(X0T, R0T)
    CF0T = math.cos(F0T)

    RK = cZK.real
    XK = cZK.imag
    R0K = 4 * RK
    X0K = 3 * XK
    cZ0K = complex(R0K, X0K)
    Z0K = abs(cZ0K)
    F0K = math.atan2(X0K, R0K)
    CF0K = math.cos(F0K)

    cZ0 = cZ0T + cZ0K
    R0 = cZ0.real
    X0 = cZ0.imag
    Z0 = abs(cZ0)
    F0 = math.atan2(X0, R0)
    CF0 = math.cos(F0)

    # print('Z0T = {:.2f} mO, Z0K = {:.2f} mO'
            # .format(1000 * Z0T, 1000 * Z0K))

    if dbg:
        pr_nicelne(f, stik, R0T, X0T, Z0T, R0K, X0K, Z0K, R0, X0, Z0)

    return cZ0

# -------------------------------------------------------------------------|--

def tokovi(f, U, ku, cZ, cZ0, dbg):
    '''
    Izračun kratkostičnih tokov.
    '''
    cZe = 2 * cZ + cZ0

    Re = cZe.real
    Xe = cZe.imag
    Ze = abs(cZe)
    Fe = math.atan2(Xe, Re)
    CFe = math.cos(Fe)

    Ik1 = ku * math.sqrt(3) * U / Ze
    Z = abs(cZ)
    Ik3 = U / (math.sqrt(3) * Z)

    if dbg:
        pr_tokovi(f, Re, Xe, Ze, Ik1, Z, Ik3)

    return Ik1, Ik3, Ze

# -------------------------------------------------------------------------|--
# -4-----------------------------------------------------------------------|--

def pr_direktne(f, RM, XM, ZM, RT, XT, ZT, RK, XK, ZK, RKM, R, X, Z):

    q = 180 / math.pi 

    print(file=f)
    print('      *** štiri direktne impedance M, T, K in KM', file=f)

    print(file=f)
    print('   M mreža (_mr)', file=f)
    print('  RM = {:8.2f} mO, upornost (R_mr)'
            .format(1000 * RM), file=f)
    print('  XM = {:8.2f} mO, induktivna upornost (X_mr)'
            .format(1000 * XM), file=f)
    # print(' cZM = {:8.2f} mO, impedanca'.format(1000 * cZM), file=f)
    print('  ZM = {:8.2f} mO, impedanca'.format(1000 * ZM), file=f)
    # print('  FM = {:.1f} stopinj, kot zaostajanja toka'
            # .format(q * FM), file=f)
    # print(' CFM = {:.3f}, cosinus fi'.format(CFM), file=f)

    print(file=f)
    print('   T transformator (_tr)', file=f)
    print('  RT = {:8.2f} mO, upornost (R_tr)'
            .format(1000 * RT), file=f)
    print('  XT = {:8.2f} mO, induktivna upornost (X_tr)'
            .format(1000 * XT), file=f)
    # print(' cZT = {:8.2f} mO, impedanca'.format(1000 * cZT), file=f)
    print('  ZT = {:8.2f} mO, impedanca (Z_tr)'
            .format(1000 * ZT), file=f)
    # print('  FT = {:.1f} stopinj, kot zaostajanja toka '
            # .format(q * FT), file=f)
    # print(' CFT = {:.3f}, cosinus fi'.format(CFT), file=f)

    print(file=f)
    print('   K kabel (_k)', file=f)
    print('  RK = {:8.2f} mO, upornost (R_k)'
            .format(1000 * RK), file=f)
    print('  XK = {:8.2f} mO, induktivna upornost (X_k)'
            .format(1000 * XK), file=f)
    # print(' cZK = {:8.2f} mO, impedanca'.format(1000 * cZK), file=f)
    print('  ZK = {:8.2f} mO, impedanca'.format(1000 * ZK), file=f)
    # print('  FK = {:.1f} stopinj, kot zaostajanja toka'
            # .format(q * FK), file=f)
    # print(' CFK = {:.3f}, cosinus fi'.format(CFK), file=f)

    print(file=f)
    print('  KM kontaktna mesta (_km)', file=f)
    print(' RKM = {:8.2f} mO, skupna upornost (R_km)'
            .format(1000 * RKM), file=f)
    # print('cZKM = {:8.2f} mO, impedanca'.format(1000 * cZKM), file=f)

    print(file=f)
    print('   direktne impedance skupno (_dir)', file=f)
    print('  R = {:8.2f} mO, upornost (R_dir)'
            .format(1000 * R), file=f)
    print('  X = {:8.2f} mO, induktivna upornost (X_dir)'
            .format(1000 * X), file=f)
    # print(' cZ = {:8.2f} mO, impedanca'.format(1000 * cZ), file=f)
    print('  Z = {:8.2f} mO, impedanca'.format(1000 * Z), file=f)
    # print('  F = {:.1f} stopinj, kot zaostajanja toka'
            # .format(q * F), file=f)
    # print(' CF = {:.3f}, cosinus fi'
            # .format(CF), file=f)

# -------------------------------------------------------------------------|--

def pr_nicelne(f, stik, R0T, X0T, Z0T, R0K, X0K, Z0K, R0, X0, Z0):

    q = 180 / math.pi 

    print(file=f)
    print('      *** dve ničelni impedanci T0 in K0', file=f)

    print(file=f)
    print('   T0 transformator (0_tr)', file=f)
    print('stik = {:8s}   , stik transformatorja'
            .format(stik), file=f)
    print(' R0T = {:8.2f} mO, ničelna upornost (R0_tr)'
            .format(1000 * R0T), file=f)
    print(' X0T = {:8.2f} mO, ničelna induktivna upornost (X0_tr)'
            .format(1000 * X0T), file=f)
    # print('cZ0T = {:8.2f} mO, ničelna impedanca'
            # .format(1000 * cZ0T), file=f)
    print(' Z0T = {:8.2f} mO, ničelna impedanca'
            .format(1000 * Z0T), file=f)
    # print(' F0T = {:.1f} stopinj, kot zaostajanja toka '
            # .format(q * F0T), file=f)
    # print('CF0T = {:.3f}, cosinus fi'.format(CF0T), file=f)

    print(file=f)
    print('   K0 kabel (0_k)', file=f)
    print(' R0K = {:8.2f} mO, ničelna upornost (R0_k)'
            .format(1000 * R0K), file=f)
    print(' X0K = {:8.2f} mO, ničelna induktivna upornost (X0_k)'
            .format(1000 * X0K), file=f)
    # print('cZ0K = {:8.2f} mO, ničelna impedanca'
            # .format(1000 * cZ0K), file=f)
    print(' Z0K = {:8.2f} mO, ničelna impedanca'
            .format(1000 * Z0K), file=f)
    # print(' F0K = {:.1f} stopinj, kot zaostajanja toka '
            # .format(q * F0K), file=f)
    # print('CF0K = {:.3f}, cosinus fi'.format(CF0K), file=f)

    print(file=f)
    print('   0 ničelne impedance skupno (_nic)', file=f)
    print('  R0 = {:8.2f} mO, ničelna upornost (R_nic)'
            .format(1000 * R0), file=f)
    print('  X0 = {:8.2f} mO, ničelna induktivna upornost (X_nic)'
            .format(1000 * X0), file=f)
    # print(' cZ0 = {:8.2f} mO, ničelna impedanca'
            # .format(1000 * cZ0), file=f)
    print('  Z0 = {:8.2f} mO, ničalna impedanca'
            .format(1000 * Z0), file=f)
    # print('  F0 = {:.1f} stopinj, kot zaostajanja toka'
            # .format(q * F0), file=f)
    # print(' CF0 = {:.3f}, cosinus fi'.format(CF0), file=f)

# -------------------------------------------------------------------------|--

def pr_tokovi(f, Re, Xe, Ze, Ik1, Z, Ik3):

    print(file=f)
    print('      *** kratkostični tokovi', file=f)

    print(file=f)
    print('   e ekvivalentna impedanca ', file=f)
    print('  Re = {:8.2f} mO, ekvivalentna upornost (R_nic)'
            .format(1000 * Re), file=f)
    print('  Xe = {:8.2f} mO, ekvivalentna induktivna upornost (X_nic)'
            .format(1000 * Xe), file=f)
    # print(' cZe = {:.2f} mO, ekvivalentna impedanca'
            # .format(1000 * cZe), file=f)
    print('  Ze = {:8.2f} mO, ekvivalentna impedanca'
            .format(1000 * Ze), file=f)
    # print('  Fe = {:.1f} stopinj, kot zaostajanja toka'
            # .format(q * Fe), file=f)
    # print(' CFe = {:.3f}, cosinus fi'.format(CFe), file=f)

    print(file=f)
    print('   kratkostični tokovi', file=f)
    print('  Ze = {:8.2f} mO, ekvivalentna impedanca'
            .format(1000*Ze), file=f)
    print(' Ik1 = {:7.1f}   A, tok enopolnega kratkega stika Ik1'
            .format(Ik1), file=f)
    print('   Z = {:8.2f} mO, impedanca 3-pol. kratkega stika'
            .format(1000*Z), file=f)
    print(' Ik3 = {:7.1f}   A, tok 3-pol. kratkega stika Ik3'
            .format(Ik3), file=f)

# -------------------------------------------------------------------------|--

def linear_interpolation(points, x):
    points.sort()
    x1, y1 = points[0][0], points[0][1]
    x9, y9 = points[-1][0], points[-1][1]
    n = len(points)
    if n == 0:
        y = 0
    elif n == 1:
        y = y1
    elif n == 2:
        k = (yn - y1) / (xn - x1)
        y = k * (x - x1) + y1
    else:
        x2, y2 = points[1][0], points[1][1]
        x8, y8 = points[-2][0], points[-2][1]
        if x < x2:
            k = (y2 - y1) / (x2 - x1)
            y = k * (x - x1) + y1
        elif x8 <= x:
            k = (y9 - y8) / (x9 - x8)
            y = k * (x - x8) + y8
        else:
            for i in range(1, n):
                xa, ya = points[i][0], points[i][1]
                xb, yb = points[i+1][0], points[i+1][1]
                if xa <= x < xb:
                    k = (yb - ya) / (xb - xa)
                    y = k * (x - xa) + ya
                    break
    return y

# -------------------------------------------------------------------------|--

#
# ### NXNX_TO_JSON in JSON_TO_NXNX
#

# -------------------------------------------------------------------------|--

def json_to_nxnx(pth):
    '''
    Prebere JSON v hh = [ nx.MultiDiGraph() ].
    
    '''
    hh = []
    if os.path.exists(pth):
        with open(pth, 'r') as f:
            hh_json = json.loads(f.read())
        for h_json in hh_json:
            gtype = h_json['gtype']
            edges = h_json['edges']
            nodes = h_json['nodes']
            if gtype in ('MultiGraph', 'MultiDiGraph'):
                h = nx.MultiDiGraph()
                for jdjd, povezava in edges.items():
                    jd1, jd2, multi = jdjd.split(' ')
                    h.add_edge(jd1, jd2, **povezava)
            else:
                h = nx.DiGraph()
                for jdjd, povezava in edges.items():
                    jd1, jd2 = jdjd.split(' ')
                    h.add_edge(jd1, jd2, **povezava)
            for jd, vozlisce in nodes.items():
                h.add_node(jd, **vozlisce)
            h.name = h_json['name']
            if 'cTP' in h_json.keys():
                h.cTP = h_json['cTP']
                h.dispod, h.nnotp = h_json['dispod'], h_json['nnotp']
                h.UTP, h.S_SN = h_json['UTP'], h_json['S_SN']
            hh.append(h)
    #
    return hh

# -------------------------------------------------------------------------|--

def nxnx_to_json(hh, pth):
    '''
    Zapiše hh = [ nx.MultiDiGraph() ] v JSON.
    
    '''
    hh_json = []
    for h in hh:
        h_json = nx_to_json(h)
        hh_json.append(h_json)
    with open(pth, 'w') as f:
        f.write(json.dumps(hh_json, indent=4))
#
def nx_to_json(h):
    if isinstance(h, nx.MultiDiGraph):
        gtype = 'MultiDiGraph'
    elif isinstance(h, nx.MultiGraph):
        gtype = 'MultiGraph'
    elif isinstance(h, nx.DiGraph):
        gtype = 'DiGraph'
    elif isinstance(h, nx.Graph):
        gtype = 'Graph'
    name = h.name
    nodes = dict()
    for jd, q in h.nodes(data=True):
        node = dict()
        for k, v in q.items():
            if not isinstance(v, QVariant):
                node[k] = v
        nodes[jd] = node
    edges = dict()
    if gtype[:5] == 'Multi':
        for jd1, jd2 in set(h.edges()):
            n = h.number_of_edges(jd1, jd2)
            for multi in range(n):
                q = h.edges[jd1, jd2, multi]
                _ = f'{jd1:s} {jd2:s} {str(multi):s}'
                edge = dict()
                for k, v in q.items():
                    if not isinstance(v, QVariant):
                        edge[k] = v
            edges[_] = edge
    else:
        for jd1, jd2, q in h.edges(data=True):
            _ = f'{jd1:s} {jd2:s}'
            edge = dict()
            for k, v in q.items():
                if not isinstance(v, QVariant):
                    edge[k] = v
            edges[_] = edge
    h_json = {'name': name, 'gtype': gtype, 'nodes': nodes, 'edges': edges}
    if 'cTP' in dir(h):
        h_json['cTP'] = h.cTP
        h_json['dispod'], h_json['nnotp'] = h.dispod, h.nnotp
        h_json['UTP'], h_json['S_SN'] = h.UTP, h.S_SN
    return h_json

# -------------------------------------------------------------------------|--

# def nxnx_to_json(hh):
    # '''
    # Zapiše hh=[nx.DiGraph()] v JSON dopustno obliko.
    
    # '''
    # return [nx_to_json(h) for h in hh]

# def nx_to_json(h):
    # '''
    # Zapiše h=nx.DiGraph() v JSON dopustno obliko.
    
    # '''
    # nodes = {}
    # for jd in h.nodes():
        # nodes[jd] = {k: v for k, v in h.nodes[jd].items()
                # if not isinstance(v, QVariant)}
    # #
    # edges = {}
    # for jd1, jd2 in h.edges():
        # _ = '{} {}'.format(jd1, jd2)
        # edges[_] = {k: v for k, v in h.edges[jd1, jd2].items()
                # if not isinstance(v, QVariant)}
    # #
    # hjson = {'cTP': h.cTP, 'UTP': h.UTP, 'dispod': h.dispod,
            # 'nnotp': h.nnotp, 'S_SN': h.S_SN, 'nodes': nodes,
            # 'edges': edges}
    # #
    # return hjson

# -------------------------------------------------------------------------|--

# def json_to_nxnx(hhjson, sw_int=False):
    # '''
    # Prebere JSON v hh=[nx.DiGraph()].
    
    # '''
    # return [json_to_nx(hjson, sw_int=sw_int) for hjson in hhjson]

# def json_to_nx(hjson, sw_int=False):
    # '''
    # Prebere JSON v h=nx.DiGraph().
    
    # '''
    # h = nx.DiGraph()
    # #
    # h.cTP = hjson['cTP']
    # h.UTP = hjson['UTP']
    # h.dispod = hjson['dispod']
    # h.nnotp = hjson['nnotp']
    # h.S_SN = hjson['S_SN']
    # #
    # for jd, vv in hjson['nodes'].items():
        # ijd = int(jd) if sw_int else jd
        # h.add_node(ijd)
        # for k, v in vv.items():
            # h.nodes[ijd][k] = v
    # #
    # for jd12, vv in hjson['edges'].items():
        # jd1, jd2 = jd12.split(' ')
        # ijd1, ijd2 = (int(jd1), int(jd2)) if sw_int else (jd1, jd2)
        # h.add_edge(ijd1, ijd2)
        # for k, v in vv.items():
            # h.edges[ijd1, ijd2][k] = v
    # #
    # return h

# -------------------------------------------------------------------------|--

#
# ### LOAD LAYER
#

# -------------------------------------------------------------------------|--

def get_present_layers(QPi):
    _ = []
    for k, v in QPi.mapLayers().items():
        if isinstance(v, QgsVectorLayer):
            _.append(v.name())
    return _

def unload_lyr(lyr):
    QPi = QgsProject.instance()
    try:
        lyr_name = lyr.sourceName()
    except:
        return
    lyrs = QPi.mapLayersByName(lyr_name)
    for lyr in lyrs.copy():
        jd = lyr.jd()
        proj.removeMapLayer(jd)

def load_lyr(style_dir, lyr):
    QPi = QgsProject.instance()
    try:
        lyr_name = lyr.sourceName()
    except:
        return
    if not QPi.mapLayersByName(lyr_name):
        QPi.addMapLayer(lyr)
        lyr_name = lyr_name.lower()
        pth = os.path.join(
                style_dir, lyr_name + ' 00 osnovni.qml')
        lyr.loadNamedStyle()

# -------------------------------------------------------------------------|--
# -------------------------------------------------------------------------|--


def hprint(h, h_name, swpr=True):
    '''
    Printanje NN omrežij.
    
    '''
    if swpr:
        for jd, q in h.nodes(data=True):
            print('\n', h_name, jd, q)
        print()
        for jd1, jd2, q in h.edges(data=True):
            print('\n', h_name, jd1, jd2, q)
        print()
        print(nx.info(h))
        print()


def kot(T1, T2):
    '''
    Kot (v stopinjah) daljice od T1 proti T2.
    
          0
       45   315
    90         270
      135   225
         180
    '''
    x1, y1 = T1[0], T1[1]
    x2, y2 = T2[0], T2[1]
    dx, dy = x2 - x1, y2 - y1
    z = math.degrees(math.atan2(dy, dx))
    if z < 0: z += 360
    w = z - 90
    if w < 0: w += 360
    return w

#
# NX to PP
#
# PP to NX
#

import pandapower as pp

# -------------------------------------------------------------------------|--

def nx_to_pp(spe, h, sw_print=False):
    '''
    Transformira NN omrežje iz networkx-oblike v pandapower-obliko.
    
    nx.MultiDiGraph() ==> pp.create_empty_network()
    
         h            ==>           net
    '''
    xspec = 0.08 # specific reactance in ohm_per_km
    print(h.dispod, h.nnotp)
    # default tip kabla, ki ga bomo spreminjali
    basic_line_type = {'c_nf_per_km': 210, 'r_ohm_per_km': 0.642,
            'x_ohm_per_km': xspec, 'max_i_ka': 0.142, 'type': 'cs',
            'q_mm2': 50, 'alpha': 0.00403}
    basic_line_type['alpha'] = 0.
    
    # vsi preseki kablov omrežja
    preseki = set()
    for jd1, jd2, q in h.edges(data=True):
        S = int(q['presek'])
        mat = q['mat']
        preseki.add((S, mat))
    preseki = list(preseki)
    preseki.sort()

    # napetost na TP (se ne uporablja trenutno)
    cTP = h.cTP
    if abs(h.nodes[cTP]['UTP']) > 0.001:
        v230 = h.nodes[cTP]['UTP']

    # ngoi: koliko GOI-jev je v omrežju?
    ngoi = 0
    for jd, q in h.nodes(data=True):
        ngoi += q['nGOI_0']

    # pgoi: koliko kW prispeva vsak GOI v konici TP?
    # to vrednost porabe bomo pripisali vsakemu gospodinjstvu
    pgoi = binomial(spe, ngoi, 0.)
    pgoi /= ngoi

    # create - empty net
    net = pp.create_empty_network(name=h.nnotp)
    if sw_print:
        print('\n# name:\n')
        print(net.name)

    for S, mat in preseki:
        line_data = basic_line_type.copy()
        name = f'KNNNO 4x{str(S)} {mat} LV'
        rspec = rspec_func(S, mat)
        cspec = cspec_func(S, mat)
        imax = imax_func(2, S, mat)
        imax /= 1000
        line_data['r_ohm_per_km'] = rspec
        line_data['max_i_ka'] = imax
        line_data['q_mm2'] = S
        pp.create_std_type(net, line_data, name, element='line')

    # create - buses
    jdTP = h.cTP
    for jd, q in h.nodes(data=True):
        vn_kv = 20. if jd == jdTP else .4
        index = pp.create_bus(net, vn_kv=vn_kv, name=jd, geodata=q['point'])
        q['index'] = index
    if sw_print:
        print('\n# bus:\n')
        print(net.bus)

    # create - external grid
    indexTP = h.nodes[jdTP]['index']
    pp.create_ext_grid(net, bus=indexTP, name='primar TP')
    if sw_print:
        print('\n# ext_grid:\n')
        print(net.ext_grid)

    # create - loads
    # phi = 18 deg <==> tg phi = 1/3 by l. valenčič 7 apr 2022
    cosphi = 0.95
    phi = math.acos(cosphi)
    tangens = math.tan(phi)
    for jd, q in h.nodes(data=True):
        index = q['index']
        tip = q['tip']
        sw_load = False
        pload = 0.
        if 'GOI' in tip or 'GOB' in tip:
            sw_load = True
            pload += pgoi * q['nGOI_0']
        if 'VEL' in tip:
            sw_load = True
            pload += 0.80 * q['Pvel_0']
        if sw_load:
            pload /= 1000
        qload = pload * tangens
        pp.create_load(net, bus=index, p_mw=pload,
                q_mvar=qload, name="Load")
        q['P_0'] = 1000 * pload
    if sw_print:
        print('\n#load:\n')
        print(net.load)

    # create - trafo and lines
    for jd1, jd2, q in h.edges(data=True):
        index1 = h.nodes[jd1]['index']
        index2 = h.nodes[jd2]['index']
        if jd1 == jdTP:
            tr = q['trafo'].split(', ')
            ST =  float(tr[0].split()[1])
            uk =  float(tr[1].split()[1])
            Pcu = float(tr[2].split()[1])
            vezava =    tr[3].split()[1]
            name = f'KNNNO {str(int(ST))}kVA 20/.4'
            sn_mva = ST / 1000
            vk_percent = uk
            vkr_percent = uk / 4.17
            i0_percent = 0.32
            pfe_kW = ST * i0_percent / 100
            vector_group = vezava + 'n'
            if sw_print:
                print()
                print('ST', ST, 'kVA')
                print('uk', uk, '%')
                print('Pcu', Pcu, 'P')
                print('vezava', vezava)
                print('sn_mva', sn_mva)
                print('vk_percent', vk_percent)
                print('vkr_percent', vkr_percent)
                print('pfe_kW', pfe_kW)
                print('vector_group', vector_group)
            tindex = pp.create_transformer_from_parameters(net,
                    hv_bus=index1,
                    lv_bus=index2,
                    name=name,
                    sn_mva=sn_mva,
                    vn_hv_kv=20,
                    vn_lv_kv=0.4,
                    vk_percent=vk_percent,
                    vkr_percent=vkr_percent,
                    pfe_kw=pfe_kW,
                    vector_group=vector_group,
                    i0_percent=i0_percent,
                    tap_side='lv',
                    tap_neutral=0,
                    tap_min=-2,
                    tap_max=2,
                    tap_step_percent=2.5,
                    tap_step_degree=0.0,
                    tap_pos=0,
                    shift_degree=150)
            q['index'] = tindex
        else:
            dolz = q['dolz']
            if dolz < 0.001: dolz = 0.001
            S = int(q['presek'])
            mat = q['mat']
            line_type = f'KNNNO 4x{str(S)} {mat} LV'
            lindex = pp.create_line(net,
                    from_bus=index1,
                    to_bus=index2,
                    length_km=dolz/1000,
                    std_type=line_type)
            q['index'] = lindex
    if sw_print:
        print('\n#trafo:\n')
        print(net.trafo)
        print('\n#line line:\n')
        print(net.line)

    return net

# -------------------------------------------------------------------------|--

def pp_to_nx(net, h, sw_print=False):
    '''
    Transformira NN solution iz pandapower-oblike v networkx-obliko.
    
    pp.create_empty_network() ==> nx.MultiDiGraph()
    
               net            ==>          h
    '''
    if sw_print:
        print('\n# res_bus:\n')
        print(net.res_bus)
        print('\n# res_ext_grid:\n')
        print(net.res_ext_grid)
        print('\n#res_load:\n')
        print(net.res_load)
        print('\n#res_trafo:\n')
        print(net.res_trafo)
        print('\n#res_line:\n')
        print(net.res_line)

    jdTP = h.cTP
    # kumulativna_poraba(h, jdTP)

    for jd, q in h.nodes(data=True):
        q['index'] = int(q['index'])
    for jd1, jd2, q in h.edges(data=True):
        q['index'] = int(q['index'])

    for jd1, jd2, q in h.edges(data=True):
        dolz = q['dolz']
        if jd1 == jdTP:
            tindex = q['index']
            p_hv_mw = float(net.res_trafo.at[tindex, 'p_hv_mw'])
            p_lv_mw = float(net.res_trafo.at[tindex, 'p_lv_mw'])
            p12 = 1000 * (p_hv_mw - p_lv_mw) / 2
            pl_mw = float(net.res_trafo.at[tindex, 'pl_mw'])
            i_lv_ka = float(net.res_trafo.at[tindex, 'i_lv_ka'])
            ib =  1000 * i_lv_ka
            loading_percent = float(net.res_trafo.at[tindex, 'loading_percent'])
            vm_pu = 0.
        else:
            lindex = q['index']
            p_from_mw = float(net.res_line.at[lindex, 'p_from_mw'])
            p_to_mw = float(net.res_line.at[lindex, 'p_to_mw'])
            p12 = 1000 * (p_from_mw - p_to_mw) / 2
            pl_mw = float(net.res_line.at[lindex, 'pl_mw'])
            i_ka = float(net.res_line.at[lindex, 'i_ka'])
            ib =  1000 * i_ka
            loading_percent = float(net.res_line.at[lindex, 'loading_percent'])
            vm_from_pu = float(net.res_line.at[lindex, 'vm_from_pu'])
            vm_to_pu = float(net.res_line.at[lindex, 'vm_to_pu'])
            vm_pu = vm_from_pu - vm_to_pu
        irel = loading_percent / 100
        dp = 1000 * pl_mw
        q['P'] = p12
        q['dP'] = dp
        q['Ib'] = ib
        q['Irel'] = irel
        q['Imax'] = ib / irel
        q['dUrel'] = 100 * vm_pu
    #
    propagiraj_dUrel_b_rek(h, jdTP)
    #
    # for jd, q in h.nodes(data=True):
        # if q['tip'] in ('TP', 'NIL'):
            # p_mw = 0.
        # else:
            # p_mw = float(net.res_load.at[index, 'p_mw'])
        # index = q['index']
        # q['P_0'] = 1000 * p_mw
    #
    for jd, q in h.nodes(data=True):
        q['P'] = q['P_0']
    for jd1, jd2, q in h.edges(data=True):
        P = q['P']
        qq = h.nodes[jd1]
        qq['P'] += P
        




    # for jd1, jd2, q in h.edges(data=True):
        # q2 = h.nodes[jd2]
        # q['nGOI'] = q2['nGOI']
        # q['Pvel'] = q2['Pvel']
        # q['P'] = q2['P']

    # for jd1, jd2, q in h.edges(data=True):
        # dolz = q['dolz']
        # if jd1 == jdTP:
            # presek = 2400.
            # rspec = 35 / presek
        # else:
            # lindex = q['index']
            # max_i_ka = net.line.at[lindex, 'max_i_ka']
            # max_i_ka = float(max_i_ka)
            # r_ohm_per_km = net.line.at[lindex, 'r_ohm_per_km']
            # r_ohm_per_km = float(r_ohm_per_km)
            # std_type = net.line.at[lindex, 'std_type']
            # std_type = str(std_type)            # 'NAYY 4x50 SE'
            # a = std_type.split()                # ['NAYY', '4x50', 'SE']
            # aa = a[1]                           # '4x50'
            # aaa = aa.split('x')                 # ['4', '50']
            # aaaa =  aaa[1]                      # '50'
            # presek = float(aaaa)                # 50.
            # rspec = r_ohm_per_km
            # q['Imax'] = 1000 * max_i_ka
        # q['presek'] = presek
        # q['rspec'] = rspec
        # resis = rspec * dolz / 1000
        # q['resis'] = resis

    # distance_resistance_conductance_TP_b(h)

    # for jd1, jd2, q in h.edges(data=True):
        # dolz = q['dolz']
        # if jd1 == jdTP:
            # tindex = q['index']
            # p_hv_mw = float(net.res_trafo.at[tindex, 'p_hv_mw'])
            # p_lv_mw = float(net.res_trafo.at[tindex, 'p_lv_mw'])
            # pl_mw = float(net.res_trafo.at[tindex, 'pl_mw'])
            # i_lv_ka = float(net.res_trafo.at[tindex, 'i_lv_ka'])
            # loading_percent = float(net.res_trafo.at[tindex, 'loading_percent'])
            # p12 = 1000 * (p_hv_mw - p_lv_mw) / 2
            # dp = 1000 * pl_mw
            # ib =  1000 * i_lv_ka
            # irel = loading_percent / 100
            # imax = ib / irel
            # vm_pu = 0.
        # else:
            # lindex = q['index']
            # p_from_mw = float(net.res_line.at[lindex, 'p_from_mw'])
            # p_to_mw = float(net.res_line.at[lindex, 'p_to_mw'])
            # pl_mw = float(net.res_line.at[lindex, 'pl_mw'])
            # i_ka = float(net.res_line.at[lindex, 'i_ka'])
            # max_i_ka = float(net.line.at[lindex, 'max_i_ka'])
            # vm_from_pu = float(net.res_line.at[lindex, 'vm_from_pu'])
            # vm_to_pu = float(net.res_line.at[lindex, 'vm_to_pu'])
            # vm_pu = vm_from_pu - vm_to_pu
            # loading_percent = float(net.res_line.at[lindex, 'loading_percent'])
            # p12 = 1000 * (p_from_mw - p_to_mw) / 2
            # dp = 1000 * pl_mw
            # imax = q['Imax']
            # ib =  1000 * i_ka
            # irel = 100 * ib / imax
        # q['P'] = p12
        # q['dP'] = dp
        # q['Imax'] = imax
        # q['Ib'] = ib
        # q['Irel'] = irel
        # # du = ib * resis
        # # durel = 100 * du / (400 / sqrt(3))
        # q['dUrel'] = 100 * vm_pu

    # h.nodes[jdTP]['dUrel'] = 0.
    # propagiraj_dUrel_b(h, jdTP)

    # for jd, q in h.nodes(data=True):
        # index = q['index']
        # vm_pu = float(net.res_bus.at[index, 'vm_pu'])
        # # vm_pu = q['dUrel']
        # vn_kv = float(net.bus.at[index, 'vn_kv'])
        # vn_kv = 1000 * vn_kv / math.sqrt(3)
        # q['dUrel'] = vm_pu
        # q['dUelerel'] = 0.
        # q['UTP'] = vn_kv
        # q['U'] = vn_kv * (1 - vm_pu / 100)

def propagiraj_dUrel(h, jd1):
    for jd2 in list(h.successors(jd1)):
        h.nodes[jd2]['dUrel'] = (
                h.nodes[jd1]['dUrel'] +
                h.edges[jd1, jd2]['dUrel'])
        propagiraj_dUrel(h, jd2)

def propagiraj_dUrel_b_rek(h, jd1):
    for jd2 in list(h.successors(jd1)):
        h.nodes[jd2]['dUrel'] = (
                h.nodes[jd1]['dUrel'] +
                h.edges[jd1, jd2, 0]['dUrel'])
        propagiraj_dUrel_b_rek(h, jd2)

# def kumulativna_poraba(h, jd1):
    # h.nodes[jd1]['nGOI'] = h.nodes[jd1]['nGOI_0']
    # h.nodes[jd1]['Pvel'] = h.nodes[jd1]['Pvel_0']
    # h.nodes[jd1]['P'] = h.nodes[jd1]['P_0']
    # for jd2 in list(h.successors(jd1)):
        # kumulativna_poraba(h, jd2)
        # nGOI = h.nodes[jd2]['nGOI']
        # kWfix = h.nodes[jd2]['Pvel']
        # kW = h.nodes[jd2]['P']
        # h.nodes[jd1]['nGOI'] += nGOI
        # h.nodes[jd1]['Pvel'] += kWfix
        # h.nodes[jd1]['P'] += kW


# def dist_resis_TP(h, jd1):
    # for jd2 in list(h.successors(jd1)):
        # h.nodes[jd2]['distTP'] = (
                # h.nodes[jd1]['distTP'] +
                # h.edges[jd1, jd2]['dolz'])
        # h.nodes[jd2]['resisTP'] = (
                # h.nodes[jd1]['resisTP'] +
                # h.edges[jd1, jd2]['resis'])
        # dist_resis_TP(h, jd2)



# def pp_to_qgis(net, h, lyrV, lyrP, sw_geom, sw_print=False):

    # pp_to_nx(net, h, sw_print=sw_print)

    # nx_to_qgis(h, lyrV, lyrP, sw_geom)

#
# ### PICKLE
#

def picklew(var, pth, file_name):
    '''
    Shrani spremenljivko 'var' v datoteko 'file_name.pickle'.
    
    '''
    pth = os.path.join(pth, file_name + '.pickle')
    with open(pth, 'wb') as f:
        pickle.dump(var, f)

# -----------------------------------------------------------------------|--

def pickler(pth, file_name):
    '''
    Vrne spremenljivko iz datoteke 'file_name.pickle'.
    
    '''
    pth = os.path.join(pth, file_name + '.pickle')
    with open(pth, 'rb') as f:
        var = pickle.load(f)
    return var

#
# ### OHRANJANJE SELEKTIRANOSTI
#

# def get_selected():
    # #
    # selected = {'VOZLISCAX': [], 'POVEZAVEX': []}
    # #
    # lyrs = QgsProject.instance().mapLayersByName('VOZLISCAX')
    # if lyrs:
        # lyr = lyrs[0]
        # if lyr.isValid():
            # for ftr in lyr.getSelectedFeatures():
                # jd = ftr['jd']
                # print(jd)
                # selected['VOZLISCAX'].append(jd)
    # #
    # lyrs = QgsProject.instance().mapLayersByName('POVEZAVEX')
    # if lyrs:
        # lyr = lyrs[0]
        # if lyr.isValid():
            # for ftr in lyr.getSelectedFeatures():
                # jd1, jd2 = ftr['jd1'], ftr['jd2']
                # print(ftr['jd1'], ftr['jd2'])
                # selected['POVEZAVEX'].append((jd1, jd2))
    # #
    # return selected

# -------------------------------------------------------------------------|--

# def python_compile(z):
    # '''
    # Kompajlira vse python datoteke.
    
    # :sw_py: 
    # :PREP:  seznam prepovedanih poddirektorijev
    # :x:     
    # :z:     
    # '''
    
    # zz = z
    # jj = z.rfind('.')
    # if 1 <= jj:
        # ime = z[:jj]
        # tip = z[jj:]
        # if tip == '.py':
            # if ime not in PREP:
                # if not sw_py:
                    # zz = ime + '.pyc'
                    # py = os.path.join(pth, z)
                    # pyc = os.path.join(pth, zz)
                    # py_compile.compile(py, pyc, optimize=2)
    # return zz



def do_pluginix_simple_simple(selfplug, selfmiza):
    #
    PLUGINS = ['changex', 'clearx', 'geomx', 'hcx', 'kantrigetx',
              'kantriputx', 'newpovezavax', 'newtpx', 'newvozliscex', 'readx',
              'simx', 'stylex', 'stylex\\style', 'simulate_panda']
    PLUGINS.remove('kantriputx')     # zato da EDP ne morejo zjebati KANTRImiza
    PLUGINS.remove('simulate_panda') # zato ker ne želimo razkrivati PandaPower
    #
    print('    PLUGINIX.zip')
    #
    pth = os.path.join(selfmiza, 'PLUGINIX.zip')
    with ZipFile(pth, 'w', compression=ZIP_DEFLATED) as zf:
        #
        # ku.py
        #
        kupy = os.path.join(selfplug, 'ku.py')
        kupyc = kupy + 'c'
        py_compile.compile(kupy, kupyc, optimize=2)
        head, tail = os.path.split(kupyc)
        zf.write(tail)
        os.remove(tail)
        #
        # vsi preostali plugini: PLUGINS
        #
        for plug in PLUGINS:
            plugplug = os.path.join(selfplug, plug)
            for x in os.listdir(plugplug):
                plugx = os.path.join(plug, x)
                plugplugx = os.path.join(plugplug, x)
                if os.path.isfile(plugplugx):
                    zf.write(plugx)
    #
    PLUGINS.remove('stylex\\style') # zato ker to ni samostojni plugin
    #
    return PLUGINS






#
# ### CLASS COUNTERID
#

class CounterID():
    #
    #
    def __init__(self):
        '''
        Inicializacija.
        
        n = 7                                   # toliko je vseh šifer
        1, 2, 3, 4, 5, 6, 7                     # to so vse šifre
        
        xIDs = 2, 4                             # zbrisane šifre
        IDs = 1, 3, 5, 6, 7                     # uporabljne šifre
        
        xIDs + IDs = 1, 2, 3, 4, 5, 6, 7        # univerzalna množica
        '''
        self.n = 0                              # total number of IDs
        self.xIDs = set()                       # deleted IDs
        self.IDs = set()                        # living IDs
        self.universe_set = set()
    #
    #
    def generate(self):
        '''
        Generira novi ID.
        
        Poglavitna metoda.
        Vrne najmanjšo izmed zbrisanih cifer xIDs.
        Če zbrisanih cifer xIDs ni, vrne naslednjo večjo šifro.
        '''
        if self.xIDs:
            ID = min(self.xIDs)
            self.xIDs.remove(ID)
        else:
            self.n += 1
            ID = self.n
            self.universe_set.add(ID)
        self.IDs.add(ID)
        return ID
    #
    #
    def delete(self, someIDs):
        '''
        Zbriše cel seznam ID-jev.
        
        '''
        self.xIDs.update(set(someIDs))
        self.IDs = self.universe_set.difference(self.xIDs)
        self._updateCounterID_(self.IDs)
    #
    #
    def read(self, newIDs):
        '''
        Prebere seznam novih ID-jev.
        
        '''
        self.IDs.update(set(newIDs))
        self._updateCounterID_(self.IDs)
    #
    #
    def _updateCounterID_(self, IDs):
        '''
        Popravi celotni objekt glede na IDs.
        
        '''
        if IDs:
            self.n = max(IDs)
            self.universe_set = set(range(1, self.n + 1))
            self.xIDs = self.universe_set.difference(IDs)
        else:
            self.__init__()
    #
    #
    def __str__(self):
        '''
        Izpis stanja CounterID objekta.
        
        '''
        IDs = list(self.IDs)
        IDs.sort()
        xIDs = list(self.xIDs)
        xIDs.sort()
        __ = '\nn = {}\nxIDs = {}\nIDs = {}'
        return __.format(self.n, xIDs, IDs)

def delete_all_features(lyr):
    if isinstance(lyr, QgsVectorLayer):
        pr = lyr.dataProvider()
        lyr.startEditing()
        ftrftr = [ftr.id() for ftr in lyr.getFeatures()]
        pr.deleteFeatures(ftrftr)
        lyr.commitChanges(stopEditing=True)

