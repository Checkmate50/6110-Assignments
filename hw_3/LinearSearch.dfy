method LinearSearch(a:array<int>, l:int, u:int, e:int) returns (r:bool)
  ensures r <==> exists k:: l <= k && k <= u && a[k] == e;
{
  var i := l;
  r := false;
  while (i <= u)
  {
    if (a[i] == e)
	{
	  r := true;
	  return;
	}
    i := i + 1;
  }
}
