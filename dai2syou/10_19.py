#100本ノックNo.10-19

#################No.10##################
#UNIXコマンド　wc
#行数や文字数をカウントする
#wc -l hightemp.txt
thisfile=open("hightemp.txt","r")
count=0
for data in thisfile:
    count+=1
print(count)
thisfile.close()

#other sample
thisfile="hightemp.txt"
count=0
with open(thisfile) as data:
    for line in data:
        count += 1
print(count)
#################No.11##################
#UNIXコマンド　sed,tr,expand
#gsed -i 's/\t/ /g' hightemp.txt
f="hightemp.txt"
outfile11="hightemp11.txt"
result=[]
with open(f,mode="r") as data:
    for line in data:
        line=line.replace("\t"," ")
        result.append(line)
        #print("new"+str(result))

with open(outfile11,mode="w") as data:
    data.writelines(result)

#################No.12##################
#UNIXコマンド　cut
#2列目をカットして新規ファイルを作成する
#cut -f 2 hightemp.txt > col2.txt
outf1="col1.txt"
outf2="col2.txt"

with open(f,"r") as file,open(outf1,"w") as of1,open(outf2,"w") as of2:
    for line in file:
        line_cols=line.split("\t")
        of1.write(line_cols[0]+"\n")
        of2.write(line_cols[1]+"\n")

#################No.13##################
#UNIXコマンド　paste
#paste col1.txt col2.txt >output.txt
#rstrip()で右端の文字（改行文字）を除外している

outf3="outfile13.txt"
with open(outf1,"r") as f1,open(outf2,"r") as f2,open(outf3,"w") as of3:
    for fl1,fl2 in zip(f1,f2):
        of3.write(fl1.rstrip()+"\t"+fl2.rstrip()+"\n")

#################No.14,15##################
#UNIXコマンド　head,tail

n = input("自然数：")
n = int(n)

print("頭から{0}行表示".format(n))
with open(f,"r") as file:
    lines = file.readlines()
    for line in lines[:n]:#スライスを利用する
        print(line)

print("末尾から{0}行表示".format(n))
with open(f,"r") as file:
    lines = file.readlines()
    for line in lines[-n:]:
        print(line)

#################No.16##################
#UNIXコマンド　split
with open(f,"r") as files:
    l = files.readlines()
    if len(l)%n == 0:
        for (i,row) in enumerate(l):
            fo = open("out{}".format(int(i/n)),"a")
            fo.write(row)
            fo.close()

#################No.17##################
#UNIXコマンド　sort,uniq
heads = set()
with open(f,"r") as files:
    l = files.readlines()
    for line in l:
        heads.add(line[:1:])
print(heads)

#################No.18##################
#UNIXコマンド　sort
with open(f,"r") as files:
    l = files.readlines()
    sorted(l,key=lambda x:x[2],reverse=True)
    for line in l:
        print(line)

#################No.19##################
#UNIXコマンド　cut,uniq,sort

from collections import defaultdict

p = defaultdict(int)
with open(f,"r") as files:
    l = files.readlines()
    for line in l:
        p[line.split()[0]]+=1
    for k,v in sorted(p.items(),key=lambda x:x[1],reverse=True):
        print(k)












