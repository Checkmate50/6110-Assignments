method BubbleSort(a:array<int>)
  ensures forall k:: forall l:: 0 <= k < l < a.Length ==> a[k] <= a[l];
  modifies a;
{
  var i:int := a.Length - 1;
  while(i > 0)
  {
    var j:int := 0;
    while (j < i)
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
