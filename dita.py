import os,subprocess,pandas
tws=[xi for xi in os.listdir() if x.endswith(".csv")]
z=pandas.read_csv(tws[0])
for br,ass in zip(z.Summary,z.Assignee):
    bn="".join([a for a in bn if a == '_' or a.isalpha()])
    bn+=("_"+ass.replace(".","_"))
    bn=bn.replace("_",".")
    cc=f'cd ..;git checkout -b {bn};touch {ass.notes};echo {bn} >> {ass.notes};git commit -m "Init {datetime.datetime.utcnow()}";git push --set-upstream origin {bn};git push -o mergerequest.create'
    subprocess.call(cc,shell=True)