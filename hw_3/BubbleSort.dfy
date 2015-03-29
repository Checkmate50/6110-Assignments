method BubbleSort(a:array<int>) 
  requires a != null;
  requires a.Length < 5;
  ensures forall k:: forall l:: 0 <= k < l < a.Length ==> a[k] <= a[l];
  modifies a;
{
  var i:int := a.Length - 1;
  while(i > 0)
	invariant -1 <= i < a.Length;
	invariant forall par1:: forall par2:: 0 <= par1 <= i && i < par2 < a.Length ==> a[par1] <= a[par2];
	invariant forall elem1:: forall elem2:: i < elem1 < elem2 < a.Length ==> a[elem1] <= a[elem2];
    decreases i;
  {
    var j:int := 0;
    while (j < i)
	  invariant 1 <= i < a.Length;
	  invariant 0 <= j <= i;
	  invariant forall par1:: forall par2:: 0 <= par1 <= i && i < par2 < a.Length ==> a[par1] <= a[par2];
	  invariant forall par1:: 0 <= par1 <= j ==> a[par1] <= a[j];
	  invariant forall elem1:: forall elem2:: i < elem1 < elem2 < a.Length ==> a[elem1] <= a[elem2];
	  decreases i - j;
    {
      if (a[j] > a[j + 1]) {
        var t:int := a[j];
        a[j] := a[j + 1];
        a[j + 1] := t;
      }
	  j := j + 1;
    }
	i := i - 1;
  }
}
