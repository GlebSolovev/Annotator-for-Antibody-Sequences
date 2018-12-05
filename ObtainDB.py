input_file = "IMGT Sequences.txt"
input_file_GeneList = "IMGT GeneList.txt"
output_file = "ObDB output.txt"
output_file_GeneList = "ObDB outputGL.txt"
output_file_DB = "ObDB outputDB.txt"
output_file_RDB = "ObDB outputRDB.txt"
data = []
geneList = []
database = []
spDB = {}
spRDB = {}

def printD():
    for i in range(len(data)):
        data[i][3] = '*'.join(data[i][3])
        data[i] = ' '.join(data[i])
    file = open(output_file,"w")
    file.write('\n'.join(data))
    file.close()
    print('Completed')
    
def printGL():
    for i in range(len(geneList)):
        geneList[i] = ' '.join(geneList[i])
    file = open(output_file_GeneList,"w")
    file.write('\n'.join(geneList))
    file.close()
    print('Completed')     

def printDB():
    for i in range(len(database)):
        database[i] = ' '.join(database[i])
    file = open(output_file_DB,"w")
    file.write('\n'.join(database))
    file.close()
    print('Completed')
    
def joinN(arr,space):
    for i in range(len(arr)):
        if(not arr[i] is str):
            arr[i] = str(arr[i])
    return space.join(arr)

def printRDB():
    to_print = []
    for sp in spRDB:
        to_print.append(sp)
        for ch in spRDB[sp]:
            if(len(spRDB[sp][ch]) == 0):
                continue
            to_print.append(ch)
            for i in range(len(spRDB[sp][ch])):
                spRDB[sp][ch][i] = joinN(spRDB[sp][ch][i],' ')
            to_print.append(';'.join(spRDB[sp][ch]))
    file = open(output_file_RDB,"w")
    file.write('\n'.join(to_print))
    file.close()
    print('Completed')    

def readF(name):
    with open(name) as f:
        return f.read()

def check(about):
    if(not about[3] == 'F'):
        return False
    if(not (about[4] == 'V-REGION' or about[4] == 'J-REGION' or about[4] == 'D-REGION')):
        return False
    if(not about[10] == ' '):
        return False
    if(about[13].startswith('partial')):
        return False
    if(about[14] == 'rev-compl'):
        return False
    seqList = list(about[15])
    for i in range(len(seqList)):
        if(seqList[i] == '*'):
            return False
    return True

def checkGL(about):
    if(not about[2] == 'F'):
        return False
    if(not ('immunoglobulin' in about[3] or 'Immunoglobulin' in about[3])):
        return False
    if('constant' in about[3]):
        return False
    if(not ('heavy' in about[3] or 'kappa' in about[3] or 'lambda' in about[3])):
        return False
    if(not ('variable' in about[3] or 'joining' in about[3] or 'diversity' in about[3])):
        return False
    return True

def add(about):
    about[15] = ''.join(about[15].split('\n'))
    about[4] = about[4][0:1]
    about[1] = about[1].split('*')
    data.append([about[2],about[4],about[15],about[1],about[0]])
    #[species,region,seq,[gene,allele],ref seq]
    
def addGL(about):
    #species;gene name;func;def; alleles num; chromosome; chrom loc; ref seq for *01;...;
    region = ''
    chain = ''
    if('heavy' in about[3]):
        chain = 'H'
    elif('kappa' in about[3]):
        chain = 'k'
    elif('lambda' in about[3]):
        chain = 'l'
    """else:
        print('UNKNOWN chain')
        print(about[3])"""
    if('variable' in about[3]):
        region = 'V'
    elif('diversity' in about[3]):
        region = 'D'
    elif('joining' in about[3]):
        region = 'J'
    """else:
        print('UNKNOWN region')
        print(about[3])"""
    splitted = about[3].split(' ')
    regDef = splitted[len(splitted)-1]
    geneList.append([about[1],about[0],chain,region,regDef,about[7]]) 
    #[gene name,species,chain(H,k,l),region(V,D,J),reg's def,ref seq]
    
def deleteFirstEquals():
    to_delete = []
    for i in range(len(database)-1):
        for j in range(i+1,len(database)):
            if(database[i][4] == database[j][4]):
                to_delete.append(j)
            break
    for k in range(len(to_delete)):
        database.pop(to_delete[k])
        return True
    return False  
    
def main():
    """parse IMGT seqs"""
    input_data = readF(input_file).split('>')
    #print(input_data)
    for i in range(1,len(input_data)):
        #ref seq|gene & allele name|species|func|regions name|
        #|start and end positions in accession number|num of nucls|...|...|num of corrected nucls/'not corrected'|
        #|num of AA| AAnum + gapNum = total|partial if it is|rev compl if it is|
        about = input_data[i].split('|')
        if(check(about)):
            add(about)
    #printD()
    """parse IMGT GeneList"""
    input_geneList = readF(input_file_GeneList).split('\n')
    for i in range(1,len(input_geneList)):
        #species;gene name;func;def; alleles num; chromosome; chrom loc; ref seq for *01;...;
        about = input_geneList[i].split(';')
        if(checkGL(about)):
            addGL(about)
    #printGL()
    
    """obtain prerecomb DB"""
    for i in range(len(data)):
        #[species+,region,seq,[gene name,allele],ref seq]
        for j in range(len(geneList)):
            #[gene name,species,chain(H,k,l),region(V,D,J),reg's def,ref seq]
            if(data[i][3][0] == geneList[j][0] and data[i][1] == geneList[j][3] and data[i][0].startswith(geneList[j][1])):
                if(data[i][4] == geneList[j][5]):
                    addInfo = data[i][3][0]+'*'+data[i][3][1]+'|'+data[i][4]+'|'+data[i][0]
                    #gene*allele|ref seq|species+
                    database.append([geneList[j][1],geneList[j][2],geneList[j][3],geneList[j][4],data[i][2],addInfo])
                    #[species,chain,region,reg's def,seq,addInfo]
                    break
                else:
                    """not 01 alleles have strange ref seq"""
                    addInfo = data[i][3][0]+'*'+data[i][3][1]+'|'+data[i][4]+'|'+data[i][0]
                    #gene*allele|ref seq|species+
                    database.append([geneList[j][1],geneList[j][2],geneList[j][3],'later',data[i][2],addInfo])
                    #[species,chain,region,reg's def CAN be known => LATER,seq,addInfo]
                    break                    
            """else: there is no such seqs in GeneList => impossible to know the region type("""
    print('database length = ',end='')
    print(len(database))
    """1378 out of 2896 - really sad("""
    #printDB() """not 01 alleles have strange ref seq"""
    
    """clean from dublicates"""
    flag = True
    while(flag):
        flag = deleteFirstEquals()
    print('cleaned database length = ',end='')
    print(len(database))
    #printDB()
                
    """prepare to recomb = clustering"""
    for i in range(len(database)):
        #print(i)
        if(not database[i][0] in spDB):
            spDB[database[i][0]] = {'H':{'V':[],'D':[],'J':[]},'k':{'V':[],'J':[]},'l':{'V':[],'J':[]}}
        spDB[database[i][0]][database[i][1]][database[i][2]].append(i);
    #print(spDB)

    """recomb"""
    cnt = 0
    for sp in spDB:
        spRDB[sp] = {'H':[],'k':[],'l':[]}
        for v in range(len(spDB[sp]['H']['V'])):
            for d in range(len(spDB[sp]['H']['D'])):
                for j in range(len(spDB[sp]['H']['J'])):
                    indV = spDB[sp]['H']['V'][v]
                    indD = spDB[sp]['H']['D'][d]
                    indJ = spDB[sp]['H']['J'][j]
                    seq = database[indV][4]+database[indD][4]+database[indJ][4]
                    spRDB[sp]['H'].append([seq,indV,indD,indJ])
                    #[seq,ind V,ind D,ind J]
                    cnt+=1
        for v in range(len(spDB[sp]['k']['V'])):
            for j in range(len(spDB[sp]['k']['J'])):
                indV = spDB[sp]['k']['V'][v]
                indJ = spDB[sp]['k']['J'][j]
                seq = database[indV][4]+database[indJ][4]
                spRDB[sp]['k'].append([seq,indV,indJ])
                #[seq,ind V,ind J]
                cnt+=1
        for v in range(len(spDB[sp]['l']['V'])):
            for j in range(len(spDB[sp]['l']['J'])):
                indV = spDB[sp]['l']['V'][v]
                indJ = spDB[sp]['l']['J'][j]
                seq = database[indV][4]+database[indJ][4]
                spRDB[sp]['l'].append([seq,indV,indJ])
                #[seq,ind V,ind J]
                cnt+=1
    print('VDJ germlines = ',end='')
    print(cnt)
    #print(spRDB)
    printRDB()
main()
