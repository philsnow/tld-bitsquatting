# TLD bitsquatting

More has been written elsewhere about bitsquatting (and better than I could).  See e.g. https://github.com/benjaminpetrin-zz/bitsquatting , on which this repo is based.

## but TLDs in particular

The above-referenced project only deals with the domain part that comes before the TLD.  The `example` in `example.com`.  But what about the TLD itself?

```
% python tld_bitsquat.py tlds-alpha-by-domain.txt | grep \^com
com:  bom
```

... `bom`?  Today I learned: https://icannwiki.org/.bom .  As of this writing it doesn't have a general availability date, so not an issue at all for `.com`, yet.

_Probably won't be an issue either since `example.bom` is probably going to be more expensive when it becomes available than `examphe.com`, but they're both a single bit-flip away from the target domain._

Let's look at some more candidates.  The output is `<target TLD>:  <list of bitsquattable TLDs>`.

```
ac:  ag cc ec as
ad:  af at al cd id ae
ae:  au am ee ag ie ad
af:  ag ad cf
ag:  af ao ac cg aw eg ae
ai:  am ci
al:  cl il am ad
am:  ao al im ae ai cm
ao:  am io co ag
aq:  au iq as
ar:  az as er cr ir
as:  es ac ar aw is aq
at:  et it ad au
au:  at eu cu aw ae aq
aw:  cw as au ag
ax:  az cx
az:  cz ax ar
ba:  be bi ca
bb:  bj br bf
bd:  be bt cd bf
be:  bg bd bm re je ba
bf:  bv cf bg bn bd bb
bg:  cg bo be bw bf
bh:  bi ch bj
bi:  bm ci by fi ba bh
bj:  fj bz bn bb bh
bm:  bi jm bo be fm cm
bn:  cn bo bj bf
bo:  bg jo ro co bm bn fo
br:  bs bv fr bz cr bb
bs:  rs br bw
bt:  bv bd
bv:  br cv bt bw bf
bw:  bs bv bg cw rw
by:  cy bi
bz:  cz br bj
ca:  sa cc ci ba ga
cc:  sc ac ca cg ck
cd:  cl cf sd bd gd ad
cf:  gf af cv cg cd cn bf
cg:  bg cf cw kg co gg cc ag sg
ch:  cl kh cx ci gh sh bh
ci:  bi ch ca ck ki si cy gi ai cm
ck:  cc ci sk co
cl:  ch al cd cn sl gl cm
cm:  cl co bm sm km am gm ci
cn:  cl cf co gn kn sn bn
co:  ao cg ck bo cn so cm
cr:  br cv gr sr cz kr ar
cu:  au cw gu su
cv:  bv cf cw sv cr
cw:  cv kw cg cu gw bw aw
cx:  ch sx cz ax cy
cy:  ky cx gy ci by sy
cz:  az sz kz cx bz cr
de:  ee dm
dj:  dk tj fj dz
dk:  dj tk do fk lk
dm:  tm fm de do
do:  dk fo to dm
dz:  dj tz
ec:  mc es ac eg
ee:  de eu me eg ge ae
eg:  ec mg ug gg ee ag
er:  gr es mr ar
es:  ec as ms er gs us
et:  gt mt at eu
eu:  gu et au ee mu
fi:  bi ni vi fk gi fm
fj:  dj bj fk
fk:  dk fi fj fo
fm:  bm gm fi fo dm
fo:  no do bo fk fm
fr:  gr nr br
ga:  ge gi ca gq
gb:  gr gf
gd:  gf cd gl gt ge
ge:  gu gg gm ee gd ga
gf:  cf gn gg wf gb gd
gg:  gf cg gw eg ge
gh:  gi ch gl
gi:  gy gm ci gh fi ga
gl:  cl gn gm gh gd
gm:  om gl ge gi fm cm
gn:  gf cn gl
gp:  gt gr gq
gq:  gu gs gy gp ga
gr:  fr er gs gp gb cr
gs:  es gr gw ws gq
gt:  et gp gu gd
gu:  eu cu gw gt ge gq
gw:  cw gu gg gs
gy:  cy gi gq
hk:  lk
hm:  jm im
hn:  in
hr:  lr ir
ht:  hu it lt
hu:  lu ht
id:  md il ie it ad
ie:  ke me id im ae ye
il:  al id im ml in
im:  il mm km am hm ie io
in:  il mn kn io hn
io:  im ao in mo
iq:  is mq aq
ir:  mr kr hr is ar
is:  ir ms iq as
it:  mt ht at id yt
je:  ke be jm ne
jm:  jo bm km hm zm je
jo:  jm no bo
jp:  np kp
ke:  kg je ie km
kg:  ke kw cg
kh:  ch ki
ki:  kh km ci ky
km:  jm ke om im ki cm
kn:  cn in
kp:  jp kr
kr:  kz cr ir kp
kw:  kg cw
ky:  cy ki
kz:  cz kr
la:  na ma lc li
lb:  lr lc
lc:  nc lb mc la ls lk
li:  ly ni la lk
lk:  mk dk lc hk li
lr:  lb lv nr mr hr ls
ls:  lr lc ms
lt:  lv lu ht mt
lu:  nu lt mu hu
lv:  lr mv lt
ly:  my li
ma:  mq mc la me
mc:  ec mk ms mg lc ma
md:  me mt ml id
me:  md mm ma mg ee ie mu
mg:  mo mc me eg mw
mh:  mx ml
mk:  mc lk mo
ml:  mh md il mm mn
mm:  mo om me im ml
mn:  in ml mo
mo:  mk mm mg mn io
mp:  mq mt mx mr
mq:  my ms ma mp mu iq
mr:  mv mz lr ms er mp ir
ms:  es mc mr ls is mq mw
mt:  mv mu md et lt mp it
mu:  mt eu me lu mq mw
mv:  lv mt mr mw
mw:  mg ms mu mv
mx:  mp mz mh my
my:  ly mq mx
mz:  mx mr
na:  ni nc la ne
nc:  na lc ng
ne:  na je ng nu
nf:  ng
ng:  nc no ne nf
ni:  na fi li
no:  jo ng fo
np:  jp nr
nr:  fr lr np nz
nu:  lu ne
nz:  nr
om:  km gm mm
pa:  pe qa
pe:  re pg pm pa
pf:  tf pg pn
pg:  pe pf tg pw
ph:  th pl
pk:  tk
pl:  ph pm pn tl
pm:  pe tm pl
pn:  tn pl pf
pr:  ps tr
ps:  rs pr pw
pt:  tt
pw:  pg ps rw tw
qa:  ua sa pa
re:  pe se ve be ru
ro:  bo so
rs:  bs ps ss rw
ru:  re rw su vu
rw:  zw rs ru bw pw
sa:  sc ca se si qa
sb:  sj sc sr
sc:  sa ss cc sk sg sb
sd:  sl st cd se
se:  sa su sm re sd sg
sg:  se cg sc so
sh:  ch sx sj sl si
si:  sa sm ci sk sy sh
sj:  sz sn sk sb sh
sk:  sc sj ck si so
sl:  cl sm sn sd sh
sm:  se sl si so cm
sn:  cn sj sl so
so:  ro co sm sn sk sg
sr:  sz ss sv sb cr
ss:  rs ws sc sr
st:  sd su sv
su:  st cu ru se
sv:  cv st sr
sx:  sh sy sz cx
sy:  cy si sx
sz:  cz sj sr sx
tc:  vc tk tg
td:  tl tf tt
tf:  tn td pf tv tg
tg:  tf tc pg ug tw to vg
th:  tl tj ph
tj:  dj th tn tk tz
tk:  tc pk dk to tj uk
tl:  th tm tn td pl
tm:  tl pm to dm
tn:  tf vn to tj pn tl
to:  tm tn tk do tg
tr:  pr tz tv
tt:  pt tv td
tv:  tf tr tw tt
tw:  tv tg pw
tz:  tj uz tr dz
ua:  qa
ug:  tg eg
uk:  tk
us:  es ws
uz:  tz
va:  vc vi ve
vc:  vg tc va
ve:  re vg vu va
vg:  vc ve tg
vi:  fi va
vn:  tn
vu:  ru ve
wf:  gf
ws:  ss us gs
ye:  ie
yt:  it
zm:  jm
zw:  rw
abb:  abc
abc:  abb
aco:  eco
bar:  car
bio:  jio rio
bms:  bmw
bmw:  bms
bom:  boo com
boo:  bom foo
bot:  jot
box:  fox
cab:  car
cal:  cam gal
cam:  cal
car:  bar cab
cba:  cfa
cbs:  sbs crs
cfa:  cba
com:  bom
cpa:  spa
crs:  cbs
day:  diy
dds:  lds
diy:  day
eco:  aco
foo:  boo goo
fox:  box
gal:  cal
gmo:  goo
goo:  gmo ooo foo
gop:  got
got:  gov gop
gov:  got
hkt:  hot
hot:  hkt jot
ibm:  ifm
ice:  icu
icu:  ice
ifm:  ibm
inc:  ink ing
ing:  inc
ink:  inc
jio:  bio
jot:  hot bot
lds:  dds
man:  men
men:  man
moe:  mom
moi:  mom
mom:  moi moe
nba:  nra
nra:  nba
ntt:  ott
one:  ong
ong:  one
ooo:  goo
ott:  ntt
phd:  thd pid
pid:  phd
pin:  xin
ren:  run
rio:  bio
rip:  vip zip
run:  ren
sas:  ses
sbs:  cbs
ses:  sas sew
sew:  ses
ski:  sky
sky:  soy ski
soy:  sky
spa:  cpa
stc:  wtc
thd:  phd
vin:  win
vip:  rip
win:  vin
wtc:  stc
xin:  pin
zip:  rip
best:  rest
cafe:  safe
care:  case
casa:  case
case:  care casa
citi:  city
city:  citi
data:  date
date:  data
dish:  fish
fish:  dish
gold:  golf
golf:  gold
life:  live
like:  nike
live:  life
nike:  like
prod:  prof
prof:  prod
reit:  rmit
rest:  best
rmit:  reit
safe:  save cafe
save:  safe
email:  gmail
gmail:  email
lexus:  nexus
nexus:  lexus
tjmaxx:  tkmaxx
tkmaxx:  tjmaxx
booking:  cooking
cooking:  booking
```

... quite a bit more to work with here.  Particularly the ccTLDs seem very densely packed with opportunity.

## How to use this

### If you're a malicious-minded person

Find a line in the above output where

1. the target TLD is widely-used, and
2. at least one of the bitsquattable domains is cheap to register

then, register a ton of domains at the cheap TLD, and squat on them.

### If you're on blue team

If you're responsible for a domain in one of the likely TLDs from the previous section:

If you control the client side (usually the case for mobile apps) you're in luck:  you can use certificate pinning in the client as a way to ensure your code is talking to the right servers.  You might already be doing this to protect against DNS spoofing/poisoning.  :tada:

If, on the other hand, you don't control the clients (most normal web sites), still not all is lost.  The attack relies on the client having a bit flipped in DRAM or whereever "early" enough so that the client tries to resolve DNS for the bitsquatted domain (and TCP has checksumming which makes it likely to catch and correct single bit-flips, through retransmission).  Depending on where the bit flip happened, the browser might use the cookie jar for `examphe.com` (presumably empty) instead of `example.com`, so the attacker won't get cookies from (all of) your users.
