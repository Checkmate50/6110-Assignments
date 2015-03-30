method InsertionSort(a:array<int>)
  requires a != null && a.Length > 0;
  ensures forall k:: forall l:: 0 <= k <= l < a.Length ==> a[k] <= a[l];
  modifies a;
{
  var i:int := 1;
  while(i < a.Length)
	invariant 1 <= i <= a.Length;
	invariant forall elem1:: forall elem2:: 0 <= elem1 <= elem2 < i ==> a[elem1] <= a[elem2];
	decreases a.Length - i;
  {
    var t:int := a[i];
	var j:int := i - 1;
	while (j >= 0)
	  invariant -1 <= j < i;
	  invariant j == i - 1 ==> t == a[i];
	  invariant forall elem1:: j < elem1 < i ==> t < a[elem1];
	  invariant forall elem1:: forall elem2:: 0 <= elem1 <= elem2 < i ==> a[elem1] <= a[elem2];
	  decreases j;
	{
	  if (a[j] <= t)
	  {
	    break;
      }
	  a[j + 1] := a[j];
      j := j - 1;
	}
    a[j + 1] := t;
    i := i + 1;
  }
}
