#http://merthsoft.com/linkguide/ti83+/fformat.html
#http://merthsoft.com/linkguide/ti83+/vars.html#equation
#http://merthsoft.com/linkguide/ti83+/tokens.html#sysvar
def b2d(b1,b2):
 if b1>256 or b2>256:
  raise IndexError
 return b2*256+b1
def dtoken(b1,b2):
 global cp
 cp+=1
 try:
  val=b1
  table=["null",">DMS",">Dec",">Frac","->","BoxPlot","[","]","{","}","r","°","^-1","^2","T","^3","(",")","round(","pxl-Test(","augment(","rowSwap(","row+(","*row(","*row+(","max(","min(","R>Pr(","R>P[theta](","P>Rx(","P>Ry(","median(","randM(","mean(","solve(","seq(","fnInt(","nDeriv(","null","fMin(","fMax("," ",'"',",","i","!","CubicReg ","QuartReg ","0","1","2","3","4","5","6","7","8","9",".","E"," or "," xor ",":","\n"," and ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[theta]","&5C","&5D","&5E","prgm","&60","&61","&62","&63","Radian","Degree","Normal","Sci","Eng","Float","=","<",">","<=",">=","!=","+","-","Ans","Fix ","Horiz","Full","Func","Param","Polar","Seq","IndpntAuto","IndpntAsk","DependAuto","DependAsk","&7E","[box]","[cross]","[dot]","*","/","Trace","ClrDraw","ZStandard","ZTrig","ZBox","Zoom In","Zoom Out","ZSquare","ZInteger","ZPrevious","ZDecimal","ZoomStat","ZoomRcl","PrintScreen","ZoomSto","Text("," nPr "," nCr ","FnOn ","FnOff ","StorePic ","RecallPic ","StoreGDB","RecallGDB ","Line(","Vertical ","Pt-On(","Pt-Off(","Pt-Change(","Pxl-On(","Pxl-Off(","Pxl-Change(","Shade(","Circle(","Horizontal ","Tangent(","DrawInv ","DrawF","&AA","rand","[pi]","getKey","'","?","-","int(","abs(","det(","identity(","dim(","sum(","prod(","not(","iPart(","fPart(","&BB","√(","∛(","ln (","e^(","log(","10^(","sin(","sin^-1(","cos(","cos^-1(","tan(","tan^-1","sinh(","sinh^-1(","cosh(","cosh^-1(","tanh(","tanh^-1(","If ","Then","Else","While ","Repeat ","For(","End","Return","Lbl ","Goto ","Pause ","Stop","IS>(","DS>(","Input ","Prompt ","Disp ","DispGraph","Output(","ClrHome","Fill(","SortA(","SortD(","DispTable","Menu(","Send(","Get(","PlotsOn ","PlotsOff ","L","Plot1(","Plot2","Plot3","&EF","^","[xth root]","1-Var Stats ","2-Var Stats ","LinReg(a+bx) ","ExpReg ","LnReg ","PwrReg","Med-Med","QuadReg ","ClrList","ClrTable","Histogram","xyLine","Scatter","LinReg(ax+b) "]
  token=table[val]
  if token[0]=="&":
   cp+=1
   ref=token[1:3]
   if ref=="EF":
    token=['null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'BLUE', 'RED', 'BLACK', 'MAGENTA', 'GREEN', 'ORANGE', 'BROWN', 'NAVY', 'LTBLUE', 'YELLOW', 'WHITE', 'LTGRAY', 'MEDGRAY', 'GRAY', 'DARKGRAY', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'BackgroundOn ', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'BackgroundOff ', 'null', 'null', 'TextColor('][b2]
   if ref=="5C":
    token=["[A]","[B]","[C]","[D]","[E]","[F]","[G]","[H]","[I]","[J]"][b2]
   if ref=="5D":
    token=["L1","L2","L3","L4","L5","L6","L7","L8","L9","L0"][b2]
   if ref=="5E":
    token=['null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','Y1','Y2','Y3','Y4','Y5','Y6','Y7','Y8','Y9','Y0','null','null','null','null','null','null','X1T','Y1T','X2T','Y2T','X3T','Y3T','X4T','Y4T','X5T','Y5T','X6T','Y6T','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','r1','r2','r3','r4','r5','r6','u','v','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','u','v','w'][b2]
   if ref=="60":
    token=["pic1","pic2","pic3","pic4","pic5","pic6","pic7","pic8","pic9","pic0"][b2]
   if ref=="61":
    token=["GDB1","GDB2","GDB3","GDB4","GDB5","GDB6","GDB7","GDB8","GDB9","GDB0"][b2]
   if ref=="62":
    token=["null","RegEq","n","[x-mean]","[Sigma]x","[Sigma]x^2","Sx","[sigma]x","minX","MaxX","MinY","MaxY","[y-mean]","[Sigma]y","[Sigma]y^2","Sy","[sigma]y","[Sigma]xy","r","Med","Q1","Q3","a","b","c","d","e","X1","X2","X3","Y1","Y2","Y3","n","p","z","t","[chi]2","F","df","[p-hat]","[p-hat]1","[p-hat]2","[x-mean]1","Sx1","n1","[x-mean]2","Sx2","n2","Sxp","lower","upper","s","r2","R2","df","SS","MS","df","SS","MS"][b2]
   if ref=="63":
    token=["ZXscl","ZYscl","Xscl","Yscl","UnStart","VnStart","Un-1","Vn-1","ZUnStart","ZVnStart","Xmin","Xmax","Ymin","Ymax","Tmin","Tmax","[theta]min","[theta]max","ZXmin","ZXmax","ZYmin","ZYmax","Z[theta]min","Z[theta]max","ZTmin","ZTmax","TblMin","nMin","ZnMin","nStart","ZnStart","[delta]tbl","Tstep","[theta]step","ZTstep","Z[theta]step","[delta]X","[delta]Y","XFact","YFact","TblInput","N","I%","PV","PMT","FV","Xres","ZXres"][b2]
   if ref=="AA":
    token=["Str1","Str2","Str3","Str4","Str5","Str6","Str7","Str8","Str9","Str0"][b2]
   if ref=="7E":
    token=["Sequential","Simul","PolarGC","RectGC","CoordOn","CoordOff","Connected","Dot","AxesOn","AxesOff","GridOn","GridOff","LabelOn","LabelOff","Web","Time","uvAxes","vwAxes","uwAxes"][b2]
   if ref=="BB":
    token=['npv(', 'irr(', 'bal(', '[Sigma]Prn(', '[Sigma]Int(', '>Nom(', '>Eff(', 'dbd(', 'lcm(', 'gcd(', 'randInt(', 'randbin(', 'sub(', 'stdDev(', 'variance(', 'inString(', 'normalcdf(', 'invNorm(', 'tcdf(', '[chi]^2cdf(', '[F]cdf(', 'binompdf(', 'binomcdf(', 'poissonpdf(', 'poissoncdf(', 'geometpdf(', 'geometcdf(', 'normalpdf(', 'tpdf(', '[chi]2pdf(', '[F]pdf(', '[F]pdf', 'randNorm(', 'tvm pmt', 'tvm i%', 'tvm Pv', 'tvm N', 'tvm FV', 'conj(', 'real(', 'imag(', 'angle(', 'cumSum(', 'expr(', 'length(', '[Delta]List(', 'ref(', 'rref(', '>Rect(', '>Polar', 'e', 'SinReg ', 'Logistic ', 'LinRegTTest ', 'ShadeNorm(', 'Shade t(', 'Shade[chi]2(', 'Shade[F](', 'Matr>list', 'List>matr', 'Z-Test(', 'T-Test ', '2-SampZTest(', '1-PropZTest(', '2-PropZTest(', '[chi]2-Test(', 'ZInterval ', '2-SampZInt(', '1-PropZInt(', '2-PropZInt(', 'GraphStyle', '2-SampTTest ', '2-Samp[F]Test ', 'TInterval ', '2-SampTInt ', 'SetUpEditor ', 'PMT End', 'PMT Bgn', 'Real', 're^[theta]i', 'a+bi', 'ExprOn', 'ExprOff', 'ClrAllLists', 'GetCalc(', 'DelVar ', 'Equ>String(', 'String>Equ(', 'Clear Entries', 'Select(', 'ModBoxPlot', 'NormProbPlot', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null','null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', "null",'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'][b2]
 except IndexError:
  token="null"
 if token=="null":
  return "(NULLCHAR ERROR "+str(b1)+" "+str(b2)+")"
 return token
def conbin(s):
 out=""
 for a in s:
  out+=chr(a)
 return out
def decode(ftext):
 outtext=""
 #print comment
 print(conbin(ftext[11:53]))
 #decode data section size
 try:
  fsize=b2d(ftext[53],ftext[54])+57
 except:
  print("error decoding length bytes\ndecoding using raw length")
  fsize=len(ftext)
  #this works too i just dont like using it 
 global cp
 cp=55
 #taking into account checksum size
 while cp!=fsize-2:
  try:
   bs=b2d(ftext[cp],ftext[cp+1])
  except:
   print('error')
  cp+=2
  try:
   vardat=b2d(ftext[cp],ftext[cp+1])
  except:
   print('error')
  cp+=2 
  try:
   vartype=ftext[cp]
  except:
   print('error')
  #probs 5 idk tho
  cp+=1
  #var name
  print(conbin(ftext[cp:cp+8]))
  cp+=8
  try:
   version=ftext[cp]
  except:
   print('error')
  #version should be 0
  #im gonna skip the flag i dont think i need it
  cp+=4
  #im also going to skip this length value as its a duplicate 
  #token time
  tokens=b2d(ftext[cp],ftext[cp+1])
  cp+=2
  limit=cp+tokens
  while cp<limit:
   tok=dtoken(ftext[cp],ftext[cp+1])
   outtext+=tok
 return outtext
  
name=input("name:")
f=open(name,"rb").read()
s=decode(f)
f=open(name.replace("8xp","txt"),"w",encoding="utf-8")
f.write(s)
f.close()