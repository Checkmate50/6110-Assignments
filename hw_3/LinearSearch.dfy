method LinearSearch(a:array<int>, l:int, u:int, e:int) returns (r:bool)
  requires a != null;
  requires 0 <= u < a.Length;
  requires 0 <= l <= u;
  ensures r <==> exists k:: l <= k && k <= u && a[k] == e;
{
  var i := l;
  r := false;
  while (i <= u)
	invariant l <= i <= u + 1;
	invariant forall k:: l <= k < i ==> a[k] != e;
	decreases u - i;
  {
    if (a[i] == e)
	{
	  r := true;
	  return;
	}
    i := i + 1;
  }
}
