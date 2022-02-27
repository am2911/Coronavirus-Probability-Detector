from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render , HttpResponse
import pickle

file=open("model.pkl2","rb")
clf=pickle.load(file)

# Create your views here.
def about(request):  
    try:
        if request.method=="POST":
            Fever=(request.POST.get("Fever")) 
            Bodypain=request.POST.get("Bodypain") 
            Age=request.POST.get("Age") 
            Runnynose=request.POST.get("Runnynose") 
            Diffbreath=request.POST.get("Diffbreath") 

            print(Fever,Bodypain,Age,Runnynose,Diffbreath)
            inputFeature=[Fever,Bodypain,Age,Runnynose,Diffbreath]
            infprob=clf.predict_proba([inputFeature])[0][1]
            
            print(round(infprob*100))
            inforate=round(infprob*100)
            context={"key":inforate}            
            return render(request,'info.html',context)
    
    except:
        return render(request,'index.html')
    
    return render(request,'index.html')
        
def info(request): 
    return render(request,'info.html')
        
  

