from django.shortcuts import render
from django.db.models import Avg,Sum,Max,Min,Count
# Create your views here.
from app.models import *

def EmpDept(request):
    LEDO=EMP.objects.select_related('DEPTNO').all()
    LEDO=EMP.objects.select_related('DEPTNO').filter(JOB='SALESMAN')
    LEDO=EMP.objects.select_related('DEPTNO').filter(COMM__isnull=True)
    LEDO=EMP.objects.select_related('DEPTNO').filter(COMM__isnull=False)
    LEDO=EMP.objects.select_related('DEPTNO').filter(MGR__isnull=False,ENAME__startswith='A')
    LEDO=EMP.objects.select_related('DEPTNO').filter(MGR__isnull=True,ENAME__startswith='A')
    LEDO=EMP.objects.select_related('DEPTNO').filter(ENAME__startswith='S')
    LEDO=EMP.objects.select_related('DEPTNO').filter(ENAME__endswith='H')
    LEDO=EMP.objects.select_related('DEPTNO').filter(JOB__startswith='M')
    LEDO=EMP.objects.select_related('DEPTNO').filter(EMPNO=7566)
    LEDO=EMP.objects.select_related('DEPTNO').filter(HIREDATE='1981-12-03')
    LEDO=EMP.objects.select_related('DEPTNO').filter(DEPTNO__DNAME='ACCOUNTING')
    LEDO=EMP.objects.select_related('DEPTNO').filter(DEPTNO__DNAME__startswith='S')
    # LEDO=EMP.objects.select_related('DEPTNO').all()
    print(EMP.objects.all().aggregate(Avg('SAL')))
    print(EMP.objects.all().aggregate(avg_sal=Avg('SAL')))
    print(EMP.objects.all().aggregate(sum_sal=Sum('SAL')))
    print(EMP.objects.values('DEPTNO').annotate(Avg('SAL')))
    print(EMP.objects.filter(DEPTNO=20).aggregate(Avg('SAL')))
    DOAVG=EMP.objects.all().aggregate(sal_avg=Avg('SAL'))
    print(DOAVG)
    LEDO=EMP.objects.select_related('DEPTNO').filter(SAL__lt=DOAVG['sal_avg'])

    d={'LEDO':LEDO}
    return render(request,'EmpDept.html',d)


def EmpMgr(request):
    LEMO=EMP.objects.select_related('MGR').all()
    LEMO=EMP.objects.select_related('MGR').filter(MGR__isnull=False)
    LEMO=EMP.objects.select_related('MGR').filter(DEPTNO=30)
    LEMO=EMP.objects.select_related('MGR').filter(SAL__gt=3000)
    LEMO=EMP.objects.select_related('MGR').filter(MGR__SAL__gt=800)

    d={'LEMO':LEMO}
    return render(request,'EmpMgr.html',d)


def EmpMgrDept(request):
    LEMDO=EMP.objects.select_related('DEPTNO','MGR').all()
    LEMDO=EMP.objects.select_related('DEPTNO','MGR').filter(DEPTNO__DNAME='RESEARCH')
    LEMDO=EMP.objects.select_related('DEPTNO','MGR').filter(MGR__ENAME='SMITH')
    LEMDO=EMP.objects.select_related('DEPTNO','MGR').filter(COMM__isnull=False)

    d={'LEMDO':LEMDO}
    return render(request,'EmpMgrDept.html',d)


def DeptEmp(request):
    LDEO=DEPT.objects.prefetch_related('emp_set').all()

    d={'LDEO':LDEO}
    return render(request,'DeptEmp.html',d)