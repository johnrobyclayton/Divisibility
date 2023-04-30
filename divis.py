#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 19:52:10 2019

@author: jclayton
"""
# variables

define basesubtractor(divisor,bits,debug){
  auto start,index
  if(divisor%2==0){return -1}
  if(divisor<0){return -3}
  if(bits<=0){return -4}
  if(divisor==0) {return -6}
  index=0
  if(divisor%2==0){
    return 0
  } else {
    start=(divisor+1)/2
    index=1
    while(index<bits){
      if(start%2==0){
        start=start/2
#        print start;print " ";print index;print "\n"
      }else {
        start=(start+divisor)/2
#        print start;print " ";print index;print "\n"
      }
      index=index+1
    }
  }
  return start
}
define subtractor(truncate,divisor,bits,debug){
  auto result
  if(truncate<0){return -1}
  if(divisor<0){return -3}
  if(bits<=0){return -4}
  if(divisor==0) {return -6}
  if(truncate==0){return 0}  

  if(debug==1){
    print "\n*****\nsubtractor\n****\n"
    print "subtractor: truncate: ",truncate,"\n"
    print "subtractor: divisor: ",divisor,"\n"
    print "subtractor: bits: ",bits,"\n"
    print "subtractor: basesubtractor: ",basesubtractor(divisor,bits,debug),"\n"
    print "subtractor: return (divisor-((basesubtractor(divisor,bits)*truncate)%divisor)) ", (divisor-((basesubtractor(divisor,bits,debug)*truncate)%divisor)),"\n"
  }
  result= (divisor-basesubtractor(divisor,bits,debug)*truncate)%divisor
  if(result<0){result=result+divisor}
  return result
}

define truncate(number,bits,debug){
  if(debug==1){
    print "\n*****\ntruncate\n****\n"
    print "truncate: number: ",number,"\n"
    print "truncate: bits: ",bits,"\n"
    print "truncate: return number%(2^bits) ", number%(2^bits),"\n"
  }
  return number%(2^bits)
}
define truncated(number,bits,debug){
  if(debug==1){
    print "\n*****\ntruncated\n****\n"
    print "truncated: number: ",number,"\n"
    print "truncated: bits: ",bits,"\n"
    print "truncated: truncate(number,bits)",truncate(number,bits,debug),"\n"
    print "truncated: return (number-(truncate(number,bits))/(2^bits) ", (number-truncate(number,bits,debug))/(2^bits),"\n"
  }
  return (number-truncate(number,bits,debug))/(2^bits)
}

define reduct(number,divisor,bits,debug){
  if(debug==1){
    print "\n*****\nreduct\n****\n"
    print "reduct: number: ",number,"\n"
    print "reduct: divisor: ",divisor,"\n"
    print "reduct: bits: ",bits,"\n"
    print "reduct: truncated(number,bits) ",truncated(number,bits,debug),"\n"
    print "reduct: truncate(number,bits)",truncate(number,bits,debug),"\n"
    print "reduct: subtractor(truncate(number,bits),divisor,bits)",subtractor(truncate(number,bits,debug),divisor,bits,debug),"\n"
    print "reduct: ","return truncated(number,bits)-subtractor(truncate(number,bits),divisor,bits) ", truncated(number,bits,debug)-subtractor(truncate(number,bits,debug),divisor,bits,debug)
  }
  return truncated(number,bits,debug)-subtractor(truncate(number,bits,debug),divisor,bits,debug)
}

define divides(number,divisor,bits,debug){
  auto result
  result=number
  while(result>0){
    result=reduct(result,divisor,bits,debug)
  }
  if (result==0){
    return 1
  } else {
    return 0
  }
}

define majorremainder(number,divisor,bits,debug){
  auto resulthigh,resultlow
  resulthigh=number
  resultlow=resulthigh
  while(resultlow>0){
    resulthigh=resultlow
    resultlow=reduct(resultlow,divisor,bits,debug)
  }
  return resulthigh
}

define minorremainder(number,step,divisor,bits,debug){
  auto i,result
  if(number<0){return -1}
  if(step<0){return -2}
  if(divisor<0){return -3}
  if(bits<=0){return -4}
  if(number>=(divisor*2^bits)){return -5}
  if(divisor==0) {return -6}
  if(number==0){return 0}  
  result=number%divisor
  for(i=0;i<step;i++){
    result=result*2^bits
    result=result%divisor
  }
  return result
}

define basicdividend(number,divisor,bits,debug){
  auto step,result,remainhigh,remainlow
  result=0
  step=0
  remainhigh=number
  remainlow=number
  while(remainlow>0){
    if(debug==1){
      print "(truncate(remainhigh,bits,debug): ",truncate(remainhigh,bits,debug),"\n"
      print "subtractor(remainhigh,divisor,bits,debug): ",subtractor(remainhigh,divisor,bits,debug),"\n"
    }
    result=result+( ( ( truncate(remainhigh,bits,debug) + subtractor(truncate(remainhigh,bits,debug),divisor,bits,debug) * 2^bits )/divisor )*2^(bits*step))
    remainlow=reduct(remainlow,divisor,bits,debug)
    remainhigh=remainlow
    step=step+1
  }
  return result
}
define steps(number,divisor,bits,debug){
  auto step,result,remainhigh,remainlow
  result=0
  step=0
  remainhigh=number
  remainlow=number
  while(remainlow>0){
    if(debug==1){
      print "(truncate(remainhigh,bits,debug): ",truncate(remainhigh,bits,debug),"\n"
      print "subtractor(remainhigh,divisor,bits,debug): ",subtractor(remainhigh,divisor,bits,debug),"\n"
    }
    result=result+( ( ( truncate(remainhigh,bits,debug) + subtractor(truncate(remainhigh,bits,debug),divisor,bits,debug) * 2^bits )/divisor )*2^(bits*step))
    remainlow=reduct(remainlow,divisor,bits,debug)
    remainhigh=remainlow
    step=step+1
  }
  return step-1
}
 

define dividendremainder(number,divisor,bits,debug){
  auto r,majremainder,minremainder,dividend,wholemultiple,numsteps
  if(number<0){return -1}
  if(number==0){return 0}
  if(divisor<0){return -2}
  if(divisor==0){return -3}
  if(bits<=0){return -4}
  if(bits%1!=0){return -5}
  majremainder=majorremainder(number,divisor,bits,debug)
  numsteps=steps(number,divisor,bits,debug)
  minremainder=minorremainder(majremainder,numsteps,divisor,bits,debug)
  wholemultiple=number-minremainder
  dividend=basicdividend(wholemultiple,divisor,bits,debug)
  print dividend,"  ",minremainder,"\n"
}
