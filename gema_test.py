import tkinter as tk
from tkinter import ttk, messagebox
import os, json

BASE=os.path.dirname(os.path.abspath(__file__))
DATA=os.path.join(BASE,"data")
os.makedirs(DATA,exist_ok=True)

def load(n,d):
    p=os.path.join(DATA,n)
    try:
        with open(p,encoding="utf-8") as f:return json.load(f)
    except:return d
def save(n,x):
    with open(os.path.join(DATA,n),"w",encoding="utf-8") as f:json.dump(x,f,indent=2)

businesses=load("businesses.json",[
 {"name":"Demo Agro Processing Ltd","sector":"Agriculture & Food Processing","location":"Lusaka","status":"Demo"},
 {"name":"Demo Copper Components Ltd","sector":"Mining Supply & Manufacturing","location":"Copperbelt","status":"Demo"}])
projects=load("projects.json",[
 {"name":"Zambia Agro-Processing Expansion","sector":"Agriculture","stage":"Feasibility","funding":"USD 2.5M"},
 {"name":"Industrial Components Plant","sector":"Manufacturing","stage":"Investor Matching","funding":"USD 5M"}])
matches=load("matches.json",[])

app=tk.Tk()
app.title("GEMA — Zambia Open Marketplace & Industrial Intelligence Platform")
app.geometry("1280x800"); app.minsize(1000,650)
style=ttk.Style()
try: style.theme_use("clam")
except: pass

header=tk.Frame(app,bg="#172554",height=70); header.pack(fill="x")
tk.Label(header,text="GEMA",font=("Segoe UI",25,"bold"),fg="white",bg="#172554").pack(side="left",padx=24)
tk.Label(header,text="Zambia Open Marketplace & Industrial Intelligence Platform",
         font=("Segoe UI",11),fg="#dbeafe",bg="#172554").pack(side="left")

body=tk.Frame(app); body.pack(fill="both",expand=True)
nav=tk.Frame(body,bg="#0f172a",width=225); nav.pack(side="left",fill="y")
main=tk.Frame(body,bg="#f8fafc"); main.pack(side="right",fill="both",expand=True)

def clear():
    for w in main.winfo_children():w.destroy()
def page(t,s=""):
    tk.Label(main,text=t,font=("Segoe UI",24,"bold"),bg="#f8fafc",fg="#0f172a").pack(anchor="w",padx=30,pady=(25,2))
    tk.Label(main,text=s,font=("Segoe UI",10),bg="#f8fafc",fg="#64748b").pack(anchor="w",padx=30,pady=(0,18))
def dash():
    clear(); page("GEMA Dashboard","Desktop test build — Stage 2 foundation + integrated investment workflow")
    r=tk.Frame(main,bg="#f8fafc"); r.pack(fill="x",padx=24)
    for h,v in [("Businesses",len(businesses)),("Investment Projects",len(projects)),("Investor Matches",len(matches)),("Status","TEST BUILD")]:
        f=tk.Frame(r,bg="white",highlightbackground="#e2e8f0",highlightthickness=1);f.pack(side="left",fill="both",expand=True,padx=6)
        tk.Label(f,text=h,font=("Segoe UI",10),fg="#64748b",bg="white").pack(anchor="w",padx=15,pady=(14,2))
        tk.Label(f,text=str(v),font=("Segoe UI",18,"bold"),bg="white").pack(anchor="w",padx=15,pady=(0,14))
    f=tk.Frame(main,bg="white",highlightbackground="#e2e8f0",highlightthickness=1);f.pack(fill="both",expand=True,padx=30,pady=22)
    tk.Label(f,text="Full GEMA test journey",font=("Segoe UI",15,"bold"),bg="white").pack(anchor="w",padx=20,pady=18)
    for x in ["Register a business/profile","Discover marketplace products and services","Explore industrial opportunities",
              "Create an investment project","Run explainable investor matching","Test due diligence / data room / term-sheet workflow"]:
        tk.Label(f,text="  • "+x,font=("Segoe UI",11),bg="white").pack(anchor="w",padx=25,pady=5)
def biz():
    clear(); page("Business Directory","Create and view reusable GEMA business profiles")
    ttk.Button(main,text="Add Demo Business",command=addbiz).pack(anchor="w",padx=30)
    tr=ttk.Treeview(main,columns=("name","sector","location","status"),show="headings")
    for c,w in zip(("name","sector","location","status"),(350,300,180,160)):tr.heading(c,text=c.title());tr.column(c,width=w)
    tr.pack(fill="both",expand=True,padx=30,pady=18)
    for b in businesses:tr.insert("", "end",values=(b["name"],b["sector"],b["location"],b["status"]))
def addbiz():
    w=tk.Toplevel(app);w.title("GEMA — Business Registration");w.geometry("500x330");es=[]
    for l in ["Business name","Sector","Location"]:
        tk.Label(w,text=l).pack(anchor="w",padx=20,pady=(15,2));e=tk.Entry(w);e.pack(fill="x",padx=20);es.append(e)
    def go():
        if not es[0].get().strip():return
        businesses.append({"name":es[0].get(),"sector":es[1].get(),"location":es[2].get(),"status":"User-created demo"})
        save("businesses.json",businesses);w.destroy();biz()
    ttk.Button(w,text="Save Business",command=go).pack(pady=22)
def market():
    clear();page("Marketplace","Stage 2 discovery layer")
    q=tk.Entry(main,font=("Segoe UI",11),width=65);q.pack(anchor="w",padx=30)
    ttk.Button(main,text="Search",command=lambda:messagebox.showinfo("GEMA Search","Search executed for: "+(q.get() or "all opportunities"))).pack(anchor="w",padx=30,pady=8)
    lb=tk.Listbox(main,font=("Segoe UI",11));lb.pack(fill="both",expand=True,padx=30,pady=10)
    for x in ["Agricultural processing equipment","Copper value-add manufacturing","Fertilizer blending",
              "Cold-chain logistics","Solar industrial power systems","Zambian SME products and services"]:lb.insert("end",x)
def industrial():
    clear();page("Industrial Intelligence","Sector opportunity discovery")
    for s in ["Agriculture & Food Processing","Mining & Mineral Value Addition","Manufacturing","Energy & Utilities","Logistics & Infrastructure","ICT & Digital Services"]:
        f=tk.Frame(main,bg="white",highlightbackground="#e2e8f0",highlightthickness=1);f.pack(fill="x",padx=30,pady=5)
        tk.Label(f,text=s,font=("Segoe UI",12,"bold"),bg="white").pack(side="left",padx=15,pady=13)
        ttk.Button(f,text="Explore",command=lambda z=s:messagebox.showinfo("GEMA",f"Exploring {z} opportunities.")).pack(side="right",padx=15)
def invest():
    clear();page("Investment Projects","Projects, feasibility, pipeline and investor matching")
    ttk.Button(main,text="Create Demo Project",command=addproj).pack(anchor="w",padx=30)
    tr=ttk.Treeview(main,columns=("name","sector","stage","funding"),show="headings")
    for c,w in zip(("name","sector","stage","funding"),(380,220,200,180)):tr.heading(c,text=c.title());tr.column(c,width=w)
    tr.pack(fill="both",expand=True,padx=30,pady=18)
    for p in projects:tr.insert("", "end",values=(p["name"],p["sector"],p["stage"],p["funding"]))
def addproj():
    w=tk.Toplevel(app);w.title("Create Investment Project");w.geometry("520x360");es=[]
    for l in ["Project name","Sector","Stage","Funding requirement"]:
        tk.Label(w,text=l).pack(anchor="w",padx=20,pady=(12,2));e=tk.Entry(w);e.pack(fill="x",padx=20);es.append(e)
    def go():
        projects.append({"name":es[0].get(),"sector":es[1].get(),"stage":es[2].get(),"funding":es[3].get()})
        save("projects.json",projects);w.destroy();invest()
    ttk.Button(w,text="Save Project",command=go).pack(pady=20)
def matching():
    clear();page("Investor Matching","Explainable matching signals: sector, geography, ticket and capability")
    combo=ttk.Combobox(main,values=[p["name"] for p in projects],state="readonly",width=65);combo.pack(anchor="w",padx=30,pady=5)
    out=tk.Text(main,height=15,font=("Consolas",10));out.pack(fill="both",expand=True,padx=30,pady=12)
    def run():
        r={"project":combo.get() or "Selected project","investor":"Demo Industrial Growth Fund","score":86,
           "factors":["Sector alignment","Funding range alignment","Zambia/regional focus","Industrial capability fit"]}
        matches.append(r);save("matches.json",matches);out.delete("1.0","end");out.insert("end",json.dumps(r,indent=2))
    ttk.Button(main,text="Run Explainable Match",command=run).pack(anchor="w",padx=30)
def workflow():
    clear();page("Deal Workflow","Due diligence → secure data room → term sheet → closing readiness → monitoring")
    for i,s in enumerate(["Due Diligence","Secure Data Room","Term Sheet & Negotiation","Closing Readiness","Monitoring"],1):
        f=tk.Frame(main,bg="white",highlightbackground="#cbd5e1",highlightthickness=1);f.pack(fill="x",padx=30,pady=5)
        tk.Label(f,text=f"{i}. {s}",font=("Segoe UI",12,"bold"),bg="white").pack(side="left",padx=15,pady=13)
        ttk.Button(f,text="Open",command=lambda z=s:messagebox.showinfo("GEMA Workflow",z+" opened in test mode.")).pack(side="right",padx=15)
def analytics():
    clear();page("Analytics","Local test database summary")
    for x,n in [("Business records",len(businesses)),("Projects",len(projects)),("Investor matches",len(matches))]:
        tk.Label(main,text=f"{x}: {n}",font=("Segoe UI",13),bg="#f8fafc").pack(anchor="w",padx=40,pady=7)
def admin():
    clear();page("Administration","Development controls")
    ttk.Button(main,text="Reset Demo Data",command=reset).pack(anchor="w",padx=30,pady=10)
    tk.Label(main,text="This is a development test build, not production software.",fg="#64748b",bg="#f8fafc").pack(anchor="w",padx=30,pady=20)
def reset():
    global businesses,projects,matches
    businesses=[{"name":"Demo Agro Processing Ltd","sector":"Agriculture & Food Processing","location":"Lusaka","status":"Demo"},{"name":"Demo Copper Components Ltd","sector":"Mining Supply & Manufacturing","location":"Copperbelt","status":"Demo"}]
    projects=[{"name":"Zambia Agro-Processing Expansion","sector":"Agriculture","stage":"Feasibility","funding":"USD 2.5M"},{"name":"Industrial Components Plant","sector":"Manufacturing","stage":"Investor Matching","funding":"USD 5M"}]
    matches=[];save("businesses.json",businesses);save("projects.json",projects);save("matches.json",matches);dash()

for name,cmd in [("Dashboard",dash),("Business Directory",biz),("Marketplace",market),("Industrial Intelligence",industrial),("Investment Projects",invest),("Investor Matching",matching),("Deal Workflow",workflow),("Analytics",analytics),("Administration",admin)]:
    tk.Button(nav,text=name,command=cmd,anchor="w",font=("Segoe UI",10),fg="#e2e8f0",bg="#0f172a",activebackground="#1e3a8a",relief="flat",padx=20,pady=11).pack(fill="x")
tk.Label(nav,text="\nGEMA TEST BUILD\nStage 2 foundation\n+ investment workflow",fg="#94a3b8",bg="#0f172a",justify="left").pack(anchor="w",padx=20,pady=25)
dash();app.mainloop()
