program ojlerovmetod;

var i, n, integer;
    s, h: real;
begin
writeln('Unesite broj koraka, vrednost koraka, pocetno x i y');
readln(n, h, x, y);
s:=y;
for i:=1 to n do
begin
s:=s+h*sqrt(x+s/4);
x:=x+h;
end
writeln('Krajnji rezultat je: ', s:0:2);
readln
end.
