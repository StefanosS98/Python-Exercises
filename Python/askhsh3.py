#������ 3
print '�������� ��� ����� ��������� ����� �����'
a=raw_input()
a=[int(x) for x in a]
print '� ����� ��� ������ �����:',a
c=len(a)
k=0
b=list(a)
for i in range(0,c):
    if a[i]!=0:
        b[k]=a[i]
        k=k+1
    i=i+1
for i in range(k,c):
    b[i]=0
s=0    
for i in range(0,c):
    if b[i]==0:
        s=s+1
if s!=0:
    print '� ����� �� �� �������� �������� ��� ����� �����:',b
else:
    print '� ����� ��������� � ����:',b

