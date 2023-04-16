from flask import Flask,redirect,url_for,render_template,request
import pickle
from sklearn.ensemble import RandomForestClassifier
import numpy as np
with open("RandomTreeModel.pickle","rb") as f:
    model=pickle.load(f)





app=Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/result',methods=['GET','POST'])
def result():
    l=[]
    if request.method=='POST':
        age=int(request.form.get("age"))
        hours=int(request.form.get("hours"))
        choice=int(request.form["ans"])
        bpm=int(request.form.get("bpm"))
        occupation=int(request.form.get("fav_genre"))
        freq_classical=int(request.form.get("classical"))
        freq_country=int(request.form.get("country"))
        freq_edm=int(request.form.get("edm"))
        freq_folk=int(request.form.get("folk"))
        freq_gospel=int(request.form.get("gospel"))
        freq_hip_hop=int(request.form.get("hip-hop"))
        freq_jazz=int(request.form.get("jazz"))
        freq_k_pop=int(request.form.get("k-pop"))
        freq_latin=int(request.form.get("latin"))
        freq_lofi=int(request.form.get("lofi"))
        freq_metal=int(request.form.get("metal"))
        freq_pop=int(request.form.get("pop"))
        freq_rb=int(request.form.get("r&b"))
        freq_rap=int(request.form.get("rap"))
        freq_rock=int(request.form.get("rock"))
        freq_video_game_music=int(request.form.get("video-game-music"))
        anxiety=int(request.form.get("anxiety"))
        depression=int(request.form.get("depression"))
        insomnia=int(request.form.get("insomnia"))
        ocd=int(request.form.get("ocd"))
        #print(f"{age},{hours},{choice},{bpm},{occupation},{freq_classical},{freq_country},{freq_edm},{freq_folk},{freq_folk},{freq_gospel},{freq_hip_hop},{freq_jazz},{freq_k_pop},{freq_latin},{freq_lofi},{freq_metal},{freq_pop},{freq_rap},{freq_rb},{freq_rock},{freq_rock},{freq_video_game_music},{anxiety},{depression},{insomnia},{ocd}")
        l=[age,hours,choice,bpm,occupation,freq_classical,freq_country,freq_edm,freq_folk,freq_gospel,freq_hip_hop,freq_jazz,freq_k_pop,freq_latin,freq_lofi,freq_metal,freq_pop,freq_rap,freq_rb,freq_rock,freq_video_game_music,anxiety,depression,insomnia,ocd]
        
        z=np.array(l).reshape(1,-1)
        p=list(model.predict(z))
        return render_template("result.html",data=p)


    return render_template('result.html',data=l)

if __name__=="__main__":
    app.run(debug=False,host=0.0.0.0)
