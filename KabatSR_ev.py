#KabatSR_ev = Kabat SR every rsd = KabatSR5
#count scorel for each rsd and choose max

#import time
#start_time = time.time()

input_mode = 'n'
output_mode = ''
print_mode = 'sir'
commentaries = True
def mode_documentation():
#input_mode:
#'n' - normal, e.g. 1 domain and seq
#'m' - many pairs 'domain and seq'
#'dm' - domain and many seqs
#'f...' - read from file
#example: 'fdm' - read from file; input: domain and many seqs
#output_mode:
#'' - normal,print()
#'f' - write in file
#print_mode:
#'s' - print seq with spaces in boundary-positions
#'i' - print indexes (boundary after each index)
#'r' - print regions (with detailed description(name,%,sure...))
    return


file_name_inp = 'vk_seqs.txt'
file_name_out = 'output_vk_seqs_indexes.txt'

to_print = [] #finally, it will be printed smwhere depending on the output_mode

#some not invariable enough rsds can be deleted in future
L1_start = [[[-19,['LM',3*18]],
             [-18,['RKEDQNPHYGAST',7]],
             [-17,['QE',3*18]],
             [-12,['CVLIMFWPHYGAST',6],['RKE',3]],
             [-11,['CVLIMFWPHYGAST',6]],
             [-10,['CVLIMFWPHYGAST',6],['RKE',3]],
             [-9,['RKEDQNPHYGAST',7]],
             [-8,['P',19],['CVLIMFWHYGAST',6]],
             [-7,['GS',3*18],['G',6*19]],
             [-6,['RKEDQNPHYGAST',7],['DEQ',17]],
             [-5,['RKEDQNPHYGAST',7],['RKQTS',15]],
             [-4,['VLIM',16],['CFWPHYGAST',6],['VA',18]],
             [-3,['RKEDQNPHYGAST',7],['TS',18]],
             [-2,['VLIM',3*16],['ILM',17]],
             [-1,['ST',3*18],['STN',17]]],
            [[22],['C',9*19],['C',12*19]],
            [[1,['RKEDQNPHYGAST',7],['RKST',16]],
            [2,['CVLIMFWPHYGAST',6],['ASG',17]],
            [3,['S',2*19],['T',18]]]]

L1_start_lambda = [[[-18,['LM',3*18]],
             [-17,['RKEDQNPHYGAST',7]],
             [-16,['QE',3*18]],
             [-12,['CVLIMFWPHYGAST',6],['RKE',3]],
             [-11,['CVLIMFWPHYGAST',6]],
             [-10,['CVLIMFWPHYGAST',6],['RKE',3]],
             [-9,['RKEDQNPHYGAST',7]],
             [-8,['P',19],['CVLIMFWHYGAST',6]],
             [-7,['GS',3*18],['G',6*19]],
             [-6,['RKEDQNPHYGAST',7],['DEQ',17]],
             [-5,['RKEDQNPHYGAST',7],['RKQTS',15]],
             [-4,['VLIM',16],['CFWPHYGAST',6],['VA',18]],
             [-3,['RKEDQNPHYGAST',7],['TS',18]],
             [-2,['VLIM',3*16],['ILM',17]],
             [-1,['ST',3*18],['STN',17]]],
            [[21],['C',9*19],['C',12*19]],
            [[1,['RKEDQNPHYGAST',7],['RKST',16]],
            [2,['CVLIMFWPHYGAST',6],['ASG',17]],
            [3,['S',2*19],['T',18]]]]

L1_end = [[[-3,['YNFAW',15]],
           [-2,['CVLIMFWPHYGAST',6],['LVMIA',15]],
           [-1,['RKEDQNPHYGAST',7],['ANH',17]]],
          [[[11,18],[12,17]],['W',9*19],['W',12*19]],
          [[1,['CVLIMFWPHYGAST',6],['Y',2*19],['FLV',16]],
          [2,['RKQ',17],['EDN',14],['QL',18]],
          [3,['Q',9*19],['Q',2*19],['EH',17]],
          [4,['RKEDQNPHYGAST',7],['K',2*19],['R',18]],
          [5,['PS',18],['HYGAT',13],['P',2*19],['SQ',17]],
          [6,['G',19],['RKEDQNPHYAST',7],['G',2*19],['DH',17]],
          [7,['RKEDQNPHYGAST',7],['QKGT',16]],
          [8,['PHYGAST',13],['RKEDQN',7],['SAPT',16]],
          [9,['CVLIMFWPHYGAST',6],['P',2*19],['FY',17]],
          [10,['RKEDQN',14],['KRQT',16]],
          [11,['CVLIMFWPHYGAST',6],['LRGTV',15]],
          [12,['VLIM',3*16],['L',2*19],['WV',17]]]]

L2_start = [[[-11,['Q',9*19],['Q',2*19],['EH',17]],
             [-10,['RKEDQNPHYGAST',7],['K',2*19],['R',18]],
             [-9,['PS',18],['HYGAT',13],['P',2*19],['SQ',17]],
             [-8,['G',19],['RKEDQNPHYAST',7],['G',2*19],['DH',17]],
             [-7,['RKEDQNPHYGAST',7],['QKGT',16]],
             [-6,['PHYGAST',13],['RKEDQN',7],['SAPT',16]],
             [-5,['CVLIMFWPHYGAST',6],['P',2*19],['FY',17]],
             [-4,['RKEDQN',14],['KRQT',16]],
             [-3,['CVLIMFWPHYGAST',6],['LRGTV',15]],
             [-2,['VLIM',3*16],['L',2*19],['WV',17]],
             [-1,['I',19],['CVLMFWPHYGAST',6],['I',2*19],['VM',18]]],
            [[14],['Y',2*19],['KG',17]],
            [[1,['YKW',17]],
             [2,['ATV',17]]]]

L2_end = [[[-3,['LRS',17]],
           [-2,['AF',18]],
           [-1,['STDP',16]]],
          [[8,12],['G',12*19]],
          [[1,['V',2*19],['I',18]],
           [2,['P',6*19]],
           [3,['RKEDQNPHYGAST',7],['DSAV',16]],
           [4,['RK',3*18],['R',6*19]],
           [5,['CVLIMFW',13],['PHYGAST',6],['F',6*19]],
           [6,['ST',3*18],['S',2*19],['T',18]],
           [7,['G',19],['CVLIMFWPHYAST',6],['G',6*19]],
           [8,['ST',3*18]],
           [9,['RKEDQNPHYGAST',7]],
           [10,['S',19],['RKEDQNPHYGAT',7]]]]

L3_start = [[[-10,['VLM',3*17]],
             [-9,['RKEDQNPHYGAST',7]],
             [-8,['RKEDQNPHYGAST',7]],
             [-7,['RKEDQNPHYGAST',7],['ED',18]],
             [-6,['D',9*19],['D',6*19]],
             [-5,['CVLIMFWPHYGASTE',5],['LFEIAV',14]],
             [-4,['GA',3*18],['AG',18]],
             [-3,['CVLIMFWPHYGASTD',5],['TVDI',16]],
             [-2,['Y',9*19],['Y',6*19]],
             [-1,['YF',3*18],['YF',18]]],
            [[31],['C',9*19],['C',12*19]],
            [[1,['RKEDQNPHYGAST',7],['QFLAS',15]],
             [2,['RKEDQNPHYGAST',7],['QHL',17]],
             [3,['YGSWH',15]]]]

L3_end = [[[-3,['P',19],['LH',17]],
           [-2,['YLPRWF',14]],
           [-1,['CVLIMFWPHYGAST',6],['TV',18]]],
          [[[8,16],[10]],['FW',3*18],['F',12*19]],
          [[1,['G',9*19],['G',6*19]],
           [2,['RKEDQNPHYGAST',7],['GQAST',15]],
           [3,['G',9*19],['G',6*19]],
           [4,['T',9*19],['T',6*19]],
           [5,['RKEDQNPHYGAST',7],['K',6*19],['R',18]],
           [6,['VL',3*18],['L',2*19],['V',18]],
           [7,['RKEDQNPHYGAST',7],['E',19],['TD',17]],
           [8,['VLI',3*17]]]]

H1_start = [[[-26,['LM',3*18]],
             [-25,['RKEDQNPHYGAST',7]],
             [-24,['QE',3*18]],
             [-20,['CVLIMFWPHYGASTRKE',3]],
             [-19,['CVLIMFWPHYGAST',6]],
             [-18,['CVLIMFWPHYGASTRKE',3]],
             [-17,['RKEDQNPHYGAST',7]],
             [-16,['P',19],['CVLIMFWHYGAST',6]],
             [-15,['GS',3*18],['G',2*19],['S',18]],
             [-14,['RKEDQNPHYGAST',7],['GAQ',17]],
             [-13,['RKEDQNPHYGAST',7],['S',2*19],['T',18]],
             [-12,['VLIM',16],['CFWPHYGAST',6],['LVM',17]],
             [-11,['RKEDQNPHYGAST',7],['KRS',17]],
             [-10,['VLIM',3*16],['LIMV',16]],
             [-9,['ST',3*18],['S',2*19],['T',18]],
             [-8,['C',9*19],['C',12*19]],
             [-7,['RKEDQNPHYGAST',7],['KATS',16]],
             [-6,['CVLIMFWPHYGAST',6],['AVT',17]],
             [-5,['S',2*19],['T',18]]],
            [[29]],
            []]

H1_end = [[[-3,['YWGA',16]],
           [-2,['MIWV',16]],
           [-1,['HNSG',16]]],
          [[[6,8],[6]],['W',9*19],['W',12*19]],
          [[1,['CVLIMFWPHYGAST',6],['V',2*19],['IF',17]],
           [2,['RKQ',17],['EDN',14],['RK',18]],
          [3,['Q',9*19],['QK',18]],
          [4,['RKEDQNPHYGAST',7],['ARPFST',14]],
          [5,['PS',18],['HYGAT',13],['P',6*19],['H',18]],
          [6,['G',2*19],['RKEDQNPHYAST',7],['G',19],['E',18]],
          [7,['RKEDQNPHYGAST',7],['KQNH',16]],
          [8,['PHYGAST',13],['RKEDQN',7],['GRKEA',15]],
          [9,['CVLIMFWPHYGAST',6],['L',6*19],['R',18]],
          [10,['RKEDQN',14],['E',6*19],['K',18]],
          [11,['CVLIMFWPHYGAST',6],['W',2*19],['YG',17]],
          [12,['VLIM',3*16],['IVML',16]]]]

H2_start = [[[-10,['Q',9*19],['QK',18]],
             [-9,['RKEDQNHYGAT',7],['ARPFST',14]],
             [-8,['PS',18],['HYGAT',13],['P',6*19],['H',18]],
             [-7,['G',19],['RKEDQNPHYAST',7],['G',2*19],['E',18]],
             [-6,['RKEDQNPHYGAST',7],['KQNH',16]],
             [-5,['PHYGAST',13],['RKEDQN',7],['GRKEA',15]],
             [-4,['CVLIMFWPHYGAST',6],['L',6*19],['R',18]],
             [-3,['RKEDQN',14],['E',6*19],['K',18]],
             [-2,['CVLIMFWPHYGAST',6],['W',2*19],['YG',17]],
             [-1,['VLIM',3*16],['IVML',16]]],
            [[13],['GAS',17],['CVLIMFWPHYT',6],['GA',18]],
            [[1,['YW',18]],
             [2,['I',2*19],['V',18]],
             [3,['SNYD',16]]]]

H2_end = [[[-10,['SNYDT',15]],
           [-9,['TIPSKA',14]],
           [-8,['YN',18]],
           [-7,['Y',2*19],['F',18]],
           [-6,['NASVG',15]],
           [-5,['DPEQA',15]],
           [-4,['SKADT',15]],
           [-3,['FVL',17]],
           [-2,['K',2*19],['QR',17]],
           [-1,['RKEDQNPHYGAST',7],['GSD',17]]],
          [[[17,20],[]],['RK',3*18],['RK',18]],
          [[1,['CVLIMFW',13],['PHYGAST',6]],
           [2,['ST',3*18]],
           [3,['MI',18],['CVLFWPHYGAST',6]],
           [4,['ST',3*18]],
           [5,['RKEDQNPHYGAST',7]],
           [6,['D',19],['RKEQNPHYGAST',7]],
           [7,['RKEDQNPHYGAST',7]],
           [8,['RKEDQNPHYGAST',7]],
           [11,['RKEDQNPHYGAST',7]],
           [12,['CVLIMFWPHYGAST',6]],
           [13,['YF',18],['PHGAST',12]],
           [14,['LIMF',3*16]],
           [15,['RKEDQNPHYGAST',7]],
           [16,['LIM',3*17]]]]

H3_start = [[[-12,['VLM',3*17]],
             [-11,['RKEDQNPHYGAST',7]],
             [-10,['RKEDQNPHYGAST',7]],
             [-9,['RKEDQNPHYGAST',7],['E',2*19],['DA',17]],
             [-8,['D',9*19],['D',6*19]],
             [-7,['CVLIMFWPHYGAST',6],['TS',18]],
             [-6,['GA',3*18],['A',6*19],['G',18]],
             [-5,['CVLIMFWPHYGAST',6],['VTIML',15]],
             [-4,['Y',9*19],['Y',6*19]],
             [-3,['YF',3*18],['Y',2*19],['F',18]],
            [-2,['C',9*19],['C',12*19]],
            [-1,['RKEDQNPHYGAST',7],['ATV',17]]],
            [[[28,31],[31]],['RKEDQNPHYGAST',7],['RASN',16]],
            [[1,['GW',18]]]]

H3_end = [[[-3,['FMGLY',15]],
           [-2,['DAGV',16]],
           [-1,['CVLIMFWPHYGAST',6],['YV',18]]],
          [[[5,20],[i for i in range(5,16)]],['FW',3*18],['W',12*19]],
          [[1,['G',9*19],['G',6*19]],
           [2,['RKEDQNPHYGAST',7],['QAEKHP',14]],
           [3,['G',9*19],['G',6*19]],
           [4,['T',9*19],['T',6*19]],
           [5,['RKEDQNPHYGAST',7],['TLSQ',16]],
           [6,['VL',3*18],['V',2*19],['L',18]],
           [7,['RKEDQNPHYGAST',7],['T',6*19]],
           [8,['VLI',3*17]]]]

data_base = {'L1_start': L1_start,'L1_end': L1_end,
             'L2_start': L2_start,'L2_end': L2_end,
             'L3_start': L3_start,'L3_end': L3_end,
             'H1_start': H1_start,'H1_end': H1_end,
             'H2_start': H2_start,'H2_end': H2_end,
             'H3_start': H3_start,'H3_end': H3_end,
             'L1_start_lambda': L1_start_lambda}

def comment(com):
    if(commentaries):
        to_print.append(com)
def commentr(com):
    if(commentaries or 'r' in print_mode):
        to_print.append(com)

def sum_r(index,res):
    cnt = 0
    for i in range(len(res)):
        cnt += res[i][index]
    return cnt
    
def name(index): #checklist index
    if(index % 2 == 0):
        return('FR{}'.format(index//2+1))
    return('CDR{}'.format(index//2+1))  

def convert_res(res,seq,checklist):
    #out[0] = [tot_sc,tot_msc] (total scorels)
    out = [[sum_r(1,res),sum_r(2,res)]]
    last = 0 #last True in checklist +1
    cur = 0 #current to_print.append-position
    for i in range(len(checklist)):
        if(checklist[i][0]):
            reg = []
            #construct region's name
            if(last == i):
                reg.append(name(i))
            elif(last == 0):
                reg.append('...' + name(i))
            else:
                reg.append(name(last) + '...' + name(i))
            #find region in seq
            if(i % 2 == 0):
                print_bound = res[checklist[i][1]][0]+1
            else:
                print_bound = res[checklist[i][1]][0]
            reg.append(seq[cur:print_bound])
            cur = print_bound
            #addinfo(start,end,%)
            #reg[i] = [name,seq,sure,start,end]
            #start,end = [scorel,max scorel,%] // sure = [scorel,max,%]
            if(last == 0):
                pos_end = res[checklist[i][1]]
                reg.append([pos_end[1],pos_end[2],pos_end[3]])
                reg.append([])
                reg.append([pos_end[1],pos_end[2],pos_end[3]])
                last = i+1
                out.append(reg)
                continue
            pos_start = res[checklist[last-1][1]]
            pos_end = res[checklist[i][1]]
            reg.append([pos_start[1] + pos_end[1],pos_start[2] + pos_end[2]]) #sure
            reg[2].append(round(reg[2][0]/reg[2][1]*100))
            reg.append([pos_start[1],pos_start[2],pos_start[3]]) #start   
            reg.append([pos_end[1],pos_end[2],pos_end[3]]) #end
            last = i+1
            out.append(reg)    
    #add remaining
    reg = []
    if(last == len(checklist)):
        reg.append('FR4')
    else:
        reg.append(name(last) + '...')
    reg.append(seq[cur:])
    pos_start = res[checklist[last-1][1]]
    reg.append([pos_start[1],pos_start[2],pos_start[3]])
    reg.append([pos_start[1],pos_start[2],pos_start[3]])
    reg.append([])
    out.append(reg)
    return out

def printR_seq(out):
    to_print.append('RESULT:')
    for i in range(1,len(out)):
        to_print[len(to_print)-1] += (' ' + out[i][1])
        
def printR_inds(res):
    to_print.append('RESULT: ')
    inds = []
    for i in range(len(res)):
        if(i % 2 == 0):
            inds.append(res[i][0])
        else:
            inds.append(res[i][0]-1)
    to_print[len(to_print)-1] += str(inds)
    if(commentaries):
        to_print.append('Description: Boundary is located after each index')
    
def printR_regs(out):
    to_print.append('RESULT: ')
    to_print[len(to_print)-1] += ('sure ' + str(out[0][2]) + '% (' + str(out[0][0]) + '/' + str(out[0][1]) + ')')
    out[1][1] = '...' + out[1][1]
    out[len(out)-1][1] = out[len(out)-1][1] + '...'
    for i in range(1,len(out)):
        to_print.append('\n' + out[i][0] + ': ' + out[i][1])
        if(len(out[i][2]) == 4):
            to_print.append('sure: ' + '100' + '% ('+ str(out[i][2][2]) + '% ' + str(out[i][2][0]) + '/' + str(out[i][2][1]) + out[i][2][3] + ')')
        else:
            to_print.append('sure: ' + str(out[i][2][2]) + '% (' + str(out[i][2][0]) + '/' + str(out[i][2][1]) + ')')
        if(not len(out[i][3]) == 0):
            to_print.append('start - ' + str(out[i][3][2]) + '% (' + str(out[i][3][0]) + '/' + str(out[i][3][1]) + ')')
        if(not len(out[i][4]) == 0):
            to_print.append('end - ' + str(out[i][4][2]) + '% (' + str(out[i][4][0]) + '/' + str(out[i][4][1]) + ')')
            
def find_canonical(cdr,reg_name):
    #db - data base of canonical structures // cdr - CDR
    #human,mouse,camel&lamma canonical structures
    L1_kappa = [3,['-Human&Mouse','RASQDISNYLA','RSSQSLVHSNGNTYLE',
                 'KSSQSLLNSRTRKNYLA','RASESVDSYGNSFMN',
                 'RASQSVSSNYLA'],
                ['-Mouse','RASQDISNYLN','SASSSVSYMH',
                 'RASSSVSSSYLH','SASSSVSYMY','RASKSVSTSGYNYMH']]
    L1_lambda = [3,['-Human','SASSSVSYMH','SGSSSNIGNNYVS',
                  'SGNNLGS-SVH','TRSSGNIASNYVQ'],
                 ['-Human&Mouse','TLSSQHSTYTIE'],
                 ['-Mouse','SASSSVSYMH']]
    L2_kappa = [2,['-Human&Mouse','-ASNLAS','AASNLDS','SASYRYS'],
                ['-Mouse','EGNTLRP','GTNNRVP']]
    L2_lambda = [3,['-Mouse','EGNTLRP','GTNNRVP','LKKDGSHSTGD']]
    L3_kappa = [3,['-Human','QQYNNWPPRYT'],
                ['-Human&Mouse','QQGSS-PLT','ALW-SNHWV',
                 'LQYYNLRT','QQSTH-PPT','QHFWSTPRT',
                 'QQYNSYS','QQYYIYPYT'],
                ['-Mouse','QQFWRTPT','QQWNYPFT',
                 'LYSREFPPWT','QQWTYPLIT','SQSTHVPPLT']]
    L3_lambda = [4,['-Human','AAWDSSLDAVV','QSYDSS-SVV','ATWDSGLSADWV'],
                 ['-Human&Mouse','ALW-SNHWV','AAWDDSRGGPDWV'],
                 ['-Mouse']]
    H1 = [2,['-Human','MYGFN'],
          ['-Human&Mouse','DYYMH','TSGMGVG','DYYIS',
           'TYAMN','GYYWS','INYMG'],
          ['-Mouse','SGYAWN','SGYWN','TYDMG',
           'SYLFQ','YGMN'],
          ['-Camel','NYCMG','PYCMG','VG'],
          ['-Camel&Lamma','TYDMG'],
          ['-Lamma','GHGHYGMG']]
    H2 = [3,['-Human','TILGGSTY'],
          ['-Human&Mouse','-IYPGNG-T-','YIWYSGSTY','-ISSGGGNTY',
           'EILPGSGSTN','RIDPNGGGTK','TTLSGGGFTF','GIDPHNGGGA',
           'GIDPHNGGPV'],
          ['-Mouse','EIRNKANNYTTE','TISSGGGYTN','SIYNGFRIH'],
          ['-Mouse&Camel','AISGGGTYIH','YIRYGGGTY'],
          ['Lamma','TIGRNLVGPSDFYTR']]
    H3 = ['-YFDY','YDFDY','GYFDY','WDGDY','--RDY',
          '-SFAY','RGFDY','EPFDY']
    
    canonicals = {'kappa1': L1_kappa, 'lambda1': L1_lambda,
                  'kappa2': L2_kappa, 'lambda2': L2_lambda,
                  'kappa3': L3_kappa, 'lambda3': L3_lambda,
                  'H1': H1, 'H2': H2, 'H3': H3}
    
    db = canonicals[reg_name]
    #H3-cs are in different format
    if(reg_name == 'H3'):
        for i in range(len(db)):
            dif = 0
            if(not(db[i][0] == cdr[0] or db[i][0] == '-')):
                return [False]
            to_compare = cdr[len(cdr)-4:]
            for j in range(1,len(db[i])):
                if(not(db[i][j] == to_compare[j-1] or db[i][j] == '-')):
                    return [False]
        return [True,'']
                
    #for other regions
    for i in range(1,len(db)):
        for j in range(1,len(db[i])):
            dif = 0
            diap = len(cdr)
            if(len(db[i][j]) < len(cdr)):
                diap = len(db[i][j])
            for k in range(diap):
                if(not(cdr[k] == db[i][j][k] or db[i][j][k] == '-')):
                    dif+=1
            if(dif <= db[0]):
                return [True,db[i][0]]
    return [False]

def canonical_structures(out,domain):
    #define CDRs         
    for i in range(1,len(out)):
        if(out[i][0] == 'CDR1'):
            tmp = find_canonical(out[i][1],domain + '1')
            if(tmp[0]):
                out[i][2].append(' + cs' + tmp[1])
        elif(out[i][0] == 'CDR2'):
            tmp = find_canonical(out[i][1],domain + '2')
            if(tmp[0]):
                out[i][2].append(' + cs' + tmp[1])            
        elif(out[i][0] == 'CDR3'):
            tmp = find_canonical(out[i][1],domain + '3')
            if(tmp[0]):
                out[i][2].append(' + cs' + tmp[1])            
    #if CDR = canonical structure (cs) => 100% and refresh total sure
    add = 0
    for i in range(1,len(out)):
        if(len(out[i][2]) == 4):
            add += (out[i][2][1]-out[i][2][0])
    out[0][0] += add
    out[0].append(round(out[0][0]/out[0][1]*100))

def output(res,seq,checklist,domain):
    to_print.append('')
    if(len(res) == 0):
        to_print.append('RESULT: Undefined')
        return
    out = convert_res(res,seq,checklist)
    if('s' in print_mode):
        printR_seq(out)
    if('i' in print_mode):
        printR_inds(res)
    if('r' in print_mode):
        canonical_structures(out,domain) #additional points for canonical structures
        printR_regs(out)

def scorel_bugcheck(bugcheck,max_scorel,index,data):
    #to_print.append(data + ' - ' + str(bugcheck))
    to_print.append('BugCheck for {} '.format(data))
    to_print[len(to_print)-1] += ('[index: ' + str(index) + ' // score: '+ str(max_scorel) + ']: ')
    for i in range(len(bugcheck)):
        if(abs(max_scorel-bugcheck[i][1]) <= 60 and bugcheck[i][0] != index):
            #index_c,scorel_c,difference
            to_print[len(to_print)-1] += ('[' + str(bugcheck[i][0]) + ' // ' + str(bugcheck[i][1]) + ' // '+ str(max_scorel-bugcheck[i][1]) + '] ')
    to_print[len(to_print)-1] += ('BugCheck done')

def search_and_scorel(seq,data,lastRes):
    bugcheck = [] #BC scorel
    max_scorel = 0
    index = 0
    for i in range(lastRes,len(seq)):
        tmp = scorel(i,data,seq,lastRes)
        bugcheck.append([i,tmp]) #BC scorel
        if(tmp > max_scorel):
            max_scorel = tmp
            index = i
    if(commentaries):
        scorel_bugcheck(bugcheck,max_scorel,index,data) #BC scorel
    return [index,max_scorel]

def list_check(x):
    try:
        x[0] = x[0]
        return True
    except TypeError:
        return False

def scorel(index,data,seq,lastRes):
    pat = data_base[data] #receiving pattern
    pat_bef = pat[0] #pattern before x
    pat_x = pat[1] #x = rsd pos that will be placed into res
    pat_aft = pat[2] #pattern after x
    score = 0
    #stpd scoring, SUPER SENSIBLE to any shift(insertions & deletions)
    if(len(pat_x) != 0):
        for i in range(1,len(pat_x)):
            for k in range(len(pat_x[i][0])):
                if(seq[index] == pat_x[i][0][k]):
                    score += pat_x[i][1]
                    #to_print.append('equals: '+str(pat_x[i]))
    if(len(pat_bef) != 0):
        for i in range(0,len(pat_bef)):
            for j in range(1,len(pat_bef[i])):
                for k in range(len(pat_bef[i][j][0])):
                    if(index+pat_bef[i][0]<=0):
                        break                
                    if(pat_bef[i][j][0][k] == seq[index+pat_bef[i][0]]):
                        score += pat_bef[i][j][1]
                        #to_print.append('equals: ' + str(pat_bef[i][j]))
                        break
    if(len(pat_aft) != 0):
        for i in range(0,len(pat_aft)):
            for j in range(1,len(pat_aft[i])):
                for k in range(len(pat_aft[i][j][0])):
                    if(index+pat_aft[i][0]>=len(seq)):
                        break
                    if(pat_aft[i][j][0][k] == seq[index+pat_aft[i][0]]):
                        score += pat_aft[i][j][1]
                        #to_print.append('equals: ' + str(pat_aft[i][j]))
                        break
    #length scoring
    scoreL = 0
    ind_dist = index - lastRes
    data_dist = pat_x[0]
    if(len(pat_x[0]) == 1): #only 1 possible dist
        if(ind_dist == data_dist[0]):
            scoreL += 6*40
            #to_print.append(data + ' - ' + str(240) + ' - ' + seq[index])
        elif(abs(ind_dist-data_dist[0]) == 1):
            scoreL += 5*40
        elif(abs(ind_dist-data_dist[0]) == 2):
            scoreL += 3*40
    elif(not list_check(data_dist[0])): #only 2 possible dists
        if(ind_dist == data_dist[0] or ind_dist == data_dist[1]):
            scoreL += 6*40
            #to_print.append(data + ' - ' + str(240) + ' - ' + seq[index])
        elif(abs(ind_dist-data_dist[0]) == 1 or abs(ind_dist-data_dist[1]) == 1):
            scoreL += 5*40
        #maybe it's excess
        elif(abs(ind_dist-data_dist[0]) == 2 or abs(ind_dist-data_dist[1]) == 2):
            scoreL += 3*40
    else: #neiborhood with the most common dists
        flag = True
        for d in data_dist[1]:
            if(ind_dist == d):
                scoreL += 6*40
                #to_print.append(data + ' - ' + str(240) + ' - ' + seq[index])
                flag = False #kostyl!
        if(flag):
            if(ind_dist >= data_dist[0][0] and ind_dist <= data_dist[0][1]):
                scoreL += 5*40
            elif(data_dist[0][0]-ind_dist <= 2 or ind_dist-data_dist[0][1] <=2):
                scoreL += 40
    return (score + scoreL)

def domain_improv(domain,script):
    if(domain == 'lambda'):
        script[0] = 'L1_start_lambda'

def KabatSR5_L(seq,domain):
    comment('L-{}-annotation'.format(domain))
    comment('Commentaries:')
    res = [[0]] #for saving result
    maxScorels = [1051+240,1140+240,729+240,1054+240,1304+240,1506+240] #+lengths
    script = ['L1_start','L1_end','L2_start','L2_end','L3_start','L3_end']
    checklist = [[False] for i in range(6)] #checklist[i][0] == True if pos[i] in res
    domain_improv(domain,script)
    for i in range(0,len(script)):
        #res[i] = [index,scorel,maxScorel,%]
        pos = search_and_scorel(seq,script[i],res[len(res)-1][0])
        pos.append(maxScorels[i])
        pos.append(round(pos[1]/pos[2]*100))
        if(pos[3] >= 65):
            res.append(pos)
            checklist[i] = [True,len(res)-2] #-2 instead of -1 because 0 will be deleted
        else:
            comment('{0} undefined (max {1}%)'.format(script[i],pos[3]))
    res.pop(0)
    output(res,seq,checklist,domain)
    #to_print.append('\nSEE:')
    #scorel(res[3][0],'L2_end',seq,res[2][0])
    
def KabatSR5_H(seq):
    comment('H-annotation')
    comment('Commentaries:')
    res = [[0]] #for saving result
    maxScorels = [1010+240,1332+240,913+240,597+200,1449+240,1500+240] #+lengths
    script = ['H1_start','H1_end','H2_start','H2_end','H3_start','H3_end']
    checklist = [[False] for i in range(6)] #checklist[i][0] == True if pos[i] in res
    for i in range(0,len(script)):
        #res[i] = [index,scorel,maxScorel,%,region's name(pos is nearly its end)]
        pos = search_and_scorel(seq,script[i],res[len(res)-1][0])
        pos.append(maxScorels[i])
        pos.append(round(pos[1]/pos[2]*100))
        if(pos[3] >= 65):
            res.append(pos)
            checklist[i] = [True,len(res)-2] #-2 instead of -1 because 0 will be deleted
        else:
            comment('{0} undefined (max {1}%)'.format(script[i],pos[3]))
    res.pop(0)
    output(res,seq,checklist,'H')
    #to_print.append('\nSEE:')
    #scorel(res[3][0],'L2_end',seq,res[2][0])    

def KabatSR5(seq,domain):
    if('H' in domain):
        KabatSR5_H(seq)
    elif('k' in domain or 'K' in domain):
        KabatSR5_L(seq,'kappa')
    elif('l' in domain): 
        KabatSR5_L(seq,'lambda')
    elif('L' in domain):
        comment('\nL-annotation')
        comment('Notice: if only lambda-domain was meant, restart the programm using \'VL-lambda\'(\'Vl\') domain-type')
        KabatSR5_L(seq,'kappa')
        KabatSR5_L(seq,'lambda')
    else:
        to_print.append('Unknown_domain-error: {}'.format(domain))
        to_print.append('Try: VH, VL-lambda(Vl), VL-kappa(Vk)')

def readF(name):
    with open(name) as f:
        return f.read()
def main():
    if(input_mode[0] == 'f'):
        input_data = readF(file_name_inp).split()

        if(input_mode[1] == 'n'):
            print('File Read: domain and seq')
            domain,seq = input_data.split()
            KabatSR5(seq,domain)
            
        elif(input_mode[1] == 'm'):
            print('Multiple File Read: (domain seq)-pairs')
            for i in range(0,len(input_data),2):
                commentr('\n\nSequence: {}'.format(i//2 + 1))
                KabatSR5(input_data[i+1],input_data[i])
                
        elif(input_mode[1] == 'd'):
            print('Multiple File Read: domain and seq-s')
            domain = input_data[0]
            for i in range(1,len(input_data)):
                commentr('\n\nSequence: {}'.format(i))
                KabatSR5(input_data[i],domain)            
            
    elif(input_mode[0] == 'n'):
        input_data = input('Input domain and seq: ')
        domain,seq = input_data.split()
        KabatSR5(seq,domain)  
        
    elif(input_mode[0] == 'm'):
        input_data = input('Multiple-Input\n' + 'Input (domain seq)-pairs:\n').split()
        for i in range(0,len(input_data),2):
            commentr('\n\nSequence: {}'.format(i//2 + 1))
            KabatSR5(input_data[i+1],input_data[i])
            
    elif(input_mode[0] == 'd'):
        input_data = input('Multiple-Input\n' + 'Input domain and seq-s:\n').split()
        domain = input_data[0]
        for i in range(1,len(input_data)):
            commentr('\n\nSequence: {}'.format(i))
            KabatSR5(input_data[i],domain)        
    else:
        print('Input_mode-error: {}'.format(input_mode))
        print('Try again')
        
    #print output
    if(output_mode == 'f'):
        file = open(file_name_out,"w")
        file.write('\n'.join(to_print))
        file.close()
        print('Completed')
    else:
        print('\n'.join(to_print))
    
main()
#print("{} time".format(time.time() - start_time))

#don't worry about memory error,
#because in this version it will happen only after 2 hours:)

#add a lot of stuff
#check North's work for more rsds on each position

#upgrade speeed