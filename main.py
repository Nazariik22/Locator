from flask import Flask,redirect,render_template,request
import requests
app=Flask(__name__,
          static_url_path="",
          )


#data = requests.get(f"https://ipinfo.io/178.92.10.153/geo").json()


#print(data)
@app.route("/",methods=["GET","POST"])

def index():
    data_ip=requests.get("https://api.ipify.org/?format=json").json()["ip"]
    if request.method=="POST":
      data = requests.get(f"https://ipinfo.io/{data_ip}/geo").json()
      print(data)
      return render_template("index1.html",data_ip=data_ip,data=data)
    return render_template("index.html",data_ip=data_ip)
app.run()





#def index():
#    return redirect("https://www.instagram.com/")