

# This file was *autogenerated* from the file solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_138963980427736364646203557164328211078134463518489686365728312873583832517087170768576679472472907142081360480944201759920246566585465801088226164314480607014663211599932950864391702460227584467326051919881067028851940610382044445003060103566003934601979805899293539507221062915314813557293919231917284247667 = Integer(138963980427736364646203557164328211078134463518489686365728312873583832517087170768576679472472907142081360480944201759920246566585465801088226164314480607014663211599932950864391702460227584467326051919881067028851940610382044445003060103566003934601979805899293539507221062915314813557293919231917284247667); _sage_const_65537 = Integer(65537); _sage_const_26363325527372681448374836719361674028908733933823971039273016094221739663363697355984980560218941405351917768372297139270315950803631724328547161889191685480725185971092638691575587334307068143724069148715129866085595445974433311000459043513392513632639058879350662222598941781017396217632160254074487773693 = Integer(26363325527372681448374836719361674028908733933823971039273016094221739663363697355984980560218941405351917768372297139270315950803631724328547161889191685480725185971092638691575587334307068143724069148715129866085595445974433311000459043513392513632639058879350662222598941781017396217632160254074487773693); _sage_const_90 = Integer(90); _sage_const_2 = Integer(2); _sage_const_54 = Integer(54); _sage_const_0p2 = RealNumber('0.2'); _sage_const_200 = Integer(200)
def factorial(n):
    if n == _sage_const_0 :
        return _sage_const_1 
    return factorial(n-_sage_const_1 ) * n
N = _sage_const_138963980427736364646203557164328211078134463518489686365728312873583832517087170768576679472472907142081360480944201759920246566585465801088226164314480607014663211599932950864391702460227584467326051919881067028851940610382044445003060103566003934601979805899293539507221062915314813557293919231917284247667  
e = _sage_const_65537  
flag = _sage_const_26363325527372681448374836719361674028908733933823971039273016094221739663363697355984980560218941405351917768372297139270315950803631724328547161889191685480725185971092638691575587334307068143724069148715129866085595445974433311000459043513392513632639058879350662222598941781017396217632160254074487773693 
M = factorial(_sage_const_90 )
a = pow(M,-_sage_const_1 ,N)
P = PolynomialRing(Zmod(N), names=('x',)); (x,) = P._first_ngens(1)
f = x + a
x = f.small_roots(X=_sage_const_2 **_sage_const_54 ,beta=_sage_const_0p2 ,epsilon=_sage_const_1 /_sage_const_200 )
# [8400642479283129]
p = x*M + _sage_const_1 
assert N % p == _sage_const_0 

