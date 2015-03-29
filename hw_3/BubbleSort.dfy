method BubbleSort(a:array<int>)
  requires a != null;
  ensures forall k:: forall l:: 0 <= k < l < a.Length ==> a[k] <= a[l];
  modifies a;
{
  var i:int := a.Length - 1;
  while(i > 0)
	invariant a.Length == 0 || i >= 0;
    decreases i;
  {
    var j:int := 0;
    while (j < i)
	  invariant j <= i;
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
