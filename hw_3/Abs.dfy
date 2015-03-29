method AbsArray(a:array<int>)
  requires a != null;
  modifies a;
  ensures forall k:: 0 <= k < a.Length ==> a[k] >= 0;
{
  var i:int := 0;
  while (i < a.Length)
	invariant 0 <= i <= a.Length;
	invariant forall k:: 0 <= k < i ==> a[k] >= 0;
	decreases a.Length - i;
  {
    if (a[i] < 0)
	{
      a[i] := -a[i];
    }
	i := i + 1;
  }
}
