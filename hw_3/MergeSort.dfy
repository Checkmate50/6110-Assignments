method MergeSort(a1:array<int>) returns (a:array<int>)
  requires a1 != null && a1.Length > 0;
  ensures a != null;
  ensures forall k:: forall l:: 0 <= k < l < a.Length ==> a[k] <= a[l];
  //modifies a;
{
  a := ms(a1, 0, a1.Length-1);
  return;
}

method ms(a1:array<int>, l:int, u:int) returns (a:array<int>)
  requires a1 != null;
  requires 0 <= l <= u < a1.Length;
  ensures a != null && a.Length == a1.Length;
  ensures forall elem1:: forall elem2:: l <= elem1 <= elem2 <= u ==> a[elem1] <= a[elem2];
  decreases u - l;
  decreases u;
{
  a := new int[a1.Length];
  assume forall k:: 0 <= k < a1.Length ==> a[k] == a1[k];
  if (l >= u)
  {
    return;
  }
  else
  {
    var m:int := (l + u) / 2;
    a := ms(a, l, m);
    a := ms(a, m+1, u);
    a := merge(a, l, m, u);
    return;
  }
}

method merge(a1:array<int>, l:int, m:int, u:int) returns (a:array<int>)
  requires a1 != null;
  requires 0 <= l <= m < u < a1.Length;
  ensures a != null && a.Length == a1.Length;
  ensures forall elem1:: forall elem2:: l <= elem1 <= elem2 <= u ==> a[elem1] <= a[elem2];
{
  a := new int[a1.Length];
  assume forall k:: 0 <= k < a1.Length ==> a[k] == a1[k];
  var buf := new int[u-l+1];
  var i:int := l;
  var j:int := m + 1;
  var k:int := 0;

  while (k < u-l+1)
	invariant m + 1 <= j <= a.Length;
	invariant l <= i <= m + 1;
	invariant k == i - l + j - m - 1;
	invariant i > m ==> j < a.Length || k > u-l;
	decreases u-l-k;
  {
    if (i > m)
    {
      buf[k] := a[j];
      j := j + 1;
    }
    else if (j > u)
    {
      buf[k] := a[i];
      i := i + 1;
    }
    else if (a[i] <= a[j])
    {
      buf[k] := a[i];
      i := i + 1;
    }
    else
    {
      buf[k] := a[j];
      j := j + 1;
    }
    k := k + 1;
  }

  assume k == buf.Length;
  assume forall elem1:: forall elem2:: 0 <= elem1 <= elem2 < k ==> buf[elem1] <= buf[elem2];
  k := 0;
  while (k < u-l+1)
	invariant 0 <= k <= u - l + 1 == buf.Length;
	invariant forall elem1:: 0 <= elem1 < k ==> a[elem1 + l] == buf[elem1]; //Assert equality between arrays
	invariant forall elem1:: forall elem2:: 0 <= elem1 <= elem2 < buf.Length ==> buf[elem1] <= buf[elem2];
	invariant forall elem1:: forall elem2:: 0 <= elem1 <= elem2 < k ==> buf[elem1] <= buf[elem2]; //buf is sorted on [0, k)

	invariant forall elem1:: forall elem2:: l <= elem1 <= elem2 < k + l ==> a[elem1] <= a[elem2];
	decreases u-l-k;
  {
    a[l + k] := buf[k];
    k := k + 1;
  }
}

